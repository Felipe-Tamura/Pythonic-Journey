from dataclasses import dataclass
import tkinter as tk
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
        self.root.title("Contatos")
        self.root.geometry("300x300")

        # Adicioanndo um texto na janela
        self.label = tk.Label(self.root, text="Olá, Tkinter!")
        self.label.pack()
        
        # Criando um botão   
        self.botao = tk.Button(self.root, text="Clique me!", command=self.clique_botao)
        self.botao.pack()
    
    def clique_botao(self):
        """ 
            Criando uma referência para o botão
        """
        self.label.config(text="Botão clicado!")

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