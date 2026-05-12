'''
*---------------------------------------------------------*
*              Fatec São Caetano do Sul                   *
* Autor: 1681432612006                                    *
* Objetivo: programa em Python que implemente uma Árvore  *
*Binária de Busca (BST)                                   *
* Data: 12/05/2026                                        *
*---------------------------------------------------------*
'''

class No:
    def __init__(self, valor):
        self.valor = valor
        self.esq = None
        self.dir = None


class ArvoreBST:
    def __init__(self, raiz=None):
        self.raiz = raiz

    def inserir(self, valor):
        if self.raiz == None:
            self.raiz = No(valor)
        else:
            self.inserir_recursivo(self.raiz, valor)

    def inserir_recursivo(self, no_atual, valor):
        if valor < no_atual.valor:
            if no_atual.esq == None:
                no_atual.esq = No(valor)
            else:
                self.inserir_recursivo(no_atual.esq, valor)
        elif valor > no_atual.valor:
            if no_atual.dir == None:
                no_atual.dir = No(valor)
            else:
                self.inserir_recursivo(no_atual.dir, valor)

    def imprimir_nos_internos(self):
        lista_internos = []
        self.pegar_internos(self.raiz, lista_internos)
        print("Nos internos:", lista_internos)

    def pegar_internos(self, no, lista):
        if no == None:
            return
        if no.esq != None or no.dir != None:
            lista.append(no.valor)
        self.pegar_internos(no.esq, lista)
        self.pegar_internos(no.dir, lista)

    def imprimir_folhas(self):
        lista_folhas = []
        self.pegar_folhas(self.raiz, lista_folhas)
        print("Nos folhas:", lista_folhas)

    def pegar_folhas(self, no, lista):
        if no == None:
            return
        if no.esq == None and no.dir == None:
            lista.append(no.valor)
        self.pegar_folhas(no.esq, lista)
        self.pegar_folhas(no.dir, lista)

    def imprimir_niveis(self):
        if self.raiz == None:
            print("Arvore vazia")
            return

        fila = []
        fila.append((self.raiz, 0))
        nivel_atual = 0
        nos_do_nivel = []

        while len(fila) > 0:
            no, nivel = fila.pop(0)

            if nivel != nivel_atual:
                print("Nivel", nivel_atual, ":", nos_do_nivel)
                nos_do_nivel = []
                nivel_atual = nivel

            nos_do_nivel.append(no.valor)

            if no.esq != None:
                fila.append((no.esq, nivel + 1))
            if no.dir != None:
                fila.append((no.dir, nivel + 1))

        print("Nivel", nivel_atual, ":", nos_do_nivel)

    def calcular_altura(self, no):
        if no == None:
            return -1
        altura_esq = self.calcular_altura(no.esq)
        altura_dir = self.calcular_altura(no.dir)
        if altura_esq > altura_dir:
            return 1 + altura_esq
        else:
            return 1 + altura_dir

    def calcular_profundidade(self, valor):
        profundidade = 0
        no_atual = self.raiz
        while no_atual != None:
            if valor == no_atual.valor:
                return profundidade
            elif valor < no_atual.valor:
                no_atual = no_atual.esq
            else:
                no_atual = no_atual.dir
            profundidade = profundidade + 1
        return -1

    def imprimir_ancestrais(self, valor):
        lista_ancestrais = []
        self.pegar_ancestrais(self.raiz, valor, lista_ancestrais)
        print("Ancestrais de", valor, ":", lista_ancestrais)

    def pegar_ancestrais(self, no, valor, lista):
        if no == None:
            return False
        if no.valor == valor:
            return True
        achou_esq = self.pegar_ancestrais(no.esq, valor, lista)
        achou_dir = self.pegar_ancestrais(no.dir, valor, lista)
        if achou_esq == True or achou_dir == True:
            lista.append(no.valor)
            return True
        return False

    def imprimir_descendentes(self, valor):
        no_alvo = self.buscar_no(self.raiz, valor)
        lista_descendentes = []
        if no_alvo != None:
            self.pegar_descendentes(no_alvo.esq, lista_descendentes)
            self.pegar_descendentes(no_alvo.dir, lista_descendentes)
        print("Descendentes de", valor, ":", lista_descendentes)

    def pegar_descendentes(self, no, lista):
        if no == None:
            return
        lista.append(no.valor)
        self.pegar_descendentes(no.esq, lista)
        self.pegar_descendentes(no.dir, lista)

    def buscar_no(self, no, valor):
        if no == None:
            return None
        if no.valor == valor:
            return no
        if valor < no.valor:
            return self.buscar_no(no.esq, valor)
        else:
            return self.buscar_no(no.dir, valor)

    def analisar_arvore(self, valor_busca):
        print("======================================")
        print("     DIAGNOSTICO GERAL DA ARVORE")
        print("======================================")

        if self.raiz == None:
            print("Arvore vazia!")
            return

        print("Raiz:", self.raiz.valor)
        print("ID da raiz:", id(self.raiz))
        print("")

        print("Nos internos:")
        self.imprimir_nos_internos()
        print("")

        print("Nos folhas:")
        self.imprimir_folhas()
        print("")

        print("Niveis da arvore:")
        self.imprimir_niveis()
        print("")

        print("======================================")
        print("  DIAGNOSTICO DO NO:", valor_busca)
        print("======================================")

        no_encontrado = self.buscar_no(self.raiz, valor_busca)

        if no_encontrado == None:
            print("No", valor_busca, "nao encontrado!")
            return

        print("No encontrado:", no_encontrado.valor)
        print("ID do no:", id(no_encontrado))
        print("")

        grau = 0
        if no_encontrado.esq != None:
            grau = grau + 1
        if no_encontrado.dir != None:
            grau = grau + 1
        print("Grau do no:", grau)

        if no_encontrado.esq != None:
            print("Filho esquerdo:", no_encontrado.esq.valor)
        if no_encontrado.dir != None:
            print("Filho direito:", no_encontrado.dir.valor)
        print("")

        print("Ancestrais:")
        self.imprimir_ancestrais(valor_busca)
        print("")

        print("Descendentes:")
        self.imprimir_descendentes(valor_busca)
        print("")

        altura = self.calcular_altura(no_encontrado)
        profundidade = self.calcular_profundidade(valor_busca)
        print("Altura do no:", altura)
        print("Profundidade do no:", profundidade)
        print("======================================")

    def tabela_nos(self):
        if self.raiz == None:
            return []

        resultado = []
        fila = []
        fila.append((self.raiz, 0))

        while len(fila) > 0:
            no, nivel = fila.pop(0)

            grau = 0
            if no.esq != None:
                grau = grau + 1
            if no.dir != None:
                grau = grau + 1

            if nivel == 0:
                tipo = "Raiz"
            elif grau == 0:
                tipo = "Folha"
            else:
                tipo = "Interno"

            ancestrais = []
            self.pegar_ancestrais(self.raiz, no.valor, ancestrais)

            linha = {
                "valor": no.valor,
                "nivel": nivel,
                "grau": grau,
                "ancestrais": ancestrais,
                "id": hex(id(no)),
                "tipo": tipo
            }
            resultado.append(linha)

            if no.esq != None:
                fila.append((no.esq, nivel + 1))
            if no.dir != None:
                fila.append((no.dir, nivel + 1))

        return resultado