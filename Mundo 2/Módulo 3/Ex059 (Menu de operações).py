from time import sleep
op = 0
n1 = int(input("Digite o 1° número: "))
n2 = int(input("Digite o 2° número: "))
while True:
    if op == 0:
        op = int(input("""
        [1] somar
        [2] multiplicar
        [3] maior
        [4] novos números
        [5] Sair
        Digite sua opção >>> """))
        print(f"{'='*50}")
    elif op == 1:
        print(f"A soma dos dois número resulta em: {n1+n2}")
        op = 0
        sleep(3)
    elif op == 2:
        print(f"A multiplicação dos dois números resulta em: {n1*n2}")
        op = 0
        sleep(3)
    elif op == 3:
        if n1 > n2:
            print(f"Entre {n1} e {n2} o maior é {n1}")
        else:
            print(f"Entre {n1} e {n2} o maior é {n2}")
        op = 0
        sleep(3)
    elif op == 4:
        print("Vamos mudar os valores então...")
        n1 = int(input("Digite o 1° número: "))
        n2 = int(input("Digite o 2° número: "))
        op = 0
        sleep(3)
    elif op == 5:
        print("Saindo...")
        sleep(2)
        break
    else:
        print("Valor inválido!!")