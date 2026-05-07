'''ELABORE UM ALGORITMO PARA DIAGNOSTICAR GRIPE COMUM.
USE OS SEGUINTES FATORES:
SINTOMAS -> FEBRE MODERADA, NARIZ ENTUPIDO, DOR DE GARGANTA, TOSSE
DURAÇÃO DOS SINTOMAS -> MENOR QUE 7 DIAS, MAIOR QUE 7 DIAS
CLASSIFICAÇÃO: PROVÁVEL GRIPE COMUM OU SINTOMAS ATÍPICOS, INVESTIGAR OUTRAS
CONDIÇÕES'''
print("-" * 20)
print("Diagnosticar Gripe Comum")
print("Responda com 1 - SIM ou 0 para NÃO")
print("-" * 20)

print("Está com Febre? \n")
res = int(input("1 - Sim ou 0 - Não"))
if res == 1:
    print("Está com Nariz Entupido? \n")
    res = int(input("1 - Sim ou 0 - Não"))
    if res == 1:
        print("Está com Dor de Garganta :\n")
        res = int(input("1 - Sim ou 0 - Não"))
        if res == 1:
            print("Está com Tosse :\n")
            res = int(input("1 - Sim ou 0 - Não"))
            if res == 1:
                print("Está GRIPADO :\n")
            else:
                print("Não está com Gripe")
                exit()
        else:
            print("Não está com Gripe")
            exit()
    else:
        print("Não está com Gripe")
        exit()
else:
    print("Não está com Gripe")