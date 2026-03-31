'''
*---------------------------------------------------------*
*              Fatec São Caetano do Sul                   *
*         Exemplo de Manipulação de Lista Ligada          *
* Autor: Eduardo Sim                                      *
* Objetivo: Mostrar manipulação de lista ligada em python *
* Data: 09/03/2026                                        *
*---------------------------------------------------------*
'''

# Banco de dados em memória (Dicionário)
produtos = {}


def valorExiste(listaCabeca, valorEntrada):
    atual = listaCabeca
    while atual is not None:
        if atual["valor"] == valorEntrada:
            return True
        atual = atual["proximo"]
    return False


# Função de Inclusão no Início
def inserirInicio(listaEntrada):
    valor = input("Digite o valor: ")
    if valorExiste(listaEntrada, valor):
        print("Codigo de produto Duplicado")
        return listaEntrada
    novoNo = {"valor": valor, "proximo": listaEntrada}
    return novoNo


# Função de Inclusão no Meio
def inserirMeio(listaEntrada):
    if listaEntrada is None:
        print("Lista vazia. Insira pelo menos um elemento antes.")
        return listaEntrada

    valor = input("Digite o valor a inserir: ")
    if valorExiste(listaEntrada, valor):
        print("Codigo de produto Duplicado")
        return listaEntrada

    posicao = int(input("Digite a posição para inserir (a partir de 1): "))
    if posicao <= 1:
        novoNo = {"valor": valor, "proximo": listaEntrada}
        return novoNo

    atual = listaEntrada
    contador = 1
    while atual["proximo"] is not None and contador < posicao - 1:
        atual = atual["proximo"]
        contador += 1

    novoNo = {"valor": valor, "proximo": atual["proximo"]}
    atual["proximo"] = novoNo

    return listaEntrada


# Função de Inclusão no Fim
def inserirFim(listaEntrada):
    valor = input("Digite o valor: ")
    if valorExiste(listaEntrada, valor):
        print("Codigo de produto Duplicado")
        return listaEntrada

    novoNo = {"valor": valor, "proximo": None}
    if listaEntrada is None:
        return novoNo

    atual = listaEntrada
    while atual["proximo"] is not None:
        atual = atual["proximo"]
    atual["proximo"] = novoNo

    return listaEntrada


# Função de Listagem
def listar(listaRecebida):
    if listaRecebida is None:
        print("Lista vazia")
        return
    listaAtual = listaRecebida
    while listaAtual is not None:
        print(listaAtual["valor"], end=" -> ")
        listaAtual = listaAtual["proximo"]
    print()

# funcao de Exclusao
def remover(listaEntrada):
    if listaEntrada is None:
        print("Lista vazia")
        return listaEntrada

    valor = input("Digite o valor a remover: ")

    if listaEntrada["valor"] == valor:
        print(f"Valor '{valor}' removido com sucesso")
        return listaEntrada["proximo"]

    atual = listaEntrada
    while atual["proximo"] is not None:
        if atual["proximo"]["valor"] == valor:
            atual["proximo"] = atual["proximo"]["proximo"]
            print(f"Valor '{valor}' removido com sucesso")
            return listaEntrada
        atual = atual["proximo"]

    print("Valor não encontrado")
    return listaEntrada

# Função de Busca
def buscar(listaRecebida):
    argumentoPesquisa = input("Informe o argumento de pesquisa: ")
    listaAtual = listaRecebida
    posicao = 0
    while listaAtual is not None:
        posicao += 1
        if listaAtual["valor"] == argumentoPesquisa:
            print(f"Valor encontrado na posição {posicao}")
            return
        listaAtual = listaAtual["proximo"]
    print("Valor não encontrado")

# Menu de Interação
def menu():
    lista = None
    while True:
        print("\n1 - Inserir no Início")
        print("2 - Inserir no Meio")
        print("3 - Inserir no Fim")
        print("4 - Listar")
        print("5 - Remover")
        print("6 - Buscar")
        print("0 - Sair")

        opcao = input("\nEscolha uma operacao: ")

        if opcao == '1':
            lista = inserirInicio(lista)
        elif opcao == '2':
            lista = inserirMeio(lista)
        elif opcao == '3':
            lista = inserirFim(lista)
        elif opcao == '4':
            listar(lista)
        elif opcao == '5':
            lista = remover(lista)
        elif opcao == '6':
            buscar(lista)
        elif opcao == '0':
            print("Obrigado por usar o sistema")
            break
        else:
            print("** Opção inválida **")


print("** Bem-vindo ao programa **")
menu()