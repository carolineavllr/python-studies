from pymongo import MongoClient

# conecta ao mongo
client = MongoClient('mongodb://localhost:27017/')
db = client['exemplo_nao_relacional']

# criar coleção e inserir dados
usuarios = db['usuarios']
usuarios.insert_one({"nome": "Alice", "email": "alice@example.com"})
usuarios.insert_one({"nome": "Bob", "email": "bob@example.com"})
usuarios.insert_one({"nome": "Charlie", "email": "charlie@example.com"})

# ler os dados
for usuario in usuarios.find():
    print(usuario)