from random import shuffle
alunos = []
for i in range(1,4):
    nome = input(f" Digite o nome do {i}° aluno: ")
    alunos.append(nome)
shuffle(alunos)
for quando,aluna in enumerate(alunos):
    print(f"O{quando+1}° aluno a apresentar vai ser {aluna}!")