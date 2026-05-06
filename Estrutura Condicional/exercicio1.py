#Estrutura IF, ELSE  e ELIF
nota1 = float(input("Digite a 1º Nota: "))
nota2 = float(input("Digite a 2º Nota: "))
media = (nota1 + nota2) / 2

if media >= 60:
    print("APROVADO")
    
elif media >= 30 and media <= 59:
    print("Exame Final")

else:
    print("REPROVADO")