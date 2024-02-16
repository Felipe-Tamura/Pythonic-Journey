from dataclasses import dataclass
import pandas as pd
import csv
import re


@dataclass
class banco_de_dados:
    """ 
        Para adicionar e excluir contatos em um arquivo csv.
    """
    arquivo = 'Desafios/Intermediário/Desafio 1/contato.csv'

    @classmethod
    def adicionar(cls, nome, numero, email):
        """ 
            Adicionando contato no arquivo
            Args:
                - nome: Nome da pessoa que você quer adicionar na lista
                - numero: Numero da pessoa que você quer adicionar
                - email: E-mail da pessoa que você quer adicionar
        """

        try:
            valid = cls.__validar_email(email)
            if not valid:
                print(f'E-mail \'{email}\' inválido, tente outro e-mail!')
            else:
                tab_contato = pd.read_csv(cls.arquivo)
                dado = (
                    {
                        'Nome': nome,
                        'Numero': numero,
                        'Email': email
                    }
                )
                if numero in tab_contato.Numero:
                    print('Esta conta já existe')
                else:
                    tab_contato.loc[len(tab_contato)] = dado
                    tab_contato.to_csv(cls.arquivo, index=False)

        except FileNotFoundError:
            print(f'Arquivo \'{cls.arquivo}\' não encontrado')
        except Exception as e:
            print(f'Erro inesperado: {e}')

    def excluir(self, dado_para_excluir):
        """ 
            Excluindo um contato da lista de contatos
            Args:
                - dado_para_excluir: Coloque o nome da pessoa que
                    deseja excluir
        """
        lista = []

        try:
            # Lendo o arquivo csv
            self.arquivo
            #Apagando o item do arquivo

        except FileNotFoundError:
            print(f'O arquivo \'{self.arquivo}\' não foi encontrado')
        except Exception as e:
            print(f'Erro inesperado: {e}')
    
    # Verificando se o email é válido
    @classmethod
    def __validar_email(cls, email_de_verificacao):
        padrao = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        verif = re.match(padrao, email_de_verificacao)
        if verif:
            return True
        else:
            return False
    
    # Verificando se o número de telefone é válido
    def __validar_telefone():
        pass

if __name__ == '__main__':

    bd = banco_de_dados()
    contato3 = bd.adicionar('Felipe', 432895, 'felipe@gmail.com')
    bd.excluir('Felipe')