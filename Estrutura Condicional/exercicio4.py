#Exercicio para descobrir o numero maior
num1 = int(input("Digite o 1º Numero: "))
num2 = int(input("Digite o 2º Numero: "))
num3 = int(input("Digite o 3º Numero: "))

if num1 == num2 or num2 == num3 or num1 == num3:
    print("Tem numeros iguai digitado")
    exit() #Encerra o programa
elif num1 > num2 and num1 > num3:
    print("O Numero Maior é: ", num1)
elif num2 > num1 and num2 > num3:
    print("O Numero Maior é: ", num2)
else:
    print("O Numero Maior é: ", num3)