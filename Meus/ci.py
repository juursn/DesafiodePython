from time import sleep
def contador(ini, fim, pas):
    if pas < 0:
        pas *= -1
    if pas == 0:
        pas = 1
    print(f"Contagem de {ini} até {fim} de {pas} em {pas}")
    sleep(1.5)
    if ini < fim:
        cont = ini
        while cont <= fim:
            print(f"{cont} ", end='', flush=True)
            sleep(0.5)
            cont += pas
        print("FIM")
    else:
        cont = ini
        while cont >= fim:
            print(f"{cont} ", end='', flush=True)
            sleep(0.5)
            cont -= pas
        print("FIM")
contador(1, 10, 1)
contador(10, 0, 2)
i = int(input("Início: "))
f = int(input("Fim: "))
p = int(input("Passo: "))
contador(i, f, p)