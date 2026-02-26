nome = input("Digite seu nome: ")
idade = input("Digite sua idade: ")

with open ("gravacao-manipulacao-arquivos/info.txt", "w") as arquivo:
    arquivo.write(f"Nome: {nome}\n")
    arquivo.write(f"Idade: {idade}\n")