import pandas as pd

nome = ["Ana", "Bruno", "Carla", "Daniel", "Eduardo",
         "Fernanda", "Gustavo", "Helena", "Igor", "Juliana"]

notas = [8.5, 6.0, 9.2, 5.8, 7.0, 4.5, 6.8, 10.0, 3.5, 7.5]

#Criando DataFrame

df = pd.DataFrame({'Nome': nome, 'Nota': notas})

#1.2-3
media = df['Nota'].mean()
print(f"\n Media da turma: {media:.2f}")

#1.4
maior_nota = df['Nota'].max()
menor_nota = df['Nota'].min()

alunos_maior = df[df["Nota"] == maior_nota]['Nome'].tolist()
alunos_menor = df[df["Nota"] == menor_nota]['Nome'].tolist()

print(f"Maior nota: {maior_nota} - Alunos: {', '.join(alunos_maior)}")
print(f"Menor nota: {menor_nota} - Alunos: {', '.join(alunos_menor)}")

print("\n Alunos com notas abaixo da média: ")
print(df[df['Nota'] < media])

acima_media = df[df['Nota'] >= media]
print("Alunos com notas maiores ou iguais á média: ")
print(df[df['Nota'] > media])
