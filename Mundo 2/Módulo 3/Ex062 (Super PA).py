t = int(input("Digite o primeiro termo da PA: "))
r = int(input("Digite a razão: "))
cont = 1
ad = 0
v = 10
while v != 0:
    ad += v
    while cont <= ad:
        print(f"{t}", end=' ')
        t += r 
        cont +=1      
    print('PAUSE')
    v = int(input("Quantos valores a mais você deseja? "))    
print(f"FIM, foram mostrados {cont-1} termos da PA")