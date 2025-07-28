maior = 0
menor = 0
for i in range(0,5):
    peso = float(input("Digite seu peso: "))
    if i == 0:
        maior = peso
        menor = peso
    else:
        if maior < peso:
            maior = peso
        if menor > peso:
            menor = peso
print(f"Maior peso: {maior}\nMenor peso: {menor} ")