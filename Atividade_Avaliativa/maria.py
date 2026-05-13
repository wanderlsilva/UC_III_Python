quant_atraso = int(input("Informe a quantidade de dias atrasados: \n"))

if quant_atraso <= 5:
    print("Você recebeu uma multa leve.")
elif quant_atraso <=15:
    print("Você recebeu uma multa moderada.")
else:
    print("Você recebeu uma multa grave.")