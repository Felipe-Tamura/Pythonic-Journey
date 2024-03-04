from dataclasses import dataclass
import pandas as pd
import csv
import re
import os
import time

@dataclass
class banco_de_dados:
    """ 
        Para adicionar e excluir contatos em um arquivo csv.
    """

    # Caminho do arquivo CSV
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

            # Verificando se o E-mail é valido
            valid_email = cls.__validar_email(email)

            # Verificando se o telefone é valido
            valid_tel = cls.__validar_telefone(numero)

            # Se tudo for válido nós podemos continuar
            if valid_email & valid_tel:

                # Criando o objeto para o arquivo de contatos
                tab_contato = pd.read_csv(cls.arquivo)

                # Criando um DataFrame para ser adicionado no arquivo CSV
                dado = (
                    {
                        'Nome': nome,
                        'Numero': numero,
                        'Email': email
                    }
                )

                # Iterando sobre o arquivo csv inteiro
                for lista in (tab_contato.Nome, tab_contato.Numero, tab_contato.Email):

                    # Se a lista estiver vazia nós colocamos para
                    # continuar e o loop finaliza
                    if lista.empty:
                        continue
                    # Verificando se o número já foi adicionado
                    if lista[0] == numero:
                        print(f'Número {numero} já adicionado, tente outro!')
                        break
                    # Verificando se o nome já foi adicionado
                    elif lista[0] == nome:
                        print(f'Nome {nome} já adicionado, tente outro!')
                        break
                    # Verificando se o email já foi adicionado
                    elif lista[0] == email:
                        print(f'Email {email} já adicionado, tente outro!')
                        break
                else:
                    # Adicionando o DataFrame criado na ultima linha
                    # do arquivo
                    tab_contato.loc[len(tab_contato)] = dado
                    # Reescrevendo sob o arquivo
                    tab_contato.to_csv(cls.arquivo, index=False)

        # Exceção para arquivo inexistente
        except FileNotFoundError:
            print(f'Arquivo \'{cls.arquivo}\' não encontrado')
        # Exceção para erro inesperado
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
        apagar_indice = 1
        
        try:
            # Lendo o arquivo csv
            with open(self.arquivo, 'r', newline='') as arquivo_entrada:
                leitor = csv.reader(arquivo_entrada)
                # Iterando sobre o arquivo
                for listagem in leitor:
                    # Verificando se o que o usuário quer excluir é
                    # diferente de cada linha do
                    if listagem[apagar_indice] != dado_para_excluir:
                        lista.append(listagem)
            
            # Sobreescrevendo arquivo com dados da lista
            with open(self.arquivo, 'w', newline='') as arquivo_saida:
                escritor = csv.writer(arquivo_saida)
                escritor.writerows(lista)

        # Exceção para arquivo inexistente
        except FileNotFoundError:
            print(f'O arquivo \'{self.arquivo}\' não foi encontrado')
        # Exceção para erro inesperado
        except Exception as e:
            print(f'Erro inesperado: {e}')
    
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

        # Caso o padrão do valor seja igual especificado nós
        # retornamos como verdadeiro
        if verif:
            return True
        else:
            print(f'Email \'{email_de_verificacao}\' inválido, tente outro email!!')
            return False
    
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
        # Caso o padrão seja igula o especificado nós retornamos como
        # verdadeiro
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
        paraNome: str | None,
        numero:str | None,
        paraNumero: str | None,
        email: str | None,
        paraEmail: str | None
    ):
        # Lendo o arquivo CSV
        contato = pd.read_csv(self.arquivo)

        # Verificando se o nome não está vazio
        if nome is not None:
            contato.loc[contato['Nome'] == nome, 'Nome'] = paraNome 
        # Verificando se o numero não está vazio
        if numero is not None:
            contato.loc[contato['Numero'] == numero, 'Numero'] = paraNumero
        # Verificando se o email não está vazio
        if email is not None:
            contato.loc[contato['Email'] == email, 'Email'] = paraEmail
        
        # Sobreescrevendo o arquivo
        contato.to_csv(self.arquivo, index=False)

if __name__ == '__main__':

    bd = banco_de_dados()
    bd.limpar_tela
    contato3 = bd.adicionar('Felipe', '11 954432895', 'felipe@gmail.com')
    contato2 = bd.adicionar('Arin', '11 912345678', 'arin@gmail.com')
    time.sleep(5) # Para teste de depuração, verificando se foi
                    # adicionado ou não para depois excluir o contato
    #bd.excluir('11 912345678')
    bd.editar(nome='Arin',paraNome='FelipeTamura', numero='11 98745321', paraNumero='11 9123487958', email='arin@gmail.com', paraEmail='arin.ta@gmail.com')
    bd.editar(nome='Felipe', paraNome='FelipePereira')