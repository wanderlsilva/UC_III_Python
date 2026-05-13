temperatura=float(input("Digite a temperatura do servidor: "))
cpu=float(input("Digite o Uso de CPU: "))

if temperatura>75 and cpu>90:
    print("Servidor Critico")
elif temperatura>60:
    print("Servidor em alerta")
else:
    print("Servidor Normal")