ano = int(input("Digite o ano: "))
if ano % 4 == 0 or ano % 400 == 0:
    print("O ano é bissexto")
else:
    print("Não é bissexto")