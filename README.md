# 📦 Controle de Estoque

O Controle de Estoque é um sistema web desenvolvido em Django 6 para gerenciar produtos, categorias, fornecedores e movimentações de estoque. Permite registrar entradas e saídas, manter histórico de movimentações e controlar produtos ativos, além de possibilitar operações CRUD (Criar, Ler, Atualizar e Excluir) de categorias e fornecedores.

## Tecnologias Utilizadas

- Linguagem: Python 3.14
- Framework Web: Django 6.0
- Banco de Dados: SQLite (padrão Django)
- Front-end: HTML5, CSS3, Bootstrap 5
- Controle de Versão: Git
- Virtual Environment: venv

## Funcionalidades

### Produtos
- Listar produtos ativos.
- Adicionar, editar e excluir produtos (soft delete ou delete real, conforme necessidade).
- Registrar movimentações (entrada e saída) para cada produto.
- Histórico detalhado de movimentações de cada produto, mostrando quantidade, data e valor total.

### Categorias
- Criar, editar e excluir categorias.
- Validação: não é possível excluir categorias que possuem produtos vinculados.

### Fornecedores
- Criar, editar e excluir fornecedores.
- Validação: não é possível excluir fornecedores que possuem produtos vinculados.

### Movimentações
- Registrar entrada e saída de produtos.
- Histórico detalhado com quantidade, data e valor total (preço unitário × quantidade).
