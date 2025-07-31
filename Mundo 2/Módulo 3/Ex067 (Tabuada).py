cont = 1
v1 = 0
while True: 
    v1 = int(input("Digite a tabuada desejada: "))
    if v1<0:
        break
    print(f"{'-'*50}")
    print(f"{'x'*10} Tabuada do {v1} {'x'*10}")
    while cont<10:
        print(f"{v1} x {cont} = {v1*cont}")
        cont +=1
    print(f"{'-'*50}")
    cont = 1
print("Fim do programa!")