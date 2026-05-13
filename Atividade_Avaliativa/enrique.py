kw = float(input("Digite quantidade de kWh consumidos: "))
if kw >300:
    print("Consumo elevado")
elif kw <=300 and kw >100:
    print("Consumo moderado")
else:
    print("Consumo baixo")