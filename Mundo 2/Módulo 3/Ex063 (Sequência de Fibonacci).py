cont = 1
n = int(input("Quantos termos você quer mostrar? "))
ss = 1
aas = sq = 0
print(f"{aas} → {ss}", end=" → ")

while cont <= n-2:
    sq = aas + ss
    print(f"{sq}", end=' → ')
    aas = ss
    ss = sq
    cont +=1
print("FIM")