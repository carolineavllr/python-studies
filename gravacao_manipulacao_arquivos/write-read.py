# arquivo txt
with open ("gravacao-manipulacao-arquivos/arquivo.txt", "w") as arquivo:
    arquivo.write("Olá, mundo!\n")
    arquivo.write("Este é um arquivo de exemplo.\n")

with open ("gravacao-manipulacao-arquivos/arquivo.txt", "r") as arquivo:
    conteudo = arquivo.read()
    print(conteudo)



# arquivo csv
import csv

with open ("gravacao-manipulacao-arquivos/arquivo.csv", "w", newline="") as arquivo:
    escritor_csv = csv.writer(arquivo)
    escritor_csv.writerow(["Nome", "Idade", "Cidade"])
    escritor_csv.writerow(["Alice", 30, "São Paulo"])
    escritor_csv.writerow(["Bob", 25, "Rio de Janeiro"])

with open ("gravacao-manipulacao-arquivos/arquivo.csv", "r") as arquivo:
    leitor_csv = csv.reader(arquivo)
    for linha in leitor_csv:
        print(linha)



# arquivo json
import json

dados = {
    "nome": "Alice",
    "idade": 30,
    "cidade": "São Paulo",
    "hobbies": ["leitura", "viagem", "cozinha"]
}

with open ("gravacao-manipulacao-arquivos/arquivo.json", "w") as arquivo:
    json.dump(dados, arquivo, indent=4)

with open ("gravacao-manipulacao-arquivos/arquivo.json", "r") as arquivo:
    dados_carregados = json.load(arquivo)
    print(dados_carregados)