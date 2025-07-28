media = 0
maior = 0
mulhe = 0
nomeH = ''
for p in range(1,6):
    print(f"{'x'*5} {p}° Pessoa {'x'*5}")
    nome = input("Nome: ")
    idade = int(input("Idade: "))
    sexo = str(input("Sexo [M/F]: ")).upper().strip()
    media +=idade 
    if sexo == 'M':
        if maior == 0:
            maior = idade
            nomeH = nome
        else:
            if idade > maior:
                maior = idade
                nomeH = nome
    if sexo == 'F':
        if idade < 20:
            mulhe += 1 
print(f"""
A média de idade do grupo é de {media/5}.
O homem mais velho tem {maior} e se chama {nomeH}.
Ao todo são {mulhe} mulheres com menos de 20 anos. """)