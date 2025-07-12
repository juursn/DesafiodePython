nome = str(input("Digite seu nome completo: ")).strip()
print(f"""
Olá {nome.title()}!
Em maiúsculas: {nome.upper()}
Em minúsculas: {nome.lower()}
Quantidade de letras: {len(nome) - nome.count(' ')}
Seu primeiro nome tem: {nome.find(' ')} letras""")