while True:
    word = input("Digite alguma coisa: ")
    if word == "73":
        print("Fim do programa!")
        break
    elif word.isnumeric(): #True caso tenha somente números
        print(f"{word} é numérico")
    elif word.islower(): #True caso tenha somente letras minusculas
        print(f"{word} é minusculo")
    elif word.isupper(): #True caso tenha somente letras maiusculas
        print(f"{word} é maiusculo")
    elif  word.isalpha(): #True caso tenha somente letras
        print(f"{word} tem letras")
    elif word.isalnum(): #True caso tenha letras e números
        print(f"{word} tem letras e números")
    elif word.isascii(): #True caso exista na tabela ASCII
        print(f"{word} está na tabela ASCII")
    elif word.isidentifier(): #True caso cumprir as wnormas de uma variável
        print(f"{word} poderia ser uma variável")
    elif word.isspace(): #True caso só tenha espaço em branco
        print(f"{word} tem somente espaços em branco")
    else:
        print(f"{word} não faço ideia do que seja isso...")