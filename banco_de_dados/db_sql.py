import sqlite3

# conecta ao banco de dados (ou cria se não existir)
conn = sqlite3.connect('banco-de-dados/exemplo-relacional.db')
cursor = conn.cursor()

# criar tabela
cursor.execute('''
CREATE TABLE IF NOT EXISTS usuarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE
)
''')

# inserir dados
cursor.execute('''
INSERT INTO usuarios (nome, email) VALUES (?, ?)
''', ("Alice", "alice@example.com"))

cursor.execute('''
INSERT INTO usuarios (nome, email) VALUES (?, ?)
''', ("Bob", "bob@example.com"))

cursor.execute('''
INSERT INTO usuarios (nome, email) VALUES (?, ?)
''', ("Charlie", "charlie@example.com"))

# salvar as alterações
conn.commit()

# ler os dados
cursor.execute('SELECT * FROM usuarios')
usuarios = cursor.fetchall()
for usuario in usuarios:
    print(usuario)

# fechar a conexão
conn.close()