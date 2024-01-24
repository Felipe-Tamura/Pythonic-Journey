# - Escreva uma função que valide senhas com base em critérios, como
# comprimento mínimo, presença de letras maiúsculas e minúsculas,
# e números.
# Vamos usar exemplo de senha a seguinte: Gato123

senha = 'Gato123'

def valida_senha(valor):
    
    if len(valor) >= 8 :
        
        caracteres_especiais = '[,&^*!!:%$@%#]+'
        
        validacao = ({
            'tem': False,
            'maiusculo': False,
            'minusculo': False,
            'tem_numero': False,
        })
        
        for i in valor:
            if i in caracteres_especiais: validacao['tem'] = True
            if i.isupper(): validacao['maiusculo'] = True
            if i.islower(): validacao['minusculo'] = True
            if i.isnumeric(): validacao['tem_numero'] = True
        
        

    else:
        print('Tamanho de senha inválida, mínimo 8 caracteres')

valida_senha(senha)