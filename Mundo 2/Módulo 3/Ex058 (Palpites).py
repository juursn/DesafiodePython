from time import sleep
from random import randint 
cont = 0
print("Vamos Jogar um jogo! Vou pensar em um número de 1 a 10...")
sleep(1)
print("Pensando...")
sleep(1)
a = randint(1,10)
tent = int(input("Tente adivinhar: "))
while a != tent:
    cont +=1
    if tent > a:
        tent = int(input("Tente um número menor: "))
    else:
        tent = int(input("Tente um número maior: "))
print(f"Você precisou de {cont} tentativas para adivinhar")