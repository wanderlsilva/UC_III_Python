media=int(input("Digite a sua media escolar: "))
renda=float(input("Digite a sua renda familiar: "))

if media >=8 and renda <=2000:
    print("bolsa integral")
elif media >=6:
    print("bolsa parcial")
else:
    print("não aprovado para bolsa")