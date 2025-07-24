import math
print("Bem-vindo a calculadora em python!")
while True:
    opc = int(input("Digite a operação desejada: 1-Adição, 2-Subtração, 3-Multiplicação, 4-Divisão, 5-Potênciação, 6-Radiciação 7- Sair "))
    n1 = int(input("Digite um valor: "))
    n2 = int(input("Digite outro valor: "))
    if opc==1:
        calc = n1+n2
        print(f"O resultado da soma é {calc}")
        
    elif opc==2:
        calc = n1-n2
        print(f"O resultado da subtração é {calc}")
        
    elif opc==3:
        calc = n1*n2
        print(f"O resultado da multiplicação é {calc}")
        
    elif opc==4:
        calc = n1 / n2 
        print(f"O resultado da Divisão é {calc}")
        
    elif opc==5:
        calc = math.pow(n1,n2)
        print(f"O resultado da potenciação é {calc}")
        
    elif opc==6:
        calc = math.pow(n1, 1/n2)
        print(f"O resultado da Radiciação é {calc}")
        
    elif opc==7:
        print("Final do programa")
        