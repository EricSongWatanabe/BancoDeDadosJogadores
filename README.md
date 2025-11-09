#  BancoDeDadosJogadores

##  Integrantes do Grupo

- **Eric Song Watanabe** — RA: 22.125.086-3  
- **Victor Pimentel Lario** — RA: 22.125.064-0

---

##  Descrição do Projeto

Este projeto tem como objetivo **integrar três diferentes bancos de dados** (PostgreSQL, MongoDB e Neo4j) para armazenar informações de jogadores de futebol, além de disponibilizar uma **interface gráfica (Tkinter)** para consulta dos dados.

O sistema é dividido em duas principais partes:

1. **`s2.py`** → API desenvolvida com **FastAPI**, responsável por receber, armazenar e consultar dados nos três bancos.
2. **`s1.py`** → Script principal que gera jogadores com dados coerentes (utilizando a biblioteca **Faker**) e envia as informações para os bancos através da API.  
   Também contém a **interface Tkinter** para buscar e visualizar os jogadores cadastrados.

---

##  Passo a Passo para Executar o Projeto

### 1. Instalar Dependências
pip install fastapi uvicorn pymongo pydantic requests psycopg2 neo4j faker tkinter


### 2. Configurar Banco de Dados
PostgreSQL:
- Crie um database com nome postgres
- Crie a tabela jogadores com as colunas:
   CREATE TABLE jogadores (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(100),
    clube VARCHAR(100),
    posicao VARCHAR(50)
);
- Faça as açterações necessárias no código (alterar link do database, etc.).

MongoDB:
- Tenha o servidor MongoDB rodando localmente ou em nuvem.
- Crie uma coleção chamada atributos.
- Faça as alterações necessárias no código (alterar o db, user, etc.).


Neo4j:
- Tenha o Neo4j Desktop ou Aura ativo.
- Verifique as credenciais (URI, USER, PASSWORD)
- Faça as alterações necessárias no código.


### 3. Explicação do Tema Escolhido
Escolhemos o tema pois o grupo ja tinha usado o mesmo tema no semestre passado em outros projetos, além dos integrantes adorarem o jogo FIFA, oque motivou ainda mais para seguir com a escolha.


### 4. Justificativa para Cada Banco Usado

PostgreSQL:
Escolhido para armazenar dados estruturados e relacionais, garantindo integridade e consistência. É ideal para informações fixas e com dependências claras entre si.

MongoDB:
Selecionado para armazenar dados semiestruturados e flexíveis, como estatísticas dos jogadores, que podem variar em tipo e quantidade sem a necessidade de alterar o esquema.

Neo4j:
Adotado por sua capacidade de representar relações complexas entre entidades. Permite consultas eficientes sobre conexões, como jogadores que atuaram juntos ou que pertencem ao mesmo clube
