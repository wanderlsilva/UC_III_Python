numerocamisas = int(input("Digite a quantidade de camisas: "))
valorCamisa = 12.50
valorFinal = numerocamisas * valorCamisa

if numerocamisas <= 5:
    valorDesconto = valorFinal * 0.03
    totalFinal = valorFinal - valorDesconto 
elif numerocamisas <= 10:
    valorDesconto = valorFinal * 0.05
    totalFinal = valorFinal - valorDesconto 
else:
    valorDesconto = valorFinal * 0.07
    totalFinal = valorFinal - valorDesconto 
     
#print("Valor Final : R$ ", valorFinal)
print(f"Valor Final : R$ {totalFinal:.2f}")