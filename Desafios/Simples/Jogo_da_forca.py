import pandas as pd
import random as rnd
import os

def limparTela():
    os.system('cls' if os.name == 'nt' else 'clear')

def palavra_aleatoria():
    palavras_tabela = pd.Series(['Sao paulo'])
    return rnd.choice(palavras_tabela)

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
        print(forca[i], end=' * ' if forca[i] == ' ' else ' ')
    
    while vidas > 0:
        print(' ' * 50, f'Vidas: {vidas}')
        numero_ocorrencia = int(0)

        letra_escolhida.append(input('\nLetra: '))

        if letra_escolhida[-1] in palavra_escolhida.lower() or letra_escolhida[-1] in palavra_escolhida.upper():   
            for i in palavra_escolhida:
                if letra_escolhida[-1] in i.lower() or letra_escolhida[-1] in i.upper(): forca[numero_ocorrencia] = i
                numero_ocorrencia += 1
                if resultado.join(forca) == palavra_escolhida:
                    print('Você venceu!!! Parabéns!!!!')
                    menu()
                    break
        else:
            vidas -= 1

        for i in range(len(forca)):
            if palavra_escolhida[i] == ' ':
                forca[i] = ' '
            print(forca[i], end=' * ' if forca[i] == ' ' else ' ')
        
        if vidas == 0:
            print(f'\nA palavra escolhida era: {str(palavra_escolhida)}')
            menu()
            break
        
menu()