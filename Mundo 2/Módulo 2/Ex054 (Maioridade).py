from datetime import datetime
maior = 0
menor = 0
for i in range(0,7):
    ano = int(input("Digite seu ano de nascimento: "))
    if datetime.now().year - ano < 18:
        menor +=1
    else:
        maior +=1 
print(f"{menor} pessoas ainda não compleram 18 anos e {maior} já completaram")
    
