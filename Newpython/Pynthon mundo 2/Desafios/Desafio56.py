# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre: a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.
SomaIdade = 0
MédiaIdade = 0
MaiorIdadeHomem = 0
NomeDoMaisVelho = ""
TotMulher = 0
for Pess in range(1, 5):
    print("----- {} Pessoa -----".format(Pess))
    Nome = str(input("Qual nome da pessoa? ")).strip()
    Idade = int(input("Qual a idade? "))
    Sexo = str(input("Qual sexo [M/F]? ")).strip().upper()
    SomaIdade += Idade
    if Pess == 1 and Sexo in "Mm":
        MaiorIdadeHomem = Idade
        NomeDoMaisVelho = Nome
    if Sexo in "Mm" and Idade > MaiorIdadeHomem:
        MaiorIdadeHomem = Idade
        NomeDoMaisVelho = Nome
    if Sexo in "Ff" and Idade < 20:
        TotMulher += 1

MédiaIdade = SomaIdade / 4
print("A média de idade entre o grupo é {}".format(MédiaIdade))
print("O homeme mais velho tem {} anos e se chama {}".format(
    MaiorIdadeHomem, NomeDoMaisVelho))
print("Ao todo são {} mulheres com menos de 20 anos".format(TotMulher))
