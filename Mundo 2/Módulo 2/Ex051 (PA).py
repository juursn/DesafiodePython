t = int(input("Digite o primeiro termo da PA: "))
r = int(input("Digite a razão: "))
d = t + (10-1) * r
for i in range(t,d+r,r):
    print(i)