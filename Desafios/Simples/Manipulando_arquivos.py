import os

os.system('cls' if os.name == 'nt' else 'clear')

arquivo = open('Desafios/Simples/main.txt', "r")

quantidade = 0
lista_de_quantidades = []
lista_de_palavras = []

for i in arquivo:
    palavras = i.split()
    for j in range(len(palavras)):
        for k in range(len(palavras)):
            if palavras[j] == palavras[k]:
                quantidade += 1
        print(f'A palavra \'{palavras[j]}\' tem {quantidade}', 'repetições' if quantidade > 1 else 'repetição')
        lista_de_quantidades.append(quantidade)
        lista_de_palavras.append(palavras[j])
        quantidade = 0

print(lista_de_palavras)
print(lista_de_quantidades)