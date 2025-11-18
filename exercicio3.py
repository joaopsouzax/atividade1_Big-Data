import pandas as pd
numeros = []
for i in range(10):
    n = int(input(f"Digite o {i + 1}º número inteiro: "))
    numeros.append(n)
for i in range(len(numeros)):
    if numeros[i] < 0:
        numeros[i] = 0

print("Lista alterada (valores negativos substituídos por 0):")
print(numeros)
