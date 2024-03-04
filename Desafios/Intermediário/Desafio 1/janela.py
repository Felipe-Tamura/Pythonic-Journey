from dataclasses import dataclass
import tkinter as tk
from tkinter import ttk
import os
import pandas as pd
class Janela:
    """ 
        Criando uma janela onde ficará os contatos, com botões de:
            - Adicionar
            - Excluir
            - Editar
    """
    
    def __init__(self):
        # Criando a janela
        self.root = tk.Tk()
        self.label = tk.Label(self.root, text="Olá, Tkinter!")
        self.botao = tk.Button(self.root, text="Clique me!", command=self.clique_botao)
        self.botao1 = tk.Button(self.root, text="Criar uma linha", command=self.desenhar_linha)
        self.variavel_entrada = tk.StringVar() # Variável vinculada a entrada
        self.entrada = tk.Entry(self.root, text=self.variavel_entrada)
        self.canvas = tk.Canvas(self.root, width=300, height=300)
        self.menubar = tk.Menu(self.root)
        self.root.config(menu=self.menubar)
        self.file_menu = tk.Menu(self.menubar, tearoff=False)
        
        # Colocando o titulo e redimensionando a janela
        self.root.title("Contatos")
        self.root.geometry("300x300")

        # Adicioanndo um texto na janela
        self.label.pack()
        
        # Criando um botão   
        self.botao.pack()
        
        # Criando uma entrada
        self.entrada.pack()

        # Adicionando um menu de barras na janela em formato de cascata
        self.menubar.add_cascade(label="Arquivo", menu=self.file_menu)

        # Adicionando um comando no menu de barras e colocando o nome "Abrir"
        self.file_menu.add_command(label="Abrir", command=self.abrir_arquivo)

        # Adicionando mais um comando no menu de barras e colocando o nome
        # de "Salvar"
        self.file_menu.add_command(label="Salvar", command=self.salvar_arquivo)

        # Criando o botão para adicionar linha
        self.botao1.pack()

        # Criando uma janela para o canvas
        self.canvas.pack()
    
    def clique_botao(self):
        """ 
            Criando uma referência para o botão
        """
        valor = self.variavel_entrada.get()
        self.label.config(text=f'O valor da entrada é \n \'{valor}\'')
    
    def abrir_arquivo(self):
        """ 
            Comando para abrir arquivo
        """
        print("Arquivo aberto")
    
    def salvar_arquivo(Self):
        """ 
            Comando para salvar arquivo
        """
        print("Arquivo salvo")

    def desenhar_linha(self):
        """ 
            Desenhando um linha na janela
        """
        self.canvas.create_line(50, 50, 200, 200, fill="blue")

    def tela(self):
        """ 
            Iniciando o loop do TkInter para que ele inicialize uma janela
        """
        self.root.mainloop()
    
    
    def limpar_tela(self):
        """ 
            Limpando o console
        """
        os.system('cls' if os.name == 'nt' else 'clear')

if __name__ == "__main__":
    #Mostrando a janela com um loop
    tel = Janela()
    tel.limpar_tela()
    tel.tela()