# Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
from datetime import date

Atual = date.today().year
TotMaior = 0
TotMenor = 0

for Pess in range(1, 8):
    Nasc = int(input("O ano que a {} pessoa nasceu? ".format(Pess)))
    Idade = Atual - Nasc
    if Idade >= 21:
        TotMaior += 1
    else:
        TotMenor += 1
print("Ao todo tivemos {} pessoas maiores de idade".format(TotMaior))
print("Também tiveram {} pessoas menores de idade".format(TotMenor))
