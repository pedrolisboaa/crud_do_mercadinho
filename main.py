from tkinter import *
from dados import Dados
from tkinter import messagebox
import constantes


def inserir_produto_bd():
    produto = input_criar_produto.get()
    quantidade = input_qtd_produto.get()
    preco = input_preco_produto.get()

    Dados().inserir_dados((produto, quantidade, preco))
    limpar_adicionar_produtos(produto, quantidade, preco)


def limpar_adicionar_produtos(produto, quantidade, preco):
    input_criar_produto.delete(0, END)
    input_qtd_produto.delete(0, END)
    input_preco_produto.delete(0, END)

    messagebox.showinfo(title=f'Adicionado {produto}', message=f'Quantidade: {quantidade}\nPreço: {preco}')


def apagar_produto_bd():
    produto_a_ser_apagado = input_remover_produto.get()
    Dados().excluir_dado(produto_a_ser_apagado)

    messagebox.showinfo(title=f'Apagado', message=f'Foi apagado o produto {produto_a_ser_apagado}')
    input_remover_produto.delete(0, END)


def substituir_produto():
    produto_antigo_estoque = input_sbt_produto.get()
    novo_produto_estoque = input_novo_produto.get()
    Dados().atualizar_dado(produto_antigo_estoque, novo_produto_estoque)
    messagebox.showinfo(title=f'Atualizado', message=f'Foi atualizado o produto {produto_antigo_estoque} para {novo_produto_estoque}')
    input_remover_produto.delete(0, END)


def mostrar_todo_banco():
    Dados().mostrar_banco()




# --------------------------------O PRINCIPAL-----------------------------------#
janela = Tk()
janela.title('Estoque Mercadinho do Pedrão')
janela.config(width=800, height=600, padx=20, pady=20, background=constantes.FUNDO)

# ------------------------------ADICIONAR PRODUTO-------------------------------#

# Labels
criar_produto = Label(text='Criar Produto: ')
criar_produto.grid(column=0, row=0)

qtd_produto = Label(text='Quantidade')
qtd_produto.grid(column=0, row=1)

preco_produto = Label(text='Preço')
preco_produto.grid(column=0, row=2)

# Inputs
input_criar_produto = Entry()
input_criar_produto.grid(column=1, row=0)

input_qtd_produto = Entry()
input_qtd_produto.grid(column=1, row=1)

input_preco_produto = Entry()
input_preco_produto.grid(column=1, row=2)

# Botão
btn_adicionar_produto = Button(text='Adicionar Produto', command=inserir_produto_bd)
btn_adicionar_produto.grid(column=0, row=3, columnspan=2)

# ------------------------------REMOVER PRODUTO-------------------------------#
# Labels

remover_produto = Label(text='Remover produto')
remover_produto.grid(column=2, row=0)

# Input
input_remover_produto = Entry()
input_remover_produto.grid(column=3, row=0)

# Botão
btn_remover_produto = Button(text='Remover produto', command=apagar_produto_bd)
btn_remover_produto.grid(column=2, row=2, columnspan=2)

# ------------------------------SUBSTITUIR PRODUTO-------------------------------#
# Labels
sbt_produto = Label(text='Substituir produto')
sbt_produto.grid(column=0, row=4)

novo_produto = Label(text='Novo produto')
novo_produto.grid(column=0, row=5)

# Inputs
input_sbt_produto = Entry()
input_sbt_produto.grid(column=1, row=4)

input_novo_produto = Entry()
input_novo_produto.grid(column=1, row=5)

# Botão
btn_substituir = Button(text='Substituir Produto', command=substituir_produto)
btn_substituir.grid(column=0, row=7, columnspan=2)

# ------------------------------MOSTRAR TODOS PRODUTOS-------------------------------#
btn_mostrar_tudo = Button(text='Mostrar Estoque', command=mostrar_todo_banco)
btn_mostrar_tudo.grid(column=2, row=5, columnspan=2)

janela.mainloop()
