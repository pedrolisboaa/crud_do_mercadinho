import sqlite3


class Dados:
    def __init__(self):
        self.conexao = sqlite3.connect('base_de_dados.db')
        self.cursor = self.conexao.cursor()

    def inserir_dados(self, dado):
        self.cursor.execute('INSERT INTO estoque (PRODUTO, PRECO, QUANTIDADE) VALUES  (?, ?, ?)', dado)
        self.conexao.commit()

    def excluir_dado(self, produto):
        sql = 'DELETE FROM estoque WHERE PRODUTO=?'
        self.cursor.execute(sql, (produto,))
        self.conexao.commit()

    def atualizar_dado(self, antigo, novo):
        # VEI tem que colocar '' (aspas simples) para o update
        self.cursor.execute(f"UPDATE estoque SET PRODUTO = '{novo}' WHERE PRODUTO = '{antigo}'")
        self.conexao.commit()

    def mostrar_banco(self):
        self.cursor.execute('SELECT * FROM estoque')
        for linha in self.cursor.fetchall():
            print(linha)

    def fechar_banco_de_dados(self):
        self.cursor.close()
        self.conexao.close()


if __name__ == '__main__':
    teste = Dados()
    enviar = ('banana', 4.50, 10)
    teste.inserir_dados(enviar)
