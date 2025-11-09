from neo4j import GraphDatabase
import os

# --- Lê as variáveis do ambiente (se estiverem num arquivo .env, falamos já sobre isso) ---
URI = os.getenv("NEO4J_URI", "neo4j+s://3e5fd840.databases.neo4j.io")
USER = os.getenv("NEO4J_USERNAME", "neo4j")
PASSWORD = os.getenv("NEO4J_PASSWORD", "OGTOWKzctXGFhFxRMQ8PMwcegd49eo-yox-H4uOnGBU")

# --- Cria a classe de conexão ---
class Neo4jConnection:
    def __init__(self, uri, user, password):
        self.driver = GraphDatabase.driver(uri, auth=(user, password))

    def close(self):
        self.driver.close()

    def execute_query(self, query, parameters=None):
        with self.driver.session() as session:
            result = session.run(query, parameters)
            return [r.data() for r in result]


if __name__ == "__main__":
    conn = Neo4jConnection(URI, USER, PASSWORD)
    print("✅ Conexão com Neo4j estabelecida com sucesso!")
    conn.close()
