d = float(input("Digite a distância em km que você irá percorrer: "))
if d <=200:
    print(f"O total da passagem é {d*0.50}")
else:
    print(f"O total da passagem é {d*0.45}")