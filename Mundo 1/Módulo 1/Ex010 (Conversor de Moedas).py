real = float(input("Digite o valor em real: "))
dolar = real/5.50
euro = real/6.38
libra = real/7.45
iene = real/0.038
print(f"Esse valor de R${real:.2f} reais equivale a: \n US${dolar:.2f} dolares \n €{euro:.2f} euros  \n £{libra:.2f} libras \n ¥{iene:.2f} ienes")