frase = str(input("Digite a frase mais legal que você conhece: ")).strip().upper()
print(f"A letra 'A' aparece: {frase.count("A")} vezes. Na primeira vez na posição {frase.find("A")} e na última na posição {frase.rfind("A")}.")
