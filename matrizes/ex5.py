matriz = []
for i in range(3):
    linha = []
    for j in range(3):
        msg = f'Numero da celula [{i}][{j}] ?'
        linha.append(int(input(msg)))
    matriz.append(linha)

pares = 0
for linha in matriz:
    for e in linha:
        if e % 2 == 0:
            pares += 1

for linha in matriz:
    print(linha)

print(f'A matriz contem {pares} numeros pares.')