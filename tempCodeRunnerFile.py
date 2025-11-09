
# @app.get("/buscar_jogadores")
# def buscar_jogadores(
#     nome: Optional[str] = Query(None),
#     posicao: Optional[str] = Query(None),
#     clube: Optional[str] = Query(None)
# ):
#     query = "SELECT id, nome, posicao, clube FROM jogador WHERE TRUE"
#     params = []

#     if nome:
#         query += " AND nome ILIKE %s"
#         params.append(f"%{nome}%")
#     if posicao:
#         query += " AND posicao = %s"
#         params.append(posicao)
#     if clube:
#         query += " AND clube = %s"
#         params.append(clube)

#     pg_cur.execute(query, params)
#     resultados = pg_cur.fetchall()

#     jogadores = [
#         {"id": r[0], "nome": r[1], "posicao": r[2], "clube": r[3]}
#         for r in resultados
#     ]

#     return jogadores