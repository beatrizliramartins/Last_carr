import sqlite3 as lite
from datetime import datetime

# Criando conexão
con = lite.connect('dados.db')


# Inserir inventorio
def inserir_form(i):
    with con:
        cur = con.cursor()
        query = "INSERT INTO Inventarioo (nome, local, descricao, marca, data_da_compra, valor_da_compra, serie, imagem) VALUES (?,?,?,?,?,?,?,?)"
        cur.execute(query, i)


# Deletar inventorio
def deletar_form(i):
    with con:
        cur = con.cursor()
        query = "DELETE FROM Inventarioo WHERE id=?"
        cur.execute(query, i)


# Atualizar inventorio
def atualizar_form(i):
    with con:
        cur = con.cursor()
        query = "UPDATE Inventarioo SET nome=?, local=?, descricao=?, marca=?, data_da_compra=?, valor_da_compra=?, serie=?, imagem=? WHERE id=?"
        cur.execute(query, i)


# Ver Inventario
def ver_form():
    lista_itens = []
    with con:
        cur = con.cursor()
        cur.execute("SELECT * FROM Inventarioo")
        rows = cur.fetchall()
        for row in rows:
            lista_itens.append(row)
    return lista_itens


# Ver Iten no inventorio
def ver_iten(id):
    lista_itens = []
    with con:
        cur = con.cursor()
        cur.execute("SELECT * FROM Inventarioo WHERE id=?", (id))
        rows = cur.fetchall()
        for row in rows:
            lista_itens.append(row)
    return lista_itens