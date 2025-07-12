time = []
jogador = {}
partidas = []
while True:
    jogador.clear()
    jogador['nome'] = str(input("Nome do jogador: "))
    total = int(input(f"Quantas partidas {jogador['nome']} jogou? "))
    partidas.clear()
    cont = 1
    while cont <= total:
        partidas.append(int(input(f"Quantos gols na partida {cont}? ")))
        cont += 1
    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)
    time.append(jogador.copy())
    while True:
        esc = str(input("Deseja continuar? [S/N] ")).upper()[0]
        if esc in 'SN':
            break
        print("ERRO! Digite apenas S ou N.")
    if esc in 'Nn':
        break
print('-' * 50)
print("N° ", end='')
for v in jogador.keys():
    print(f"{v:<17} ", end='')
print()
print('-' * 50)
for c, v in enumerate(time):
    print(f"{c:>5} ", end='')
    for i in v.values():
        print(f"{str(i):<17}", end='')
    print()
print('-' * 50)
while True:
    pesq = int(input("Qual jogador você quer ver os dados? (999 encerra): "))
    if pesq == 999:
        break
    if pesq >= len(time):
        print("ERRO! Esse jogador não existe no cadastro.")
    else:
        print(f"Estatísticas do jogador selecionado: {time[pesq]['nome']}.")
        for c, g in enumerate(time[pesq]['gols']):
            print(f"Na partida {c+1} o jogador {time[pesq]['nome']} fez {g} gols.")
    print("-" * 50)
print("Obrigado por usar o programinha de CAIO GUILHERME")