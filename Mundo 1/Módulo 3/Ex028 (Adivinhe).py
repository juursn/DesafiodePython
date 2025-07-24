from random import randint
v = randint(1,5)
r = "s"
while r == "s":
    n = int(input("Tente adivinhar o número entre 0 e 5 que eu estou pensando: "))
    print("⋆"*40)
    print("Acertou!" if v==n else "Errou!")
    r = input("Deseja tentar novamente? (S/N) ").lower()