from dataclasses import dataclass
import tkinter as tk
import os
import pandas as pd

@dataclass
class Janela:
    
    #Criando a janela
    janela = tk.Tk()
    janela.configure(padx=8, pady=10)
    janela.title("Teste")

    lb = tk.Listbox(janela, height=5)
    #Fazer um loop aqui para adicionar itens da listagem na listbox
    #_*50
    
     
    lb.grid()
    
    def tela(self):
        self.janela.mainloop()
    
    def limpar_tela(self):
        os.system('cls' if os.name == 'nt' else 'clear')

if __name__ == "__main__":
    #Mostrando a janela com um loop
    tel = Janela()
    tel.limpar_tela()
    tel.tela()