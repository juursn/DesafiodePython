v = 0
n = int(input("Digite um número: "))
for i in range(2,n-1):
    if n % i == 0:
        v = i
if v == 0:
    print(f"O número {n} é primo!")
else:
    print(f"O número {n} não é primo! pois é divisivel por {v}")