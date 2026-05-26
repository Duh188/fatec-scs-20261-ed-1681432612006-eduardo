'''
*---------------------------------------------------------*
*              Fatec São Caetano do Sul                   *
* Autor: 1681432612006                                    *
* Objetivo:Consolidar a compreensão do mecanismo de Fator *
* de Balanceamento (FB) em Árvores AVL                    *
* Data: 25/05/2026                                        *
*---------------------------------------------------------*
'''
class No:
    def __init__(self, valor):
        self.valor = valor
        self.esq = None
        self.dir = None
        self.altura = 0


def altura(no):
    if no is None:
        return -1
    return no.altura


def calcular_altura(no):
    return 1 + max(altura(no.esq), altura(no.dir))


def fator_balanceamento(no):
    return altura(no.esq) - altura(no.dir)


def rotacao_direita(y):
    x = y.esq
    T2 = x.dir
    x.dir = y
    y.esq = T2
    y.altura = calcular_altura(y)
    x.altura = calcular_altura(x)
    return x


def rotacao_esquerda(x):
    y = x.dir
    T2 = y.esq
    y.esq = x
    x.dir = T2
    x.altura = calcular_altura(x)
    y.altura = calcular_altura(y)
    return y


def imprimir_arvore_str(raiz, nivel=0, prefixo="Raiz: "):
    linhas = []
    if raiz is not None:
        fb = fator_balanceamento(raiz)
        linhas.append(" " * (nivel * 4) + prefixo + f"{raiz.valor} (FB={fb:+d}, H={raiz.altura})")
        if raiz.esq or raiz.dir:
            if raiz.esq:
                linhas.append(imprimir_arvore_str(raiz.esq, nivel + 1, "Esq: "))
            else:
                linhas.append(" " * ((nivel + 1) * 4) + "Esq: NULL")
            if raiz.dir:
                linhas.append(imprimir_arvore_str(raiz.dir, nivel + 1, "Dir: "))
            else:
                linhas.append(" " * ((nivel + 1) * 4) + "Dir: NULL")
    return "\n".join(linhas)


def imprimir_todos_fbs(raiz, linhas=None):
    if linhas is None:
        linhas = []
    if raiz:
        linhas.append(f"  No {raiz.valor}: H={raiz.altura}, FB={fator_balanceamento(raiz):+d}")
        imprimir_todos_fbs(raiz.esq, linhas)
        imprimir_todos_fbs(raiz.dir, linhas)
    return linhas


def fbs_pos_rotacao(raiz, log):
    log.append(f"\n  FBs apos rotacao:")
    for linha in imprimir_todos_fbs(raiz):
        log.append(linha)


def inserir(raiz, valor, log):
    if raiz is None:
        novo = No(valor)
        novo.altura = 0
        log.append(f"\nINCLUSAO DO NO {valor} (folha)")
        log.append(f"  PASSO 1 - ALTURA H({valor})")
        log.append(f"  h(filho_esq) = -1")
        log.append(f"  h(filho_dir) = -1")
        log.append(f"  H({valor}) = 1 + max(-1, -1) = 0")
        log.append(f"  PASSO 2 - FB({valor})")
        log.append(f"  h(subarv_esq) = -1")
        log.append(f"  h(subarv_dir) = -1")
        log.append(f"  FB({valor}) = -1 - (-1) = 0  -> Balanceado")
        return novo

    if valor < raiz.valor:
        raiz.esq = inserir(raiz.esq, valor, log)
    elif valor > raiz.valor:
        raiz.dir = inserir(raiz.dir, valor, log)
    else:
        return raiz

    raiz.altura = calcular_altura(raiz)
    fb = fator_balanceamento(raiz)

    log.append(f"\n  Recalculando no {raiz.valor}:")
    log.append(f"  PASSO 1 - ALTURA H({raiz.valor})")
    log.append(f"  h(filho_esq) = {altura(raiz.esq)}")
    log.append(f"  h(filho_dir) = {altura(raiz.dir)}")
    log.append(f"  H({raiz.valor}) = 1 + max({altura(raiz.esq)}, {altura(raiz.dir)}) = {raiz.altura}")
    log.append(f"  PASSO 2 - FB({raiz.valor})")
    log.append(f"  h(subarv_esq) = {altura(raiz.esq)}")
    log.append(f"  h(subarv_dir) = {altura(raiz.dir)}")

    if -1 <= fb <= 1:
        log.append(f"  FB({raiz.valor}) = {altura(raiz.esq)} - ({altura(raiz.dir)}) = {fb}  -> Balanceado")
    else:
        log.append(f"  FB({raiz.valor}) = {altura(raiz.esq)} - ({altura(raiz.dir)}) = {fb}  -> DESEQUILIBRIO")

    if fb == 2 and fator_balanceamento(raiz.esq) >= 0:
        log.append(f"\n  NO CRITICO: {raiz.valor} (FB=+2)")
        log.append(f"  FB(filho esq {raiz.esq.valor}) = {fator_balanceamento(raiz.esq)}")
        log.append(f"  CASO LL -> Rotacao Simples a Direita no no {raiz.valor}")
        log.append(f"\n  ANTES DA ROTACAO:")
        log.append(imprimir_arvore_str(raiz))
        raiz = rotacao_direita(raiz)
        log.append(f"\n  DEPOIS DA ROTACAO:")
        log.append(imprimir_arvore_str(raiz))
        fbs_pos_rotacao(raiz, log)

    elif fb == -2 and fator_balanceamento(raiz.dir) <= 0:
        log.append(f"\n  NO CRITICO: {raiz.valor} (FB=-2)")
        log.append(f"  FB(filho dir {raiz.dir.valor}) = {fator_balanceamento(raiz.dir)}")
        log.append(f"  CASO RR -> Rotacao Simples a Esquerda no no {raiz.valor}")
        log.append(f"\n  ANTES DA ROTACAO:")
        log.append(imprimir_arvore_str(raiz))
        raiz = rotacao_esquerda(raiz)
        log.append(f"\n  DEPOIS DA ROTACAO:")
        log.append(imprimir_arvore_str(raiz))
        fbs_pos_rotacao(raiz, log)

    elif fb == 2 and fator_balanceamento(raiz.esq) < 0:
        log.append(f"\n  NO CRITICO: {raiz.valor} (FB=+2)")
        log.append(f"  FB(filho esq {raiz.esq.valor}) = {fator_balanceamento(raiz.esq)}")
        log.append(f"  CASO LR -> Rotacao Dupla")
        log.append(f"\n  ANTES DAS ROTACOES (zig-zag):")
        log.append(imprimir_arvore_str(raiz))
        log.append(f"\n  Passo 1: Rotacao a Esquerda no filho {raiz.esq.valor}")
        raiz.esq = rotacao_esquerda(raiz.esq)
        log.append(f"\n  ESTADO INTERMEDIARIO:")
        log.append(imprimir_arvore_str(raiz))
        log.append(f"\n  Passo 2: Rotacao a Direita no pai {raiz.valor}")
        raiz = rotacao_direita(raiz)
        log.append(f"\n  DEPOIS DA ROTACAO DUPLA LR:")
        log.append(imprimir_arvore_str(raiz))
        fbs_pos_rotacao(raiz, log)

    elif fb == -2 and fator_balanceamento(raiz.dir) > 0:
        log.append(f"\n  NO CRITICO: {raiz.valor} (FB=-2)")
        log.append(f"  FB(filho dir {raiz.dir.valor}) = {fator_balanceamento(raiz.dir)}")
        log.append(f"  CASO RL -> Rotacao Dupla")
        log.append(f"\n  ANTES DAS ROTACOES (zig-zag reverso):")
        log.append(imprimir_arvore_str(raiz))
        log.append(f"\n  Passo 1: Rotacao a Direita no filho {raiz.dir.valor}")
        raiz.dir = rotacao_direita(raiz.dir)
        log.append(f"\n  ESTADO INTERMEDIARIO:")
        log.append(imprimir_arvore_str(raiz))
        log.append(f"\n  Passo 2: Rotacao a Esquerda no pai {raiz.valor}")
        raiz = rotacao_esquerda(raiz)
        log.append(f"\n  DEPOIS DA ROTACAO DUPLA RL:")
        log.append(imprimir_arvore_str(raiz))
        fbs_pos_rotacao(raiz, log)

    return raiz


def processar_rede(numero, titulo, sequencia):
    print(f"\nREDE {numero:02d} - {titulo}")
    print(f"Sequencia: {' -> '.join(map(str, sequencia))}")
    print("-" * 50)

    raiz = None
    for valor in sequencia:
        log = []
        raiz = inserir(raiz, valor, log)
        for linha in log:
            print(linha)

    print(f"\nARVORE FINAL - REDE {numero:02d}")
    print(imprimir_arvore_str(raiz))
    print("\nFBs finais:")
    for linha in imprimir_todos_fbs(raiz):
        print(linha)


redes = [
    (1, "LL - Rotacao Simples a Direita",    [50, 30, 70, 20, 40, 10]),
    (2, "RR - Rotacao Simples a Esquerda",   [40, 20, 60, 50, 80, 90]),
    (3, "LR - Rotacao Dupla a Direita",      [60, 30, 80, 10, 45, 38]),
    (4, "RL - Rotacao Dupla a Esquerda",     [25, 15, 50, 35, 70, 30]),
    (5, "Multiplos Rebalanceamentos LL e RR",[100, 50, 150, 30, 75, 20, 40, 10]),
    (6, "Rede Mista LR e LL",               [55, 25, 75, 15, 40, 32, 48, 60]),
    (7, "Desafio - Todos os Tipos",          [70, 40, 90, 20, 55, 85, 100, 45, 60, 50]),
]

for numero, titulo, sequencia in redes:
    processar_rede(numero, titulo, sequencia)