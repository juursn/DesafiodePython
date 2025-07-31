print("Vamos fatorar!!")
n = int(input("Digite um número: "))
cont = n 
f = 1
print(f"{n}! = ", end='')
while cont > 0:
    print(f"{cont}", end='')
    if cont > 1:
        print(' x ', end='')
    else:
        print(' = ', end='')
    f *= cont
    cont -=1
print(f"{f}", end=' ')