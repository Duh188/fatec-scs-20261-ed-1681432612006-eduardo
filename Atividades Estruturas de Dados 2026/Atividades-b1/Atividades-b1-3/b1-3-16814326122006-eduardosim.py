'''
*---------------------------------------------------------*
*              Fatec São Caetano do Sul                   *
*          Calculadora de notação polonesa reversa        *
*          (RPN/pós-fixa)                                 *
* Autor: Eduardo Sim                                      *
* Objetivo: Calcular utilizando notação polonesa reversa  *
* Data: 09/03/2026                                        *
*---------------------------------------------------------*
'''

X = 0.0
Y = 0.0
Z = 0.0
T = 0.0

def mostrar_pilha(acao):
    print(f"  {acao:<35} T={T:.2f}  Z={Z:.2f}  Y={Y:.2f}  X={X:.2f}")

def push(valor):
    global X, Y, Z, T
    T = Z
    Z = Y
    Y = X
    X = valor

def pop():
    global X, Y, Z, T
    valor = X
    X = Y
    Y = Z
    Z = T
    return valor

def validar_expressao(tokens):
    operadores = ["+", "-", "*", "/"]
    contador = 0

    if len(tokens) == 0:
        print("ERRO: A expressão está vazia")
        return False

    for token in tokens:
        if token in operadores:
            if contador < 2:
                print(f"ERRO: O operador '{token}' não tem operandos suficientes")
                return False
            contador = contador - 1
        else:
            try:
                float(token)
                contador = contador + 1
            except ValueError:
                print(f"ERRO: '{token}' não é um número nem um operador válido")
                return False

    if contador != 1:
        print(f"ERRO: A expressão ficou desequilibrada, sobraram {contador} valores.")
        return False

    return True

def converter_para_infixa(tokens):
    operadores = ["+", "-", "*", "/"]
    pilha_infixa = []

    for token in tokens:
        if token in operadores:
            b = pilha_infixa.pop()
            a = pilha_infixa.pop()
            expressao = "(" + a + " " + token + " " + b + ")"
            pilha_infixa.append(expressao)
        else:
            numero = float(token)
            if numero == int(numero):
                pilha_infixa.append(str(int(numero)))
            else:
                pilha_infixa.append(str(numero))

    resultado = pilha_infixa[0]
    if resultado[0] == "(" and resultado[-1] == ")":
        resultado = resultado[1:-1]

    return resultado

def calcular_rpn(expressao):
    global X, Y, Z, T

    X = 0.0
    Y = 0.0
    Z = 0.0
    T = 0.0

    tokens = expressao.strip().split()

    if not validar_expressao(tokens):
        return

    operadores = ["+", "-", "*", "/"]

    print()
    print(f"  {'AÇÃO':<35} {'T':>6}  {'Z':>6}  {'Y':>6}  {'X':>8}")
    print("-" * 70)

    for token in tokens:

        if token not in operadores:
            push(float(token))
            mostrar_pilha("ENTER " + token)

        else:
            b = pop()
            a = pop()

            resultado = 0.0

            if token == "+":
                resultado = a + b
            elif token == "-":
                resultado = a - b
            elif token == "*":
                resultado = a * b
            elif token == "/":
                if b == 0:
                    print("ERRO: Divisão por zero")
                    return
                resultado = a / b

            push(resultado)
            mostrar_pilha("OP " + token + "  (" + str(a) + " " + token + " " + str(b) + " = " + str(resultado) + ")")

    notacao_infixa = converter_para_infixa(tokens)

    print()
    print("  Expressão RPN digitada : " + expressao)
    print("  Notação Infixa         : " + notacao_infixa)
    print()
    print("  O resultado da expressão algébrica é: " + str(X))
    print()

print("  Operadores aceitos: +  -  *  /")
print("  Exemplo de entrada: 5 1 2 + 4 * + 3 -")
print("  Digite 'sair' para encerrar o programa.")
print()

# Loop principal do programa
while True:
    entrada = input("  Digite a expressão RPN: ")

    if entrada.lower() == "sair":
        print()
        print("  Programa encerrado.")
        print()
        break

    if entrada.strip() == "":
        print("  Por favor, digite uma expressão.")
        continue

    calcular_rpn(entrada)