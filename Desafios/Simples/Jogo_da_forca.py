from mecanicas import engine

engine.limparTela()

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
    
    engine.limparTela()
    vidas = 5
    palavra_escolhida = [engine.palavra_aleatoria()]
    letra_escolhida = []

    while vidas > 0:
        print(' ' * 50, f'Vidas: {vidas}')
        
        for k in palavra_escolhida[0]:
            print('_' * len(k.split()), end=' ')
        
        letra_escolhida.append(input('\nLetra: '))

        for i in palavra_escolhida:
            if letra_escolhida[-1] in i:
                print('\nAcertou')
            else:
                print('\nVocê errou')
                vidas -= 1
            
            if i in letra_escolhida[-1] and vidas > 0:
                print(palavra_escolhida)
                print(letra_escolhida)
                menu()
    
        if vidas == 0:
            print(f'\nA palavra escolhida era: {str(palavra_escolhida)}')
            break
menu()