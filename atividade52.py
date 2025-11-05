# Peça a quantidade q (q>0). Leia q inteiros e armazene em uma lista.
# Exiba: maior, menor, média com 2 casas, quantos pares e quantos ímpares.
# Ex.: [5, 2, 9, 2] → maior=9, menor=2, média=4.50, pares=2, ímpares=2.

quantidade = int(input('Digite a quantidade: '))
numeros = []

for i in range(quantidade):
    numero = int(input(f"Digite o número: "))
    numeros.append(numero)

maior = max(numeros)
menor = min(numeros)
media = sum(numeros) / quantidade

pares = 0
impares = 0

for i in numeros:
    if i % 2 == 0:
        pares += 1
    else:
        impares += 1

print(f"maior={maior}, menor={menor}, média={media:.2f}, pares={pares}, ímpares={impares}")
