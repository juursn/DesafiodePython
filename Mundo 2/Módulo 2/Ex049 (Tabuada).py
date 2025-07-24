num = int(input("Digite a tabuada desejada: "))
tam = int(input("Até que valor: "))
for n in range(1,tam+1):
    print(f"{num} x {n} = {num*n}")