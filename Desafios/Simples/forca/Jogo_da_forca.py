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
    print(palavra_escolhida)
    
    while vidas > 0:
        print(' ' * 65, f'Vidas: {vidas}')
        
        letra_escolhida = []
        letra_escolhida.append(input('Letra: '))

        for i in palavra_escolhida:
            if letra_escolhida[::] == i[1]:
                print('Acertou')
            else:
                vidas -= 1
            
menu()