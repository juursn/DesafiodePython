dia = int(input("Digite a dia: "))
mes = int(input("Digite o mês: "))
ano = int(input("Digite o ano: ")) 
dias = (31,30,29,28)
if ano < 2025 and ano > 0:
    if mes <= 12 and mes >0:
        if mes == 4 or mes == 6 or mes == 9 or mes == 11:
            if dia > dias[1]:
                print(f"A data {dia}/{mes}/{ano} é uma data inválida!")
            else: 
                print(f"A data {dia}/{mes}/{ano} é uma data válida!")
        elif mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12:
            if dia > dias[0]:
                print(f"A data {dia}/{mes}/{ano} é uma data inválida!")
            else:
                print(f"A data {dia}/{mes}/{ano} é uma data válida!")
        elif mes == 2:
            if(ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
                if dia > dias[2]:
                    print(f"A data {dia}/{mes}/{ano} é uma data inválida!")
                else:
                    print(f"A data {dia}/{mes}/{ano} é uma data válida!")
            elif dia > dias[3]:
                print(f"A data {dia}/{mes}/{ano} é uma data inválida!")
            else:
                print(f"A data {dia}/{mes}/{ano} é uma data válida!")
    else:
        print(f"A data {dia}/{mes}/{ano} é uma data inválida!")
else:
    print(f"A data {dia}/{mes}/{ano} é uma data inválida!")