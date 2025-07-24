n = 0 
for i in range(0,6):
    v = int(input("Digite o número: "))
    if v % 2 == 0:
        n = v + n
print(n)