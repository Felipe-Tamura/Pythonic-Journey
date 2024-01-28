import os

os.system('cls' if os.name == 'nt' else 'clear')

def contarVogais(texto):
    """ Conta quantas vogais uma frase ou palavra possui """
    vogais = 'aeiou'
    return len([c for c in texto.lower() if c in vogais])

while True:
    print('_' * 50, '\nEscolha uma das opções abaixo', '\n1. Contar vogais', '\n2. Sair')
    escolha = int(input('r: '))

    match escolha:
        case 1:
            countW = str(input('Digite a frase/palavra: '))
            resultado = contarVogais(countW)
            print(f'Na frase \u0027{countW}\u0027 existe {resultado} palavra(s)') #unicode characters
        
        case 2:
            break
        
        case _ as erro:
            print(f'O valor {erro} não é valido, por favor apenas 1 e 2')