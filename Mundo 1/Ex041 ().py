idade = int(input("Digite sua idade: "))
if idade> 0 and idade<=9:
    print("Você é um nadador MIRIM!")
elif idade > 9 and idade <=14:
    print("Você é um nadador INFANTIL!")
elif idade > 14 and idade <=19:
    print("Você é um nadador JUNIOR")
elif idade >19 and idade <=20:
    print("Você é um nadador SÊNIOR")
elif idade > 20:
    print("Você é um nadador MASTER!")