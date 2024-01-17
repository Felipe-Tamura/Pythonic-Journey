lista_de_palavras = ['Sao Paulo']

for i in lista_de_palavras[0]:
    texto = 'a'
    print(('_' if i != texto else texto) * len(i.split()), end=' ' if i != ' ' else '* ')
    
    # if texto == i:
    #     print('_' * len(i) + texto, end=' ')