# Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços. Exemplos de palíndromos

Frase = str(input("Digite uma frase! ")).strip().upper()
Palavras = Frase.split()
Junto = "".join(Palavras)
Inverso = ""

for Letra in range(len(Junto) - 1, -1, -1):
    Inverso += Junto[Letra]
if Junto == Inverso:
    print("Temos um palíndromo!")
else:
    print("Essa palavra não é um palíndromo!")
