# Importando o SQL Lite
import sqlite3 as lite

# Criando Conexao

try:
    con = lite.connect('cadastro_alunos.db')
    print('Conexao com banco de dados realizado com sucesso!')
except lite.Error as e:
    print('Erro ao conectar com o banco de dados', e)


# Trabalhando com a tabela de cursos

# CREATE cursos

def criar_cursos(i):
    with con:
        cur = con.cursor()
        query = "INSERT INTO cursos(nome, duracao, preco) VALUES(?,?,?)"
        cur.execute(query, i)


# criar_cursos(['Python', '2 semanas', 50])

# UPDATE cursos (UPDATE U)
def ver_cursos():
    lista = []
    with con:
        cur = con.cursor()
        cur.execute('SELECT * FROM cursos')
        linha = cur.fetchall()

        for i in linha:
            lista.append(i)
            return lista


#print(ver_cursos())

# Atualizar cursos (Updat U)

def atualizar_cursos(i):
    with con:
        cur = con.cursor()
        query = "UPDATE cursos SET nome=?, duracao=?, preco=? WHERE id=?"
        cur.execute(query, i)


l = ['Python', 'Duas semanas', 50.0, 1]


# atualizar_cursos(l)

# Deletar cursos (DELETE D)

def deletar_cursos(i):
    with con:
        cur = con.cursor()
        query = "DELETE FROM cursos WHERE=id?"
        cur.execute(query, i)


#deletar_cursos[1]

# Tabela de Turmas -----------------------------------------

# Criar turmas (insert)

def criar_turma(i):
    with con:
        cur = con.cursor()
        query = "INSERT INTO turmas (nome, cursos_nome, data_inicio) VALUES (?, ?, ?)"
        cur.execute(query, i)


# READ turmas

def ver_turmas():
    lista = []
    with con:
        cur = con.cursor()
        cur.execute('SELECT * FROM turmas')
        linha = cur.fetchall()

        for i in linha:
            lista.append(i)
            return lista

# Atualizar turmas (Updat U)

def atualizar_turmas(i):
    with con:
        cur = con.cursor()
        query = "UPDATE turmas SET nome=?, cursos_nome=?, data_inicio=? WHERE id=?"
        cur.execute(query, i)

# Deletar turmas (DELETE D)

def deletar_turmas(i):
    with con:
        cur = con.cursor()
        query = "DELETE FROM turmas WHERE=id?"
        cur.execute(query, i)

# Tabela Alunos  -----------------------------------------


# Criar Alunos (insert)

def criar_alunos(i):
    with con:
        cur = con.cursor()
        query = "INSERT INTO alunos (nome, email, telefone, imagem, data_nascimento, cpf, turma_nome) VALUES (?, ?, ?, ?, ?, ?, ?)"
        cur.execute(query, i)


# READ Alunos

def ver_alunos():
    lista = []
    with con:
        cur = con.cursor()
        cur.execute('SELECT * FROM alunos')
        linha = cur.fetchall()

        for i in linha:
            lista.append(i)
            return lista

# Atualizar Alunos (Updat U)

def atualizar_alunos(i):
    with con:
        cur = con.cursor()
        query = "UPDATE alunos SET nome=?, email=?, telefone=?, imagem=?, data_nascimento=?, cpf=?, turma_nome=? WHERE id=?"
        cur.execute(query, i)

# Deletar Alunos (DELETE D)

def deletar_alunos(i):
    with con:
        cur = con.cursor()
        query = "DELETE FROM alunos WHERE=id?"
        cur.execute(query, i)






