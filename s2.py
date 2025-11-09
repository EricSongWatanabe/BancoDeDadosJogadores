from fastapi import FastAPI
from pydantic import BaseModel
from pymongo import MongoClient
import psycopg2
from neo4j import GraphDatabase

# Conexão PostgreSQL
pg_conn = psycopg2.connect(
    dbname="postgres",
    user="postgres",
    password="fei",
    host="localhost",
    port="5432"
)
pg_cur = pg_conn.cursor()

# Conexão MongoDB
client = MongoClient("mongodb+srv://EricSongWatanabe:ut8mbh7v@eric.6x0uuaj.mongodb.net/?retryWrites=true&w=majority")
db = client["cc6240-2"]
colecao = db["projeto"]

app = FastAPI()

class Jogador(BaseModel):
    nome: str
    posicao: str
    clube: str

class Atributos(BaseModel):
    jogador_id: int
    ataque: int
    fisico: int
    defesa: int

class Estatisticas(BaseModel):
    jogador_id: int
    partidas: int
    gols: int
    assistencias: int

#Neo4j
NEO4J_URI = "neo4j+ssc://3e5fd840.databases.neo4j.io" 
NEO4J_USER = "neo4j"
NEO4J_PASSWORD = "OGTOWKzctXGFhFxRMQ8PMwcegd49eo-yox-H4uOnGBU"

driver = GraphDatabase.driver(NEO4J_URI, auth=(NEO4J_USER, NEO4J_PASSWORD))

#PostgreSQL
@app.post("/add_jogador")
def add_jogador(jog: Jogador):
    pg_cur.execute(
        "INSERT INTO jogador (nome, posicao, clube) VALUES (%s, %s, %s) RETURNING id;",
        (jog.nome, jog.posicao, jog.clube)
    )
    jogador_id = pg_cur.fetchone()[0]
    pg_conn.commit()
    return {"msg": "Jogador salvo com sucesso!", "id": jogador_id, "nome": jog.nome}

#MongoDB
@app.post("/add_atributo")
def add_atributo(item: Atributos):
    doc = {
        "jogador_id": item.jogador_id,
        "ataque": item.ataque,
        "fisico": item.fisico,
        "defesa": item.defesa
    }
    colecao.insert_one(doc)
    return {"msg": "Atributos salvos com sucesso!", **doc}

#Neo4j
@app.post("/add_estatistica")
def add_estatistica(est: Estatisticas):
    query = """
    MERGE (j:Jogador {jogador_id: $jogador_id})
    SET j.partidas = $partidas,
        j.gols = $gols,
        j.assistencias = $assistencias
    RETURN j
    """
    try:
        with driver.session() as session:
            session.run(query, est.dict())
        return {"msg": "Estatísticas salvas com sucesso!", **est.dict()}
    except Exception as e:
        return {"error": str(e)}


@app.get("/buscar_jogadores")
def buscar_jogadores(nome: str = None, posicao: str = None, clube: str = None):
    query = "SELECT id, nome, posicao, clube FROM jogador WHERE 1=1"
    params = []

    if nome:
        query += " AND nome ILIKE %s"
        params.append(f"%{nome}%")
    if posicao and posicao != "Qualquer":
        query += " AND posicao = %s"
        params.append(posicao)
    if clube and clube != "Qualquer":
        query += " AND clube = %s"
        params.append(clube)

    pg_cur.execute(query, params)
    resultados = pg_cur.fetchall()

    jogadores = [
        {"id": r[0], "nome": r[1], "posicao": r[2], "clube": r[3]} for r in resultados
    ]

    return {"jogadores": jogadores}