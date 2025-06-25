from math import radians,sin,cos,tan
from fractions import Fraction
an = float(input("Digite o ângulo desejado: "))
sen = sin(radians(an))
fsen = Fraction(sen).limit_denominator(100) 
coss = cos(radians(an))
fcos = Fraction(coss).limit_denominator(100) 
tang = tan(radians(an))
ftan = Fraction(tang).limit_denominator(100) 
print(f"O seno do ângulo de {an}° é de aproximadamente {sen:.2f} ou {fsen}\nO cosseno do ângulo de {an}° é de aproximadamente {coss:.2f} ou {fcos}\nA tangente do ângulo de {an}° é de aproximadamente {tang:.2f} ou {ftan}")