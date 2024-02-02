import random as rnd
import os


os.system('cls' if os.name == 'nt' else 'clear')

def cript(__palavra: str):
    """ 
        Criptografando uma palavra usando Cifra de Cesar
        
        Args:
            -   __palavra: String que irá ser criptografada
            -   descisao: Escolha entre criptografar ou descriptografar
    """
    __alfabeto = 'abcdefghijklmnopqrstuvwxyz'
    __escriba = []
    __acrescimo_de_letra = 25

    #Loop nas palavras e iterando sobre o alfabeto
    for i in range(len(__palavra)):
        for j in __alfabeto:

            #Se a letra em '__palavra' é igual a letra no alfabeto
            if __palavra[i].lower() == j:

                #Escolhendo um número aleatório entre 1 e 0
                __escolha = rnd.randint(0, 1)
                if __escolha == 1:#Adicionando letra em maiúsculo

                    #Pegando o indice padrão da letra e incrementando
                        #até o próximo indice da lista
                    __indice = __alfabeto.index(j) + __acrescimo_de_letra
                    __letra = __alfabeto[
                        __indice if __indice < len(__alfabeto) - 1 else __indice - len(__alfabeto)
                    ] #Se o indice for muito maior que o ultimo indice
                        #de alfabeto nós precisamos decrementar para
                        #incrementar a continuação do alfabeto, como
                        #se ele fosse infinito
                    __escriba.append(__letra.upper())

                elif __escolha == 0:#Adicionando letra em minúscula

                    __indice = __alfabeto.index(j) + __acrescimo_de_letra
                    __letra = __alfabeto[
                        __indice if __indice < len(__alfabeto) - 1 else __indice - len(__alfabeto)
                    ]
                    __escriba.append(__letra.lower())
    return ''.join(__escriba)

def descript(__palavra):
    __alfabeto = 'abcdefghijklmnopqrstuvwxyz'
    __escriba = []
    __decrescimo_de_letra = 25
    
    #Loop 
    for i in range(len(__palavra)):
        for j in __alfabeto:
            if __palavra[i].lower() == j:
                __indice = __alfabeto.index(j) + len(__alfabeto)
                __letra = __alfabeto[
                    __indice - __decrescimo_de_letra if __indice > len(__alfabeto) - 1 else __indice
                ]
                __escriba.append(__letra)
    return ''.join(__escriba)

x = 'Palavra para ser criptografada'

cripita = cript(x)
print(cripita)

y = 'OzkzUQZozQzrDQBqHOSNFQZEZcZ'
descripita = descript(y)
print(descripita)