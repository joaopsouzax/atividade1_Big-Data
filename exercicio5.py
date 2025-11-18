import pandas as pd

def soma(a:int, b:int) -> int:
    return a + b

def subtracao(a:int, b:int) -> int:
    return a - b

def multiplicacao(a:int, b:int) -> int:
    resultado = 0
    sinal = 1

    if b < 0:
        b = -b
        sinal *= -1
    if a < 0:
        a = -a
        sinal *= -1

    for _ in range(b):
        resultado = soma(resultado, a)
    return resultado * sinal

def potencia(a:int, b:int) -> int:

    if b == 0:
        return 1
    resultado = a
    for _ in range(1, b):
        resultado = multiplicacao(resultado, a)
    return resultado

a = int(input("Digite o primeiro número inteiro: "))
b = int(input("Digite o segundo número inteiro: "))

print("\nEscolha a operação desejada:")
print("1 - Soma")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Potência")

opcao = int(input("Digite a opção: "))

resultado = None
operacao = ""

if opcao == 1:
    resultado = soma(a, b)
    operacao = "Soma"
elif opcao == 2:
    resultado = subtracao(a, b)
    operacao = "Subtração"
elif opcao == 3:
    resultado = multiplicacao(a, b)
    operacao = "Multiplicação"
elif opcao == 4:
    resultado = potencia(a, b)
    operacao = "Potência"
else:
    print("Opção inválida!")

if resultado is not None:
    df = pd.DataFrame({
        "operacao": [operacao],
        "A": [a],
        "B": [b],
        "Resultado": [resultado]
    })

    print("\n Resultado da operação: ")
    print(df.to_string(index=False))
