import pandas as pd
import random as rnd
import os

class engine():
    
    def palavra_aleatoria():
        palavras_tabela = pd.Series(['Sao paulo', 'Campinas', 'Osasco', 'Pinheiros', 'Cotia'])
        return rnd.choice(palavras_tabela)
                
    
    def limparTela():
        os.system('cls' if os.name == 'nt' else 'clear')
