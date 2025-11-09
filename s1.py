from faker import Faker
import random
import requests
import time
import tkinter as tk
from tkinter import ttk, messagebox

fake = Faker('pt_BR')

clubes = [
    "Flamengo", "Palmeiras", "Corinthians", "São Paulo", "Grêmio",
    "Internacional", "Vasco", "Cruzeiro", "Botafogo", "Fluminense"
]

posicoes = ["Goleiro", "Zagueiro", "Lateral", "Meio-Campista", "Atacante"]

NUM_JOGADORES = 10

def gerar_atributos_por_posicao(posicao: str):
    """Gera atributos coerentes com a posição do jogador."""
    if posicao == "Goleiro":
        return {
            "ataque": random.randint(1, 30),
            "defesa": random.randint(70, 99),
            "fisico": random.randint(60, 90)
        }

    elif posicao == "Zagueiro":
        return {
            "ataque": random.randint(20, 50),
            "defesa": random.randint(70, 99),
            "fisico": random.randint(60, 95)
        }

    elif posicao == "Lateral":
        return {
            "ataque": random.randint(50, 80),
            "defesa": random.randint(50, 80),
            "fisico": random.randint(60, 90)
        }

    elif posicao == "Meio-Campista":
        return {
            "ataque": random.randint(50, 85),
            "defesa": random.randint(40, 80),
            "fisico": random.randint(60, 90)
        }

    elif posicao == "Atacante":
        return {
            "ataque": random.randint(75, 99),
            "defesa": random.randint(20, 50),
            "fisico": random.randint(60, 95)
        }

    else:
        return {
            "ataque": random.randint(40, 90),
            "defesa": random.randint(40, 90),
            "fisico": random.randint(40, 90)
        }


def gerar_estatisticas_por_posicao(posicao: str):
    # """Gera estatísticas coerentes com a posição do jogador."""
    partidas = random.randint(10, 200)

    if posicao == "Goleiro":
        gols = random.randint(0, 3)
        assistencias = random.randint(0, 5)
    elif posicao == "Zagueiro":
        gols = random.randint(0, 10)
        assistencias = random.randint(0, 10)
    elif posicao == "Lateral":
        gols = random.randint(1, 10)
        assistencias = random.randint(5, 20)
    elif posicao == "Meio-Campista":
        gols = random.randint(5, 20)
        assistencias = random.randint(5, 25)
    elif posicao == "Atacante":
        gols = random.randint(10, 40)
        assistencias = random.randint(5, 20)
    else:
        gols = random.randint(0, 10)
        assistencias = random.randint(0, 10)

    return {
        "partidas": partidas,
        "gols": gols,
        "assistencias": assistencias
    }


for i in range(NUM_JOGADORES):
    print(f"\n Gerando Jogador {i + 1}/{NUM_JOGADORES}")

    nome = fake.name_male()
    posicao = random.choice(posicoes)
    clube = random.choice(clubes)

    try:
        res_jog = requests.post(
            "http://127.0.0.1:8000/add_jogador",
            json={"nome": nome, "posicao": posicao, "clube": clube},
            timeout=5
        )
        res_jog.raise_for_status()
        jogador_id = res_jog.json().get("id")
        print(f" Jogador cadastrado: {nome} ({posicao}, {clube}) [ID {jogador_id}]")
    except Exception as e:
        print(" Erro ao cadastrar jogador:", e)
        continue

    atributos = gerar_atributos_por_posicao(posicao)

    try:
        res_attr = requests.post(
            "http://127.0.0.1:8000/add_atributo",
            json={"jogador_id": jogador_id, **atributos},
            timeout=5
        )
        res_attr.raise_for_status()
        print(f" Atributos -> Ataque: {atributos['ataque']} | "
              f"Defesa: {atributos['defesa']} | Físico: {atributos['fisico']}")
    except Exception as e:
        print("")

    stats = gerar_estatisticas_por_posicao(posicao)

    #Neo4j
    try:
        res_est = requests.post(
            "http://127.0.0.1:8000/add_estatistica",
            json={"jogador_id": jogador_id, **stats},
            timeout=5
        )
        res_est.raise_for_status()
        print(f" Estatísticas -> {stats['partidas']} jogos, "
              f"{stats['gols']} gols, {stats['assistencias']} assistências")
    except Exception as e:
        print(" Erro ao cadastrar estatísticas:", e)

    time.sleep(0.5)

print("\n Cadastro automático concluído com sucesso!")

# -------------------------------------- buscar jogadores ---------------------------

def buscar_jogadores():
    nome = entry_nome.get().strip()
    posicao = combo_posicao.get()
    clube = combo_clube.get()

    try:
        res = requests.get(
            "http://127.0.0.1:8000/buscar_jogadores",
            params={"nome": nome, "posicao": posicao, "clube": clube},
            timeout=5
        )
        res.raise_for_status()
        data = res.json().get("jogadores", [])

        for item in tree.get_children():
            tree.delete(item)

        if not data:
            messagebox.showinfo("Resultado", "Nenhum jogador encontrado.")
            return

        for jog in data:
            tree.insert("", "end", values=(jog["id"], jog["nome"], jog["posicao"], jog["clube"]))

    except Exception as e:
        messagebox.showerror("Erro", f"Não foi possível buscar jogadores.\n{e}")


# -------------------------------------- tk inter -----------------------------------

root = tk.Tk()
root.title("Busca de Jogadores")
root.geometry("750x500")
root.configure(bg="#1a1a1a")

titulo = tk.Label(root, text="Buscar Jogadores", font=("Segoe UI", 18, "bold"), bg="#1a1a1a", fg="white")
titulo.pack(pady=10)

frame_filtros = tk.Frame(root, bg="#1a1a1a")
frame_filtros.pack(pady=5)

tk.Label(frame_filtros, text="Nome:", bg="#1a1a1a", fg="white").grid(row=0, column=0, padx=5)
entry_nome = tk.Entry(frame_filtros, width=25)
entry_nome.grid(row=0, column=1, padx=5)

tk.Label(frame_filtros, text="Posição:", bg="#1a1a1a", fg="white").grid(row=0, column=2, padx=5)
combo_posicao = ttk.Combobox(frame_filtros, values=["Qualquer", "Goleiro", "Zagueiro", "Lateral", "Meio-Campista", "Atacante"], width=20)
combo_posicao.current(0)
combo_posicao.grid(row=0, column=3, padx=5)

tk.Label(frame_filtros, text="Clube:", bg="#1a1a1a", fg="white").grid(row=0, column=4, padx=5)
combo_clube = ttk.Combobox(frame_filtros, values=[
    "Qualquer", "Flamengo", "Palmeiras", "Corinthians", "São Paulo", "Grêmio",
    "Internacional", "Vasco", "Cruzeiro", "Botafogo", "Fluminense"
], width=20)
combo_clube.current(0)
combo_clube.grid(row=0, column=5, padx=5)

btn_buscar = tk.Button(root, text="Buscar", command=buscar_jogadores, bg="#2e8b57", fg="white", font=("Segoe UI", 11, "bold"))
btn_buscar.pack(pady=10)

cols = ("ID", "Nome", "Posição", "Clube")
tree = ttk.Treeview(root, columns=cols, show="headings", height=12)
for col in cols:
    tree.heading(col, text=col)
    tree.column(col, anchor="center", width=150)
tree.pack(padx=10, pady=10, fill="both", expand=True)

root.mainloop()