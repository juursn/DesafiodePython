quant = int(input("Quantas notas você tem? "))
soma = 0
for i in range(1,quant+1):
    nota = int(input(f"Digite sua {i}° nota: "))
    soma+= nota
media = soma/quant
if media <5:
    print(f"Você está REPROVADO! Sua média é {media:.2f}")
elif media >=5 and media<=7:
    print(f"Você está de RECUPERAÇÃO! Sua média é {media:.2f}")
else:
    print(f"Você está APROVADO! Sua média é {media:.2f}")