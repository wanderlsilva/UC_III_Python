idade = int(input("informe sua idade"))
class_f = int(input("qual a classificação do filme?:"))

if idade >=18:
    print ("apenas para maiores de 18")
elif idade >=14:
    print ("apenas para maiores de 14")
elif idade >=4:
    print ("filme infantil")
else:
    print ("acesso negado")
    