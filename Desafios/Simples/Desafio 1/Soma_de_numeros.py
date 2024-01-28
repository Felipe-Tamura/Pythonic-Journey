import os

os.system('cls' if os.name == 'nt' else 'clear')

def soma(valor1, valor2):
    return valor1 + valor2

while True:
    print('_'*50)
    print('Escolha uma das opções abaixo:')
    print('1. Realizar soma')
    print('2. Sair')
    resposta = int(input('r: '))

    if resposta == 2:
        break
    
    val1 = int(input('Valor 1: '))
    val2 = int(input('Valor 2: '))

    print('O resultado da soma é =', soma(val1, val2))
