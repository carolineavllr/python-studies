filmesFavoritos = ["O Poderoso Chefão", "O Senhor dos Anéis", "Pulp Fiction", "Forrest Gump"]

datas = 1990, 1994, 1995, 1999

filmesEData = {}

for i in range(len(filmesFavoritos)):
    filmesEData[filmesFavoritos[i]] = datas[i]
    
print(filmesEData)
