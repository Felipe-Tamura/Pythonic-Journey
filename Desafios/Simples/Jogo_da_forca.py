lista_de_palavras = ['Sao Paulo']

texto = ['u']
texto.append('a')

for i in lista_de_palavras[0]:
    print(('_' if i != texto[1] else texto[1]) * len(i.split()), end=' ' if i != ' ' else '* ')
    