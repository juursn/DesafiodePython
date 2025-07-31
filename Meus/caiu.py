import random
contV = 0
while True:
    player = int(input("Digite um número: "))
    maquina = random.randint(1, 10)
    soma = player + maquina
    esc = ' '
    while esc not in 'PI':
        esc = str(input("Escolha: par ou impar [P/I]. ")).strip().upper()[0]
    print(f"Sua escolha foi {player}, a escolha do computador foi {maquina}, e a soma dos números é: {soma}.")
    if esc == 'P':
        if soma % 2 == 0:
            print("Você venceu.")
            contV += 1
        else:
            print("Você perdeu.")
            break
    elif esc == 'I':
        if soma % 2 == 0:
            print("Você venceu.")
            contV += 1
        else:
            print("Você perdeu.")
            break
    print("Jogando novamente...")
print(f"Você venceu um total de {contV} consecutivas.")