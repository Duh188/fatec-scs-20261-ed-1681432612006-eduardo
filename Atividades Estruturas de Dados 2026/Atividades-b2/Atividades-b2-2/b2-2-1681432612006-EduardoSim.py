'''
*---------------------------------------------------------*
*              Fatec São Caetano do Sul                   *
* Autor: 1681432612006                                    *
* Objetivo:                                               *
* Data: 28/04/2026                                        *
*---------------------------------------------------------*
'''

fila_normal = []
fila_prioridade = []

fila_normal.append({"nome": "math_exam.pdf", "paginas": 3, "admin": 1})
fila_normal.append({"nome": "world_map_image.png", "paginas": 1, "admin": 0})
fila_normal.append({"nome": "english_text.pdf", "paginas": 23, "admin": 1})
fila_normal.append({"nome": "history_homework.pdf", "paginas": 2, "admin": 0})

while True:
    print("\n1- Solicitar impressão")
    print("2- Organizar fila")
    print("3- Imprimir")
    print("4- Mostrar filas")
    print("5- Contar arquivos")
    print("6- Sair")

    try:
        opcao = int(input("Escolha: "))
    except:
        print("Digite um número válido!")
        continue

    if opcao == 1:
        nome = input("Nome do arquivo: ")

        try:
            paginas = int(input("Número de páginas: "))
            admin = int(input("É admin? (1=sim, 0=não): "))
        except:
            print("Erro nos dados!")
            continue

        if paginas <= 0 or admin not in (0, 1):
            print("Dados inválidos!")
            continue

        fila_normal.append({"nome": nome, "paginas": paginas, "admin": admin})

    elif opcao == 2:
        print("Organizando...")

        fila_prioridade.clear()

        for item in fila_normal:
            if item["admin"] == 1:
                fila_prioridade.append(item)

        for item in fila_normal:
            if item["admin"] == 0:
                fila_prioridade.append(item)

    elif opcao == 3:
        if not fila_prioridade:
            print("Fila vazia!")
            continue

        item = fila_prioridade.pop(0)
        tipo = "admin" if item["admin"] else "aluno"

        print(f"Imprimindo {tipo}: {item['nome']} ({item['paginas']} páginas)")

    elif opcao == 4:
        print("\nFila normal:")
        if not fila_normal:
            print("Vazia")
        for item in fila_normal:
            tipo = "admin" if item["admin"] else "aluno"
            print(f"{tipo}: {item['nome']} ({item['paginas']} páginas)")

        print("\nFila organizada:")
        if not fila_prioridade:
            print("Vazia")
        for item in fila_prioridade:
            tipo = "admin" if item["admin"] else "aluno"
            print(f"{tipo}: {item['nome']} ({item['paginas']} páginas)")

    elif opcao == 5:
        admins = 0
        alunos = 0

        for item in fila_prioridade:
            if item["admin"] == 1:
                admins += 1
            else:
                alunos += 1

        print(f"Admins: {admins} | Alunos: {alunos}")

    elif opcao == 6:
        print("Saindo...")
        break

    else:
        print("Opção inválida!")

    print("=" * 40)