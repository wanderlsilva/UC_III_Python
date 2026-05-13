orcamento = int(input("Digite o seu orçamento: "))

if orcamento <= 1000:
    print("Modelo básico")
elif orcamento >= 1001 and orcamento < 2500:
    print("Modelo intermediário")
else:
    print("Modelo premium")       