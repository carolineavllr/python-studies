import sqlite3

conn = sqlite3.connect("banco-de-dados/escola.db")
cursor = conn.cursor()

cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS alunos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        idade INTEGER NOT NULL,
        turma TEXT NOT NULL
    )
    """
)

cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS disciplinas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome_disciplina TEXT NOT NULL,
        estudante_id INTEGER,
        FOREIGN KEY (estudante_id) REFERENCES alunos (id)
    )
    """
)

cursor.execute(
    """
    INSERT INTO alunos (nome, idade, turma)
    VALUES
        ('Alice', 20, 'Turma A'),
        ('Bob', 22, 'Turma B'),
        ('Charlie', 21, 'Turma A')
    """
)

cursor.execute(
    """
    UPDATE alunos
    SET idade = 23
    WHERE nome = 'Bob'
    """
)

cursor.execute(
    """
    SELECT * FROM alunos
    """
)

alunos = cursor.fetchall()

for aluno in alunos:
    print(aluno)

conn.commit()
conn.close()
