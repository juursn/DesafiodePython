def triangulo(l1,l2,l3):
    if l1<l2+l3 and l2<l1+l3 and l3<l1+l2:
        return True
    else:
        return False
l1 = int(input("Digite o primeiro lado: "))
l2 = int(input("Digite o segundo lado: ")) 
l3 = int(input("Digite o segundo lado: "))
if triangulo(l1,l2,l3) == True:
    print("Forma um lindo triângulo:")
    
    if l1 == l2 == l3:
        print("Equilátero!")
    elif l1 == l2 or l2==l3 or l1 == l3:
        print("Isóceles!")
    else:
        print("Escaleno!")
else:
    print("Não forma um triângulo...")