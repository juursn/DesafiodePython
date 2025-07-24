from random import choice
alunos = []
for i in range(1,4):
    nome = input(f" Digite o nome do {i}° aluno: ")
    i+=1
    alunos.append(nome)
print(f"O aluno escolhido foi {choice(alunos)}!")