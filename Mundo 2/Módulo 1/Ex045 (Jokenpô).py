from random import randint
from time import sleep
print("Vamos jogar Jokenpô!")
res = 0
while res not in (1,2,3):
    res = int(input("[1] Pedra, [2] Papel, [3] Tesoura : "))
bot = randint(1,3)
if res<=3 and res>0:
    print("Pedra...")
    sleep(0.5)
    print("Papel...")
    sleep(0.5)
    print("Tesouraa!!")
    print(f"{'✂'*50}")
    if bot == 1:
        if res == 1:
            print(f"Empate! você escolheu {res} e eu {bot}")
        elif res == 2:
            print(f"Eu ganhei! você escolheu {res} e eu {bot}")
        elif res == 3:
            print(f"Você ganhou! você escolheu {res} e eu {bot}")
    elif bot == 2:
        if res == 1:
            print(f"Eu ganhei! você escolheu {res} e eu {bot}")
        elif res == 2:
            print(f"Empate! você escolheu {res} e eu {bot}")
        elif res == 3:
            print(f"Você ganhou! você escolheu {res} e eu {bot}")
    elif bot ==3:
        if res == 1:
            print(f"Você ganhou! você escolheu {res} e eu {bot}")
        elif res == 2:
            print(f"Eu ganhei! você escolheu {res} e eu {bot}")
        elif res == 3:
            print(f"Empate! você escolheu {res} e eu {bot}")