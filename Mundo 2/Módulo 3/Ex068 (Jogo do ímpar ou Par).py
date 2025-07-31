from random import randint
np = randint(1,10)
n = int(input("Digite um valor: "))
ip = str(input("Impar ou par? [I/P] "))[0].upper()
v = cont = 0
while True:
    if ip == 'I':
        cont+=1
        if sum(n,np) % 2 == 0:
            print("Você perdeu!")
            break
        else:
            print(f"Você ganhou!\nVocê digitou: {n}\nA máquina digitou: {np}")
            v+=1
            n = int(input("Digite um valor: "))
            ip = str(input("Impar ou par? [I/P] "))[0].upper()
    elif ip == 'P':
        cont+=1
        if sum(n,np) % 2 == 0:
            print("Você ganhou!\nVocê digitou: {n}\nA máquina digitou: {np} ")
            v+=1
            n = int(input("Digite um valor: "))
            ip = str(input("Impar ou par? [I/P] "))[0].upper()
        else:
            print(f"Você perdeu!\nVocê digitou: {n}\nA máquina digitou: {np}")
            break
print(f"GAME OVER! Você ganhou {v} vezes em {cont} tentativas")