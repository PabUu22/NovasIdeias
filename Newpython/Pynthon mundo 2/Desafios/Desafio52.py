#  Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

num = int(input("Digite um número: "))
tot = 0
for n in range(1, num + 1):
    if num % n == 0:
        print("\033[33m", end=" ")
        tot += 1
    else:
        print("\033[31m", end=" ")
    print("{}".format(n), end=" ")
print("\n\033[m0 número {} foi divisível {} vezes".format(num, tot))
if tot == 2:
    print("E por isso ele é primo")
else:
    print("E por isso ele não é primo")
