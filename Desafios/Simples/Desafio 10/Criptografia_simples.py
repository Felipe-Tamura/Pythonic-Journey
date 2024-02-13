import random as rnd
import os
from dataclasses import dataclass


@dataclass
class Cifra:
    __alfabeto = 'abcdefghijklmnopqrstuvwxyz'
    __escriba = []
    __varicao = 25
    __palavra: str
    
    def cript(self):
        """ 
            Criptografando uma palavra usando Cifra de Cesar
            
            Args:
                -   __palavra: String que irá ser criptografada
        """

        #Garantindo que a lista está vazia
        self.__escriba.clear()
        
        #Loop nas palavras e iterando sobre o alfabeto
        for i in range(len(self.__palavra)):
            for j in self.__alfabeto:

                #Se a letra em '__palavra' é igual a letra no alfabeto
                if self.__palavra[i].lower() == j:

                    #Escolhendo um número aleatório entre 1 e 0
                    __escolha = rnd.randint(0, 1)
                    if __escolha == 1:#Adicionando letra em maiúsculo

                        #Pegando o indice padrão da letra e incrementando
                            #até o próximo indice da lista
                        __indice = self.__alfabeto.index(j) + self.__varicao
                        __letra = self.__alfabeto[
                            __indice if __indice < len(self.__alfabeto) - 1 else __indice - len(self.__alfabeto)
                        ] #Se o indice for muito maior que o ultimo indice
                            #de alfabeto nós precisamos decrementar para
                            #incrementar a continuação do alfabeto, como
                            #se ele fosse infinito
                        self.__escriba.append(__letra.upper())

                    elif __escolha == 0:#Adicionando letra em minúscula

                        __indice = self.__alfabeto.index(j) + self.__varicao
                        __letra = self.__alfabeto[
                            __indice if __indice < len(self.__alfabeto) - 1 else __indice - len(self.__alfabeto)
                        ]
                        self.__escriba.append(__letra.lower())
            if self.__palavra[i] == ' ':
                #Se o indice for um espaço (' ') nós adicionamos este espaço
                self.__escriba.append(self.__palavra[i])
        return ''.join(self.__escriba)

    def descript(self):
        """ 
            Descriptografando uma palavra usando Cifra de Cesar
            
            Args:
                -   __palavra: String que irá ser descriptografada
        """

        #Garantindo que a lista está vazia
        self.__escriba.clear()

        #Loop
        for i in range(len(self.__palavra)):
            # A mesma coisa que o 'cript' unica coisa que muda é o decremento
            for j in self.__alfabeto:
                if self.__palavra[i].lower() == j:
                    __indice = self.__alfabeto.index(j) - self.__varicao
                    __letra = self.__alfabeto[
                        #Aqui muda o decremento
                        __indice - self.__varicao if __indice > len(self.__alfabeto) - 1 else __indice 
                    ]
                    self.__escriba.append(__letra)
            if self.__palavra[i] == ' ':
                self.__escriba.append(self.__palavra[i])
        return ''.join(self.__escriba).capitalize()

    def clear():
        """ 
            Para limpar o terminal
        """
        os.system('cls' if os.name == 'nt' else 'clear')

if __name__ == '__main__':

    Cifra.clear()

    x = 'Palavra para ser criptografada'
    y = 'oZkzUqz ozqZ rdq BQhOsnFQzezcz'

    cripita = Cifra(x)
    print(cripita.cript())

    descripita = Cifra(y)
    print(descripita.descript())