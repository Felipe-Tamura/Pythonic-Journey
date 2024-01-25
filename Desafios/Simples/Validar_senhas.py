import os
import re

#Limpar prompt
os.system('cls' if os.name == 'nt' else 'clear')

def valida_senha(valor):
    """ 
        Validamos se a senha tem as credênciais necessárias
        
        - valor: senha para verificação
    """
    
    if len(valor) >= 8 :
        
        caracteres_especiais = r'[,&^*!!:%$@%#]+'#Reservando caractesres especiais do python com r'string'
        
        validacao = {
            'tem_caract': bool(re.search(caracteres_especiais, valor)),#Para procurar um caractere no valor
            'maiuscula': any(c.isupper() for c in valor),#Iterando no objeto para ver se é maiúsculo
            'minuscula': any(c.islower() for c in valor),#Iterando no objeto para ver se é minúsculo
            'numero': any(c.isnumeric() for c in valor)#Iterando no objeto para ver se possui número
        }
        
        mensagem_erro = {
            'tem_caract': f'A senha precisa conter pelo menos um destes caracteres: {caracteres_especiais}',
            'maiuscula': 'A senha precisa conter pelo menos uma letra maiúscula',
            'minuscula': 'A senha precisa conter pelo menos uma letra minúscula',
            'numero': 'A senha precisa conter pelo menos um número'
        }

        for crit, condicao in validacao.items():#Duas variáveis que receberão o mesmo valor
            if not condicao:#Verificando cada condição não verdadeira (2ª Variável)
                print(f'\nSenha inválida: {mensagem_erro[crit]}')#Alegando o erro (1ª Variável)
                break
        else:
            print('\nSenha válida, pode passar!!!')
            
    else:
        print('\nTamanho de senha inválida, mínimo 8 caracteres!!!\n')

#Loop infinito
while True:
    
    print('_'*50,'\nSelecione uma opção', '\n1. Continuar','\n2. Sair')
    mensagem = int(input('r: '))
    print('_'*50)
    
    match mensagem:
        case 1:
            senha = input('Senha: ')
            valida_senha(senha)  
        case 2:
            break
        case _ as x:
            print(f'Valor {x} inválido, apenas 1 ou 2')