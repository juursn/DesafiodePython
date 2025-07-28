v = 0
n = int(input("Digite um número: "))
for i  in range(1, n + 1):
    if n % i == 0:
        print('\033[33m', end=' ')
        v +=1
    else:
        print('\033[31m', end=' ')
    print(f"{i}", end='')
print(f"\n\033[mO número {n} foi divisível {v} vezes")
if v == 2: 
    print("E por isso ele é PRIMO!")
else:
    print("E por isso ele NÃO É PRIMO!")