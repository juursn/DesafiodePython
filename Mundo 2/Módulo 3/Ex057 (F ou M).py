s = str(input("Informe seu sexo: [M/F] ")).upper().strip()[0]
while s not in 'MmFf':
    s = str(input("Dado inválido!! Digite novamente: "))
print(f"Registrado com sucesso! seu sexo é {s}")