quant = int(input("Quantas notas você tem?"))
soma = 0
cont = 0
while cont < quant: 
   nota = float(input("Digite sua nota: "))
   soma += nota
   cont+= 1
media = soma/quant
if media <= 6 and media >= 0:
   print(f"Abaixo da média, Sua média é {media:.2f}")
if media > 6 and media < 8: 
    print(f"Na média, Sua média é {media:.2f}")
if media <=8 and media >= 9:
   print(f"Quase lá, Sua média é {media:.2f}")
if media == 10:
   print(f"Média máxima, Sua média é {media:.2f}")