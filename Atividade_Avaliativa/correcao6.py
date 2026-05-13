ten = float(input("informe a temperatura"))
umi = float(input("informe a umidade do ar"))
if ten > 40 and umi < 10: 
    print("clima seco")
elif ten < 20:
    print("clima frio")
else:
    print("clima estavel") 