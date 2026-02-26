import sqlite3


def conectar_banco():
    return sqlite3.connect("loja.db")


def criar_tabela_produtos():
    conn = conectar_banco()
    cursor = conn.cursor()
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS produtos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            preco REAL NOT NULL
        )
        """
    )


def inserir_produto(nome, preco):
    conn = conectar_banco()
    cursor = conn.cursor()
    cursor.execute(
        """
        INSERT INTO produtos (nome, preco)
        VALUES (?, ?)
        """,
        (nome, preco),
    )
    conn.commit()


def listar_produtos():
    conn = conectar_banco()
    cursor = conn.cursor()
    cursor.execute(
        """
        SELECT * FROM produtos
        """
    )
    produtos = cursor.fetchall()
    for produto in produtos:
        print(produto)
