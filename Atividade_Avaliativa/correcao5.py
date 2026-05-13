senha = input("Informe sua senha")
numeros = int(input("Possui numeros - 1 sim 0 não"))
letra = int(input("Possui letra maiuscula - 1 sim 0 não"))
if len(senha) >8 and numeros ==1 and letra ==1:
    print("Senha forte")
elif len(senha) >8 and numeros ==1:
    print("Senha média")
else:
    print("Senha fraca")