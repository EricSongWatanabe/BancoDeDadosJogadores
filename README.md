# BancoDeDadosJogadores

# 🗃️ Projeto de Integração de Bancos de Dados com Interface Tkinter

## 👥 Integrantes do Grupo

- **Eric Song Watanabe** — RA: 22.125.086-3  
- **Victor Pimentel Lario** — RA: 22.125.064-0

---

## 📖 Descrição do Projeto

Este projeto tem como objetivo **integrar três diferentes bancos de dados** (PostgreSQL, MongoDB e Neo4j) para armazenar informações de jogadores de futebol, além de disponibilizar uma **interface gráfica (Tkinter)** para consulta dos dados.

O sistema é dividido em duas principais partes:

1. **`s2.py`** → API desenvolvida com **FastAPI**, responsável por receber, armazenar e consultar dados nos três bancos.
2. **`s1.py`** → Script principal que gera jogadores com dados coerentes (utilizando a biblioteca **Faker**) e envia as informações para os bancos através da API.  
   Também contém a **interface Tkinter** para buscar e visualizar os jogadores cadastrados.
