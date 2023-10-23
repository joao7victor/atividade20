# Exercício Python 28: Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5
# e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
# O programa deverá escrever na tela se o usuário venceu ou perdeu.
# DICA ESTUDEM A BIBLIOTECA PYTHON RANDOM

import random

num = int(input("Digite um número entre 0 e 5: "))
aleatorio = random.randint(0, 5)

if num > 5 or num <0:
    print("Digite um número entre 0 e 5.")
elif num == aleatorio:
    print("Você ganhou o sorteio.")
else:
    print("Você perdeu o sorteio.")