print("buffet restaurante ")
valor_pago = float(input("informe valor pago"))
possui_cupom =int(input("possui cupom 1 sim 0 não"))
if valor_pago > 50:
    print ("buffet liberado")
elif possui_cupom ==1:
    print ("buffet liberado")
else: 
    print("buffet não liberado")