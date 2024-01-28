import os

os.system('cls' if os.name == 'nt' else 'clear')

def palindromo(texto1):
    """ Verifica se uma palavra escrita ao contrário seria a mesma palavra escrita na ordem"""
    resultado = texto1.replace(' ', '')
    if resultado.lower() == resultado.lower()[::-1]:
        return print(f'A palavra {texto1} é um palíndromo')
    else:
        return print(f'A palavra {texto1} não é um padíndromo')

while True:
    print('_' * 50)
    print('Escolha uma das opções abaixo:')
    print('1. Verificar palíndromo')
    print('2. Sair')
    escolha = int(input('r: '))
    
    match escolha:
        case 1:
            palindromo(str(input('Dgitie a palavra: ')))
            
        case 2:
            break
        
        case _ as x:
            print(f'o valor {x} não corresponde as opções')