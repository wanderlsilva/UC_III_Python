nota = float(input("informe a nota dsa prova"))
falta = int(input("informe a quantidade de falta"))
if nota >85 and falta <5:
    print("aprovado")
elif nota >70:
    print("lista de espera")
else:
    print("reprovado")
    