print("Escolha o tipo do veiculo:")
print("1 - moto")
print("2- carro")
print("3- caminhão")

opcao= int(input("Informe o tipo do veiculo:"))

if opcao == 1:
    print("O valor do pedagio é R$5")
elif opcao ==2:
    print("O valor do pedagio é R$10")
elif opcao ==3:
    print("O valor do pedágio è de R$25")
else:
    print("veiculo não identificado")