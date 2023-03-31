# Importando o SQL Lite
import sqlite3

# Criando Conexao

try:
    con = sqlite3.connect('cadastro_alunos.db')
    print('Conexao com bando de dados realizado com sucesso!')
except sqlite3.Error as e:
    print('Erro ao conectar com o banco de dados', e)

# Criando a tabela de cursos
try:
    with con:
        cur = con.cursor()
        cur.execute('''CREATE TABLE cursos
                 (id INTEGER PRIMARY KEY,
                 nome TEXT,
                 duracao INTEGER,
                 preco REAL
                 )''')
        print("Tabela cursos criado com sucesso")

except sqlite3.Error as e:
    print('Erro ao criar a tabela cursos', e)

# Criando a tabela de turmas
try:
    with con:
        cur = con.cursor()
        cur.execute('''CREATE TABLE turmas
                 (id INTEGER PRIMARY KEY,
                 nome TEXT,
                 curso_nome TEXT,
                 data_inicio DATE,
                 FOREIGN KEY (curso_nome) REFERENCES cursos (nome) ON UPDATE CASCADE ON DELETE CASCADE
                 )''')
        print("Tabela turmas criado com sucesso")

except sqlite3.Error as e:
    print('Erro ao criar a tabela turmas', e)

# Criando a tabela de alunos
try:
    with con:
        cur = con.cursor()
        cur.execute('''CREATE TABLE alunos
                 (id INTEGER PRIMARY KEY,
                 nome TEXT,
                 email TEXT,
                 telefone TEXT,
                 imagem TEXT,
                 data_nascimento DATE,
                 cpf TEXT,
                 turma_nome TEXT,
                 FOREIGN KEY (turma_nome) REFERENCES turmas (nome) ON DELETE CASCADE
                 )''')
        print("Tabela alunos criado com sucesso")

except sqlite3.Error as e:
    print('Erro ao criar a tabela alunos', e)