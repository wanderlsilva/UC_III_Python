print("==Sistema de controle de entrada==")
print("-"*20)

nome = input("Informe o nome:\n" )
idade = int(input("Informe a idade:\n "))
convite = input("Possui convite? - s?n:\n")
print("-"*20)

if idade >= 16 and convite == "s":
    print("Apenas entram com convite")
elif idade < 16:
    print("Não entram")
else:
    print("entrada negada")