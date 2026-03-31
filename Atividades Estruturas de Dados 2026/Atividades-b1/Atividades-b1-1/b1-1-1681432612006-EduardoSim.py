"""
-------------------------------------
        FATEC ANTONIO RUSSO
            atividade 01(B1)
        autor: 1681432612006
  Objetivo: Utilizar estrutura de
     dados Dicionário em python
        data: 25/02/2026
-------------------------------------
"""
catalogo = {}


def adicionar_filme(id_para_adicionar, titulo, diretor):
    if catalogo.get(id_para_adicionar) is None:
        catalogo[id_para_adicionar] = {
            "titulo": titulo,
            "diretor": diretor
        }
        print(f"Filme '{titulo}' adicionado com sucesso!")
        return
    print(f"Já existe um filme com o ID: {id_para_adicionar}")


def buscar_filme(id_para_buscar):
    filme = catalogo.get(id_para_buscar)
    if filme is None:
        print(f"Não existe um filme com o ID: {id_para_buscar}")
        return None
    return filme


def remover_filme(id_para_remover):
    if id_para_remover not in catalogo:
        print(f"Não existe um filme com o ID: {id_para_remover}")
        return

    titulo = catalogo[id_para_remover]["titulo"]
    del catalogo[id_para_remover]
    print(f"O filme '{titulo}' foi deletado.")


def listar_todos():
    if not catalogo:
        print("O catalogo está vazio.")
    else:
        print("\n--- Listagem de Filmes ---")
        for id_atual, dados in catalogo.items():
            print(f"ID: {id_atual} | Título: {dados['titulo']} | Diretor: {dados['diretor']}")
        print("--------------------------\n")


id_do_filme = 1

adicionar_filme(id_do_filme, "As Branquelas", "Augusto Conti")
adicionar_filme(2, "O Poço", "Eduardo Sim")

listar_todos()

filme_encontrado = buscar_filme(id_do_filme)
if filme_encontrado:
    print(f"Filme encontrado: {filme_encontrado['titulo']}")

remover_filme(id_do_filme)

listar_todos()
