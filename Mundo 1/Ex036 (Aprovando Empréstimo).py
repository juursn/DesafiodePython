valor = float(input("Digite o valor da casa: "))
salario = float(input("Digite seu salário: "))
anos = int (input("Em quantos anos você irá pagar?"))
prest = valor/(12*anos)
if prest > salario*(30/100):
    print(f"Emprestimo negado, você teria que pagar {prest:.2f}")
else:
    print(f"aprove, você irá pagar {prest:.2f} por mês.")