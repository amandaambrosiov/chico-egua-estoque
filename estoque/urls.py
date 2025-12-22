from django.urls import path
from . import views

urlpatterns = [
    path("", views.listar_produtos, name="listar_produtos"),
    path("adicionar/", views.adicionar_produto, name="adicionar_produto"),
    path("editar/<int:produto_id>/", views.editar_produto, name="editar_produto"),
    path("movimentar/<int:produto_id>/", views.registrar_movimentacao, name="registrar_movimentacao"),
    path("historico/<int:produto_id>/", views.historico_movimentacoes, name="historico_movimentacoes"),
    path("produtos/<int:produto_id>/excluir/", views.excluir_produto, name="excluir_produto"),
    path('produto/<int:produto_id>/detalhes/', views.detalhes_produto, name='detalhes_produto'),

    path("categorias/", views.listar_categoria, name="listar_categoria"),
    path("categorias/", views.lista_categorias, name="lista_categorias"),
    path("categorias/adicionar/", views.adicionar_categoria, name="adicionar_categoria"),
    path("categorias/<int:categoria_id>/editar/", views.editar_categoria, name="editar_categoria"),
    path("categorias/<int:categoria_id>/excluir/", views.excluir_categoria, name="excluir_categoria"),

    path("fornecedores/", views.listar_fornecedores, name="listar_fornecedores"),
    path("fornecedores/", views.lista_fornecedores, name="lista_fornecedores"),
    path("fornecedores/adicionar/", views.adicionar_fornecedor, name="adicionar_fornecedor"),
    path("fornecedores/<int:fornecedor_id>/editar/", views.editar_fornecedor, name="editar_fornecedor"),
    path("fornecedores/<int:fornecedor_id>/excluir/", views.excluir_fornecedor, name="excluir_fornecedor"),

    path("historico/", views.historico_geral, name="historico_geral"),

]
