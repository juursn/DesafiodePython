s = float(input("Digite o seu salário: "))
if s <= 1200:
    n = s*1.15
    print(f"Seu salário atual é de R${n:.2f}!")
else:
    n = s*1.10
    print(f"Seu salário atual é de R${n:.2f}!")