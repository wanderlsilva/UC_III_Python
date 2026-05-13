ram=int(input("digite a quantidade de memoria ram: \n"))
placa=int(input("possui placa de video 1-sim 2-nao\n"))

if ram>=16 and placa==1:
    print("alto desempenho")
    
elif ram >= 8 and ram <16:
    print("desempenho intermediario")
    
else:
    print("desempenho basico")