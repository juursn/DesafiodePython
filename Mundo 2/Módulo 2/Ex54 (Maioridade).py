from datetime import datetime
p = 0
for i in range(0,7):
    ano = int(input("Digite seu ano de nascimento: "))
    if datetime.now().year - ano < 18:
        p+=1
print(f"{p} pessoas ainda não compleram 18 anos ")
    
