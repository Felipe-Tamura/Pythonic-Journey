import os

os.system('cls' if os.name == 'nt' else 'clear')

def calcular_fatorial(valor):
    if valor == 0 or valor == 1:
        return 1
    else:
        for i in range(1, valor + 1):
            valor = valor * i
        return valor

while True:
    
    print('_'*50, '\nEsolha uma das opções', '\n1. Calcular fatorial', '\n2. Sair')
    mensagem = int(input('r: '))
    print('_'*50)
    os.system('cls' if os.name == 'nt' else 'clear')
    match mensagem:
        case 1:
            while True:
                fatorial = int(input('Valor fatorial: '))
                if fatorial != -1:
                    resultado = calcular_fatorial(fatorial)
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print(f'O fatorial de de {fatorial} é = {resultado}')
                else:
                    break
        case 2:
            break
        case _ as x:
            print(f'Valor {x} inválido, aceita apenas 1 e 2')