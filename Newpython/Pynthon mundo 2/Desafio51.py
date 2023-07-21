# Aqui dara inicio a continuação dos minha atividades, partindo de um novo inicio.

# Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.

first = int(input('Primeiro termo: '))
Razão = int(input('Razão: '))
décimo = first + (10 - 1) * Razão
for m in range(first, décimo + Razão, Razão):
    print("{}".format(m), end=" - ")
print("Acabou")