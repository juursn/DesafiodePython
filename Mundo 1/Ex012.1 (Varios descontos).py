valor = float(input("Digite o valor da sua compra: "))
desc = float(input("Digite o desconto desejado: "))
onto = desc/100
calc = (100 - (onto*100))/100 
res = valor*calc
print(f"O valor R${valor} com o desconto de {desc}% é R${res}")