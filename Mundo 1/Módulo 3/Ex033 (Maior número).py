n1  = int(input("Digite um número: "))
n2 = int(input("Digite um número: "))
n3 = int(input("Digite um número: "))
numeros = [n1,n2,n3]
maior = numeros[0]
menor = numeros[0]
for i in numeros:
    if i> maior:
        maior = i
    if i< menor:
        menor = i
print(f"O menor é {menor} e o maior é {maior}.")