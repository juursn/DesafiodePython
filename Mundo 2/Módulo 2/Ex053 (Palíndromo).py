p = "".join((input("Digite um palíndromo: ")).upper().split())
m = ''
for c in p:
    m = c + m
if m == p:
    print("É um belo palíndromo!")
else:
    print("Opa, isso não é um palíndromo")
    