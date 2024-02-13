import os

os.system('cls' if os.name == 'nt' else 'clear')

def anagram(valor1: str, valor2: str):
    """ 
        Verificando se duas palavras são anagramas
            (Todas as letras iguais mas em lugares diferentes)

        Args:
            -   valor1: Valor de vefificação
            -   valor2: Valor de comparação
    """
    lista_de_letras = []
    
    #Loop de verificação
    while len(lista_de_letras) < len(valor1):
        tem_a_letra = False
        while not tem_a_letra:
            for i in valor1.lower():
                for j in valor2.lower():
                    if j == i:
                        lista_de_letras.append(i)
                        tem_a_letra = True

    #Concatenando e verificando
    if ''.join(lista_de_letras) == valor1.lower():
        print(f'\nAs palavras \'{valor1}\' e \'{valor2}\' são anagramas\n')
    else:
        print(f'\nAs palavras \'{valor1}\' e \'{valor2}\' não são anagramas\n')

#Loop infinito
while True:
    print('_' * 50, '\nEscolha uma das opções', '\n1. Verificar Anagramas', '\n2. Sair')
    verificacao = int(input('r: '))    
    print('_' * 50)

    match verificacao:
        case 1:
            vida = 5
            while vida > 0:
                val1 = input('Palavra 1: ')
                val2 = input('Palavra 2: ')
                anagram(val1, val2)
                vida-=1
        case 2:
            break
        case _ as x:
            print(f'Valor {x} inválido, escolha apenas 1 ou 2')