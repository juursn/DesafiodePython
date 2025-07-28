n = 0 
p = 0
for i in range(0,6):
    v = int(input("Digite o número: "))
    if v % 2 == 0:
        n = v + n
        p+= 1
print(f"Você informou {p} números pares e a soma foi {n}")