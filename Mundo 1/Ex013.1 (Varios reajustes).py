sal = float(input("Digite seu salário atual: "))
rea = float(input("Digite a porcentagem do aumento: "))
aum = rea/100
calc = aum+1
res = sal*calc
print(f"Seu salário de {sal} após o reajuste de 15% passa a ser {res:.2f}")