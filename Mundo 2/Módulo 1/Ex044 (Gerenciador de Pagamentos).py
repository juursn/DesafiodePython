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
    print(f"O valor a ser pago é de {valor} em parcelas de {valor/2}")
elif pagar == 4:
    x = int(input("Em quantas vezes você deseja pagar? "))
    if x>=3:
        print(f"O valor a ser pago é de {valor*1.20} em parcelas de {(valor*1.20)/x}")
    else:
        print("Valor inválido")
else:
    print("Valor inválido")