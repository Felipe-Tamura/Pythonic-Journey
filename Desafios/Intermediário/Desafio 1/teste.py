import numpy as np
import pandas as pd

#DATABASE
data = {'Jogos':[1, 2, 3, 4], 
    'Placar':[12, 24, 10, 24],
    'Mínimo da Temporada':[12, 12, 10, 10],
    'Máximo da Temporada':[12, 24, 24, 24],
    'Quebra recorde mín':[0, 0, 1, 1],
    'Quebra recorde max':[0, 1, 1, 1]}

df = pd.DataFrame(data)

j = input("Número de Jogos:")
p = input("Qual foi o placar?:")

mint = 0
if int(p) < 15:
    mint = p


new_row = {'Jogos':j, 'Placar': p, 'Mínimo da Temporada': mint}

df.loc[len(df)] = new_row

print(df)