print("-" * 36)
print(" SISTEMA DE DIAGNÓSTICO DE INTERNET")
print("-" * 36)

roteador = int(input("O Roteador está ligado? - Responda 1 para Sim ou 0 para não \n"))
luzes = int(input("As Luzes estão ligadas? - Responda 1 para Sim ou 0 para não \n"))
cabo = int(input("O Cabo de Rede está conectado? - Responda 1 para Sim ou 0 para não \n"))
if roteador == 1 and luzes == 1 and cabo == 1:
    print("Está OK e funcionando!!!")
elif roteador == 0:
    print("Ligue o Roteador")
elif cabo == 0:
    print("Verifique o Cabo de Rede")
else:
    print("Problema no Modem!!!")
