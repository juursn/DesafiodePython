from datetime import datetime
ano = int(input("Digite o ano do seu nascimento: "))
atual = datetime.now().year
temp = atual-ano
if  temp == 18:
    print("Você precisa se alistar!")
elif  temp < 18:
    print(f"Ainda não é a hora, faltam {18-temp} anos ")
else:
    print(f"Passou da hora! deveria ter feito a {temp-18} anos atrás.")