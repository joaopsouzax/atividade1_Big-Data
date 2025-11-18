import pandas as pd

print("DIGITE OS 6 NÚMEROS SORTEADOS NA MEGA-SENA:")

numeros_sorteados = []

for i in range(6):
    while True:
        try:
            num = int(input(f"Número sorteado {i+1}: "))
            if num < 1 or num > 60:
                print("Digite um número entre 1 e 60.")
                continue
            if num in numeros_sorteados:
                print("Número repetido. Digite outro.")
                continue
            numeros_sorteados.append(num)
            break
        except ValueError:
            print("Digite um numero valido")

print("\n DIGITE OS 6 NÚMEROS DO SEU JOGO:")
numeros_jogador = []
for i in range(6):
    while True:
        try:
            num = int(input(f"Número sorteado {i + 1}: "))
            if num < 1 or num > 60:
                print("Digite um número entre 1 e 60.")
                continue
            if num in numeros_jogador:
                print("Número repetido. Digite outro.")
                continue
            numeros_jogador.append(num)
            break
        except ValueError:
            print("Digite um numero valido")

df_sorteio = pd.DataFrame({"Sorteados": numeros_sorteados})
df_jogador = pd.DataFrame({"Jogador": numeros_jogador})

acertos = set(numeros_sorteados).intersection(set(numeros_jogador))
quantiia_acertos = len(acertos)

print("\n RESULTADO FINAL")
print(f"Números sorteados: {sorted(numeros_sorteados)}")
print(f"Seus números:      {sorted(numeros_jogador)}")
print(f"Números acertados: {sorted(acertos)}")
print(f" Você fez {quantiia_acertos} {'ponto' if quantiia_acertos == 1 else 'pontos'}!")
