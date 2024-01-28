import pandas as pd
import random as rnd
import os

def limparTela():
    os.system('cls' if os.name == 'nt' else 'clear')

def palavra_aleatoria():
    tabela = pd.DataFrame(
        {
            'Cidade': ['Sao paulo', 'Campinas', 'Osasco', 'Pinheiros', 'Cotia'],
            'Comida':['Lasanha', 'Feijoada', 'Macarrão', 'Bife', 'Queijo'],
            'Objeto': ['Lapis', 'Garfo', 'Colher', 'Papel', 'Mesa'],
            'Filme': ['Fuga das galinhas', 'Jhon Wick', 'Harry Potter', 'A casa do Mickey Mouse', 'Matrix'],
            'Anime': ['Naruto', 'Hunter x Hunter', 'Bleach', 'Death Note', 'Noragami'],
        }
    )
    random_column = rnd.randint(0, 4)
    random_row = rnd.randint(0, 4)
    
    print(tabela.columns[random_column])
    return tabela.iat[random_row, random_column]

limparTela()

def menu():
    print('_'*50,'\nEscolha uma das opções','\n1. Jogar', '\n2. Sair')
    escolha = int(input('r: '))
    match escolha:
        case 1:
            jogo()
        case 2:
            exit()
        case _ as x:
            print(f'O valor {x} não é valido, por favor escolha de 1 a 2')
            menu()

def jogo():
    """ jogando """
    
    limparTela()
    vidas = 5
    palavra_escolhida = palavra_aleatoria()
    letra_escolhida = ['']
    forca = ['_'] * len(palavra_escolhida)
    resultado = ''
    
    for i in range(len(forca)):
        if palavra_escolhida[i] == ' ':
            forca[i] = ' '
        print(forca[i], end='*' if forca[i] == ' ' else ' ')
    
    #Loop infinito
    while vidas > 0:
        print(' ' * 50, f'Vidas: {vidas}')
        numero_ocorrencia = 0

        letra_escolhida.append(input('\nLetra: '))

        if letra_escolhida[-1] in letra_escolhida[:-1]:
            print(f'A letra "{letra_escolhida.pop()}" já foi')
        else:
            if letra_escolhida[-1] in palavra_escolhida.lower() or letra_escolhida[-1] in palavra_escolhida.upper():   
                for i in palavra_escolhida:
                    if letra_escolhida[-1] in i.lower() or letra_escolhida[-1] in i.upper(): forca[numero_ocorrencia] = i
                    numero_ocorrencia += 1
                    if resultado.join(forca) == palavra_escolhida:
                        print('Você venceu!!! Parabéns!!!!')
                        print(f'"{resultado.join(forca)}" era a resposta')
                        menu()
                        break
            else:
                vidas -= 1

        for i in range(len(forca)):
            if palavra_escolhida[i] == ' ':
                forca[i] = ' '
            print(forca[i], end='*' if forca[i] == ' ' else ' ')
            
        print('\nLetras que já foram: ', letra_escolhida)
        
        if vidas == 0:
            print(f'\nQue pena, a palavra escolhida era: {str(palavra_escolhida)}')
            menu()
            break
        
menu()