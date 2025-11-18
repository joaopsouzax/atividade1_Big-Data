import pandas as pd
numeros = []
print("Digite 10 números inteiros:")
for i in range(10):
    num = int(input(f"Digite o {i + 1}º número: "))
    numeros.append(num)
busca = int(input("\nDigite um número para verificar se está na lista: "))
posicoes = [i for i, n in enumerate(numeros) if n == busca]
if posicoes:
    print(f"\nO número {busca} foi encontrado nas posições: {posicoes}")
else:
    print(f"\nO número {busca} não se encontra na lista.")
