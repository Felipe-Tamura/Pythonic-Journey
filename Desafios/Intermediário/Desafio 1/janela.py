import csv
import tkinter as tk
from tkinter import ttk
import os

class Janela(tk.Tk):
    """ 
        Criando uma janela onde ficará os contatos, com botões de:
            - Adicionar
            - Excluir
            - Editar
    """
    
    def __init__(self):
        # Lendo o arquivo CSV e adicionando-o em uma lista
        self.arquivo = "Desafios/Intermediário/Desafio 1/contato.csv"

        # Chamando o inicializado da classe pai para criar uma janela
        super().__init__()
        
        # Adicionando um título
        self.title("Contatos")
        
        # Colocando um espaçamento de 10 para cada canto da janela
        self.configure(padx=10, pady=10, background="#6F4E37")

        # Garantindo que o nome do cabeçalho das colunas sejam a primeira
        # linha do arquivo csv
        dados = self.ler_dado()
        
        # Criando colunas
        self.treeview = ttk.Treeview(self, columns=(dados[0]))
        self.treeview.grid(row = 0, column = 1, columnspan = 4, rowspan = 4, pady=5, padx=5)
        
        # Chamando a função para adicionar tudo nas colunas
        self.exibir_dados_lista()
        
        # Criando um botão para adicionar um novo contato
        bt_add = tk.Button(
            self,
            text="Adicionar",
            width = 10,
            height = 2,
            background = "#D27D2D",
            foreground = "#7B3F00",
            activebackground = "#E5AA70",
            activeforeground = "#7B3F00"
        )
        bt_add.grid(row = 0, column = 0, sticky=tk.S)

        # Criando um botão para excluir contato selecionado
        bt_del = tk.Button(
            self,
            text="Excluir",
            width = 10,
            height = 2,
            background = "#D27D2D",
            foreground = "#7B3F00",
            activebackground = "#E5AA70",
            activeforeground = "#7B3F00"
        )
        bt_del.grid(row = 1, column = 0)

        # Criando um botão para editar o contato selecionado
        bt_edit = tk.Button(
            self,
            text="Editar",
            width = 10,
            height = 2,
            background = "#D27D2D",
            foreground = "#7B3F00",
            activebackground = "#E5AA70",
            activeforeground = "#7B3F00"
        )
        bt_edit.grid(row = 2, column = 0, sticky=tk.N)
        

    def exibir_dados_lista(self):
        """ 
            Adicionando itens a caixa_lista e retornando a exibição
        """
        # Instanciando os dados
        dados = self.ler_dado()
        index = range(1, len(dados[0]) + 1)

        # Limpando lista antiga
        for row in self.treeview.get_children():
            self.treeview.delete(row)
                
        # Criando uma função para adicionar nome a coluna
        adicionar_nome = lambda coluna: self.treeview.heading(coluna, text=coluna)

        # Iterando/mapeando lista de colunas e adicionando nome da coluna
        list(map(adicionar_nome, dados[0]))

        # Criando uma função para adicionar novos itens a lista
        adicionar = lambda indice, item: self.treeview.insert('', tk.END, text=indice, values=item)
         
        # Iterando/Mapeando lista de dados e adicionando itens
        list(map(adicionar, index, dados[1]))

    def ler_dado(self):
        """ 
            Lendo o arquivo csv e adicionando os dados em uma lista
        """
        with open(self.arquivo, 'r') as arquivo_entrada:
            leitor = csv.reader(arquivo_entrada)
            
            # Lendo nome das colunas
            nome_coluna = next(leitor)

            # Realizando iteração e adicionando na lista
            dados = [row for row in leitor]
            
        return nome_coluna, dados
    
    def botao_adicionar():
        pass
    
    def botao_editar():
        pass
    
    def botao_excluir():
        pass

    @property
    def limpar_console(self):
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def iniciar_janela(self):
        self.mainloop()

if __name__ == "__main__":
    janela1 = Janela()
    janela1.limpar_console
    janela1.iniciar_janela()