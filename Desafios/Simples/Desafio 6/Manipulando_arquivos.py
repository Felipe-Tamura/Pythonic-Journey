import os

os.system('cls' if os.name == 'nt' else 'clear')

arquivo = open('Desafios/Simples/main.txt', "r")

quantidade = 0
lista_de_quantidades = []
lista_de_palavras = []

for i in arquivo:
    palavras = i.split()
    for j in range(len(palavras)):
        if palavras[j] not in lista_de_palavras:
            for k in range(len(palavras)):
                if palavras[j] == palavras[k]:
                    quantidade += 1
            lista_de_quantidades.append(quantidade)
            lista_de_palavras.append(palavras[j])
            quantidade = 0

def organizando_quantidades(valores):
    
    for i in range(len(valores) -1):
        trocou = False
        for j in range(len(valores) -i -1):
            if valores[j] > valores[j + 1]:
                valores[j], valores[j + 1] = valores[j + 1], valores[j]
                trocou = True
        if not trocou:
            break
        
    return valores[-1]

numero_indice = organizando_quantidades(lista_de_quantidades.copy())
resultado_final = lista_de_palavras[lista_de_quantidades.index(numero_indice)]
print(f'A palavra/letra mais comum é:', resultado_final)
