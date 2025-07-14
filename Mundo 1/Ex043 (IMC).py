peso = float(input("Digite seu peso: "))
altu = float(input("Digite sua altura: "))
if altu>2.0:
    altu= altu/100
imc= peso/(altu**2)
print(f"Seu IMC é: {imc:.2f}")
if imc> 40:
    print("Obesidade mórbida")
elif imc<40 and imc>=30:
    print("Obesidade")
elif imc<30 and imc>=25:
    print("Sobrepeso")
elif imc<25 and imc>=18.5:
    print("Peso ideal")
else:
    print("Abaixo do peso")