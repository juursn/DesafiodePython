n1 = int(input("Digite a medida do primeiro lado: "))
n2 = int(input("Digite a medida do segundo lado:  "))
n3 = int(input("Digite a medida do terceiro lado: "))
if n1 < n2+n3 and n2 < n1+n3 and n3< n1+n2:
    print("Formam um triângulo lindo!")
else:
    print("Não consegue formar um triângulo!")