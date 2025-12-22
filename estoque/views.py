from django.shortcuts import render, redirect, get_object_or_404
from .models import Produto, Movimentacao, Categoria, Fornecedor
from django.db.models import Q
from django.contrib import messages

def adicionar_produto(request):
    if request.method == "POST":
        nome = request.POST.get("nome")
        descricao = request.POST.get("descricao")
        preco_compra = request.POST.get("preco_compra")
        preco = request.POST.get("preco")
        quantidade = request.POST.get("quantidade")
        categoria_id = request.POST.get("categoria")
        fornecedor_id = request.POST.get("fornecedor")

        categoria = Categoria.objects.get(id=categoria_id)
        fornecedor = Fornecedor.objects.get(id=fornecedor_id)

        Produto.objects.create(
            nome=nome,
            descricao=descricao,
            preco_compra=preco_compra,
            preco=preco,
            quantidade=quantidade,
            categoria=categoria,
            fornecedor=fornecedor
        )

        messages.success(request, "Produto cadastrado com sucesso!")
        return redirect("listar_produtos")

    categorias = Categoria.objects.all()
    fornecedores = Fornecedor.objects.all()
    return render(request, "estoque/adicionar_produto.html", {
        "categorias": categorias,
        "fornecedores": fornecedores
    })

def excluir_produto(request, produto_id):
    produto = get_object_or_404(Produto, id=produto_id)
    produto.ativo = False
    produto.save()

    messages.warning(request, "Produto excluído com sucesso!")
    return redirect("listar_produtos")

def editar_produto(request, produto_id):
    produto = get_object_or_404(Produto, id=produto_id)

    if request.method == "POST":
        produto.nome = request.POST.get("nome")
        produto.descricao = request.POST.get("descricao")
        produto.preco_compra = request.POST.get("preco_compra")
        produto.preco = request.POST.get("preco")
        produto.categoria_id = request.POST.get("categoria")
        produto.fornecedor_id = request.POST.get("fornecedor")
        produto.save()

        messages.success(request, "Produto atualizado com sucesso!")
        return redirect("listar_produtos")

    categorias = Categoria.objects.all()
    fornecedores = Fornecedor.objects.all()

    return render(request, "estoque/editar_produto.html", {
        "produto": produto,
        "categorias": categorias,
        "fornecedores": fornecedores
    })

def detalhes_produto(request, produto_id):
    produto = get_object_or_404(Produto, id=produto_id)
    return render(request, "estoque/detalhes_produto.html", {
        "produto": produto
    })

def registrar_movimentacao(request, produto_id):
    produto = get_object_or_404(Produto, id=produto_id)

    if request.method == "POST":
        tipo = request.POST.get("tipo")
        quantidade = int(request.POST.get("quantidade"))

        if tipo == "saida" and quantidade > produto.quantidade:
            return render(request, "estoque/erro.html", {
                "mensagem": f"Não há estoque suficiente. Quantidade disponível: {produto.quantidade}"
            })

        mov = Movimentacao.objects.create(
            produto=produto,
            tipo=tipo,
            quantidade=quantidade,
        )

        mov.aplicar_movimentacao()

        messages.success(request, "Movimentação efetuada com sucesso!")
        return redirect("listar_produtos")

    return render(request, "estoque/registrar_movimentacao.html", {"produto": produto})

def historico_movimentacoes(request, produto_id):
    produto = get_object_or_404(Produto, id=produto_id)
    movimentacoes = Movimentacao.objects.filter(produto=produto).order_by("-data")

    return render(request, "estoque/historico_movimentacoes.html", {
        "produto": produto,
        "movimentacoes": movimentacoes
    })

def adicionar_categoria(request):
    if request.method == "POST":
        nome = request.POST.get("nome")

        Categoria.objects.create(nome=nome)
        return redirect("lista_categorias")

    messages.success(request, "Categoria adicionada com sucesso!")
    return render(request, "estoque/categorias/categoria_form.html")

def lista_categorias(request):
    categorias = Categoria.objects.all()
    return render(request, "estoque/categorias/categoria_lista.html", {"categorias": categorias})

def editar_categoria(request, categoria_id):
    categoria = get_object_or_404(Categoria, id=categoria_id)

    if request.method == "POST":
        categoria.nome = request.POST.get("nome")
        categoria.descricao = request.POST.get("descricao")
        categoria.save()

        messages.success(request, "Categoria atualizada com sucesso!")
        return redirect("lista_categorias")

    return render(request, "estoque/categorias/categoria_form.html", {
        "categoria": categoria
    })


def excluir_categoria(request, categoria_id):
    categoria = get_object_or_404(Categoria, id=categoria_id)

    produtos_relacionados = Produto.objects.filter(
    categoria=categoria,
    ativo=True
    ).exists()


    if produtos_relacionados:
        return render(request, "estoque/erro.html", {
            "mensagem": "Não é possível excluir esta categoria porque existem produtos cadastrados usando ela."
        })

    categoria.delete()

    messages.warning(request, "Categoria removida com sucesso!")
    return redirect("lista_categorias")


def adicionar_fornecedor(request):
    if request.method == "POST":
        nome = request.POST.get("nome")
        telefone = request.POST.get("telefone")
        email = request.POST.get("email")

        telefone = telefone.replace("(", "").replace(")", "").replace("-", "").replace(" ", "")

        if len(telefone) != 11:
            messages.error(request, "Telefone inválido.")
            return redirect("lista_fornecedores")

        Fornecedor.objects.create(
            nome=nome,
            telefone=telefone,
            email=email
        )

        messages.success(request, "Fornecedor adicionado com sucesso!")
        return redirect("lista_fornecedores")

    return render(request, "estoque/fornecedores/fornecedor_form.html")

def lista_fornecedores(request):
    fornecedores = Fornecedor.objects.all()
    return render(request, "estoque/fornecedores/fornecedor_lista.html", {"fornecedores": fornecedores})

def editar_fornecedor(request, fornecedor_id):
    fornecedor = get_object_or_404(Fornecedor, id=fornecedor_id)

    if request.method == "POST":
        fornecedor.nome = request.POST.get("nome")
        fornecedor.telefone = request.POST.get("telefone")
        fornecedor.email = request.POST.get("email")
        fornecedor.save()

        messages.success(request, "Fornecedor atualizado com sucesso!")
        return redirect("lista_fornecedores")

    return render(request, "estoque/fornecedores/fornecedor_form.html", {
        "fornecedor": fornecedor
    })


def excluir_fornecedor(request, fornecedor_id):
    fornecedor = get_object_or_404(Fornecedor, id=fornecedor_id)

    fornecedor_relacionados = Produto.objects.filter(
    fornecedor=fornecedor,
    ativo=True
    ).exists()

    if fornecedor_relacionados:
        return render(request, "estoque/erro.html", {
            "mensagem": "Não é possível excluir este fornecedor porque existem produtos cadastrados usando ela."
        })
    
    fornecedor.delete()

    messages.warning(request, "Fornecedor removido com sucesso!")
    return redirect("lista_fornecedores")

def historico_geral(request):
    movimentacoes = Movimentacao.objects.all().order_by('-data')

    for m in movimentacoes:
        m.valor_total = m.quantidade * m.produto.preco

    return render(request, "estoque/historico_geral.html", {
        "movimentacoes": movimentacoes
    })

def listar_produtos(request):
    query = request.GET.get('q', '')

    if query:
        produtos = Produto.objects.filter(
            Q(ativo=True) &
            (Q(nome__icontains=query) |
             Q(categoria__nome__icontains=query) |
             Q(fornecedor__nome__icontains=query))
        )
    else:
        produtos = Produto.objects.filter(ativo=True)

    return render(request, "estoque/listar_produtos.html", {"produtos": produtos})

def listar_categoria(request):
    query = request.GET.get('q', '')

    if query:
        categorias = Categoria.objects.filter(
            nome__icontains=query
        )
    else:
        categorias = Categoria.objects.all()

    return render(
        request,
        "estoque/categorias/categoria_lista.html",
        {"categorias": categorias}
    )

def listar_fornecedores(request):
    query = request.GET.get('q', '')

    if query:
        fornecedores = Fornecedor.objects.filter(
            nome__icontains=query
        )
    else:
        fornecedores = Fornecedor.objects.all()

    return render(
        request,
        "estoque/fornecedores/fornecedor_lista.html",
        {"fornecedores": fornecedores}
    )