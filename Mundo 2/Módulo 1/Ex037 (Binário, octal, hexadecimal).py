n = int(input("Digite um número inteiro: "))
e = int(input("""
[1] Converter para binário
[2] Converter para octal
[3] Converter para hexadecimal
    Digite a opção desejada: """))
if e == 1:
    print(f"O número {n} convertido para binário fica: {bin(n)}")
elif e == 2:
    print(f"O número {n} convertido para octal fica: {oct(n)}")
elif e == 3:
    print(f"O número {n} convertido para hexadecimal fica: {hex(n)}")
else:
    print("Inválido")