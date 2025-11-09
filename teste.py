from pymongo import MongoClient

# Conexão com o cluster do MongoDB Atlas (troque usuário, senha e cluster)
client = MongoClient("mongodb+srv://EricSongWatanabe:ut8mbh7v@eric.6x0uuaj.mongodb.net/?retryWrites=true&w=majority&appName=Eric")

# Escolher banco e coleção
db = client["cc6240-2"]
colecao = db["teste"]

# Inserir um documento
colecao.insert_one({"nome": "Eric", "idade": 20})

# Buscar todos documentos
for doc in colecao.find():
    print(doc)