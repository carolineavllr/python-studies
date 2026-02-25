# Crie um programa que grave em um arquivo alunos.csv uma lista de alunos e suas notas.
# Leia o arquivo alunos.csv e imprima apenas os alunos com nota maior ou igual a 7.0.

import csv
# Gravar alunos e notas no arquivo CSV
alunos = [
    {"nome": "Alice", "nota": 8.5},
    {"nome": "Bob", "nota": 6.0},
    {"nome": "Charlie", "nota": 7.5},
    {"nome": "David", "nota": 5.0},
    {"nome": "Eve", "nota": 9.0}
]

with open("gravacao-manipulacao-arquivos/alunos.csv", "w", newline="") as arquivo:
    escritor_csv = csv.DictWriter(arquivo, fieldnames=["nome", "nota"])
    escritor_csv.writeheader()
    for aluno in alunos:
        escritor_csv.writerow(aluno)

# Ler o arquivo alunos.csv e imprimir apenas os alunos com nota maior ou igual a 7.0
with open("gravacao-manipulacao-arquivos/alunos.csv", "r") as arquivo:
    leitor_csv = csv.DictReader(arquivo)
    for linha in leitor_csv:
        if float(linha["nota"]) >= 7.0:
            print(f"Aluno: {linha['nome']}, Nota: {linha['nota']}")