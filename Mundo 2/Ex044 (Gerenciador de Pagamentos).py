valor = float(input("Valor da compra: "))
pagar = int(input(""" Pressione:
[1] À vista dinheiro/cheque
[2] À vista no cartão
[3] 2x no cartão
[4] 3x ou mais no cartão 
"""))
if pagar == 1:
    print(f"O valor a ser pago é de {valor*0.90}")
elif pagar == 2:
    print(f"O valor a ser pago é de {valor*0.95}")
elif pagar == 3:
    print(f"O valor a ser pago é de {valor}")
elif pagar == 4:
    print(f"O valor a ser pago é de {valor*1.20}")
else:
    print("Valor inválido")