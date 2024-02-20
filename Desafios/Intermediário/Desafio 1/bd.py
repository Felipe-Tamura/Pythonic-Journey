from dataclasses import dataclass
import pandas as pd
import csv
import re
import os


@dataclass
class banco_de_dados:
    """ 
        Para adicionar e excluir contatos em um arquivo csv.
    """
    arquivo = 'Desafios/Intermediário/Desafio 1/contato.csv'

    @classmethod
    def adicionar(cls, nome: str, numero: str, email: str):
        """ 
            Adicionando contato no arquivo
            Args:
                - nome: Nome da pessoa que você quer adicionar na lista
                - numero: Numero da pessoa que você quer adicionar
                - email: E-mail da pessoa que você quer adicionar
        """

        try:
            valid_email = cls.__validar_email(email)
            valid_tel = cls.__validar_telefone(numero)

            if valid_email & valid_tel:
                tab_contato = pd.read_csv(cls.arquivo)
                dado = (
                    {
                        'Nome': nome,
                        'Numero': numero,
                        'Email': email
                    }
                )
                for lista in tab_contato.Numero:
                    if lista == numero:
                        print(f'Número \'{numero}\' já adicionado')
                        break
                else:
                    tab_contato.loc[len(tab_contato)] = dado
                    tab_contato.to_csv(cls.arquivo, index=False)

        except FileNotFoundError:
            print(f'Arquivo \'{cls.arquivo}\' não encontrado')
        except Exception as e:
            print(f'Erro inesperado: {e}')

    def editar(self, dado_para_editar):
        pass
    
    def excluir(self, dado_para_excluir):
        """ 
            Excluindo um contato da lista de contatos
            Args:
                - dado_para_excluir: Coloque o nome da pessoa que
                    deseja excluir
        """
        lista = []
        apagar_indice = 1
        
        try:
            # Lendo o arquivo csv
            with open(self.arquivo, 'r', newline='') as arquivo_entrada:
                leitor = csv.reader(arquivo_entrada)
                for listagem in leitor:
                    if listagem[apagar_indice] != dado_para_excluir:
                        lista.append(listagem)
            
            # Sobrescrevendo arquivo com dados da lista
            with open(self.arquivo, 'w', newline='') as arquivo_saida:
                escritor = csv.writer(arquivo_saida)
                escritor.writerows(lista)

        except FileNotFoundError:
            print(f'O arquivo \'{self.arquivo}\' não foi encontrado')
        except Exception as e:
            print(f'Erro inesperado: {e}')
    
    # Verificando se o email é válido
    @classmethod
    def __validar_email(cls, email_de_verificacao):
        """ 
            Verificando se o padrão do email está válido
            Args:
                - email_de_verificacao: Email para validação
        """
        
        padrao = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        # ^: Considerar tudo que está nos colchetes
        # \w: Digitos alfanumerios
        # \.: Caso haja ponto
        # -: Caso haja hifen
        # +: Concatenação
        # @: Literal (Literalmente o @)
        # $: Fim do padrão

        # Procurando um padrão no email_de_verificacao
        verif = re.match(padrao, email_de_verificacao)
        if verif:
            return True
        else:
            print(f'Email \'{email_de_verificacao}\' inválido, tente outro email!!')
            return False
    
    # Verificando se o número de telefone é válido
    @classmethod
    def __validar_telefone(cls, telefone_de_verificacao):
        """ 
            Verificando se o padrão do telefone é válido
            Args:
                - telefone_de_verificacao: Telefone para validação
        """
        padrao = r'\d{2} 9\d{8}$'
        # \d: Digitos
        # {<digito>}: Quantidade de digitos que pode ter
        # 9: Literal
        
        # Procurando um padrão no telefone_de_verificacao
        verifi = re.match(padrao, telefone_de_verificacao)
        if verifi:
            return True
        else:
            print(f'Telefone \'{telefone_de_verificacao}\' inválido, tente outro telefone')
            return False
    
    @property
    def limpar_tela(self):
        """ 
            Para limpar o terminal.
            
            Chamamos esta função como se fosse
            uma propriedade, sem abrir os parênteses
        """
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def editar(
        self,
        nome: str | None,
        numero:str | None,
        email: str | None
    ):
        contato = pd.read_csv(self.arquivo)

        print(contato) 
        
        #contato.to_csv(self.arquivo, index=False)

if __name__ == '__main__':

    bd = banco_de_dados()
    bd.limpar_tela
    contato3 = bd.adicionar('Felipe', '11 954432895', 'felipe@gmail.com')
    contato2 = bd.adicionar('Felipe', '11 912345678', 'felipe@gmail.com')
    bd.excluir('11 912345678')
    bd.editar(nome='Arin', numero='11 98745321', email='arin@gmail.com')