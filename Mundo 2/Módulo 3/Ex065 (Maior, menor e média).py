r = 's'
cont = media = maior = menor = 0
while r in 'Ss':
    n = int(input("Digite um número: "))
    r = str(input("Deseja continuar? [S/N]"))
    media += n
    cont +=1
    if maior and menor == 0:
        maior = menor = n
    else:
        if maior < n:
            maior = n
        if menor > n:
            menor = n
print(f"Você digitou {cont} valores e a média foi {media/cont:.2f}\nO maior valor é {maior}\nO menor valor é {menor}")