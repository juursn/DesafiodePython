n = soma = cont =0
while n != 999:
    n = int(input("Digite um número: [999 para] "))
    if n != 999:
        soma += n
        cont +=1
print(f"Você digitou {cont} valores e a soma deles é {soma}")