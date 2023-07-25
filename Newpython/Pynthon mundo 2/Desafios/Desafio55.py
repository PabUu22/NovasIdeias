# Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.
Maior = 0
Menor = 0
for Pess in range(1, 6):
    Peso = float(input("Digite o peso da {} pessoa: ".format(Pess)))
    if Peso == 1:
        Maior = Peso
        Menor = Peso
    else:
        if Peso > Maior:
            Maior = Peso
        if Peso < Menor:
            Menor = Peso
print("O maior peso registrado foi {}kg".format(Maior))
print("O menor peso registrado foi {}kg".format(Menor))
