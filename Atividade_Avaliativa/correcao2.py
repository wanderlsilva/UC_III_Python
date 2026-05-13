nome=input("Informe seu nome")
quantidade= int(input("Informe quantidade falata"))
nota= float(input("Informe a nota"))
if nota>8 and quantidade<3:
    print("elegivel para promocão")
elif nota>6 and nota<=8:
    print("bom desempenho")
else:
    print("precisa melhorar")