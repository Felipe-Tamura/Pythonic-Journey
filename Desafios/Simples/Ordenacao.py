import os

os.system('cls' if os.name == 'nt' else 'clear')

def bubbleSort(lista):
    """
    Para organizar uma lista de números em ordem crescente. Se chama bubble por causa
    da "imitação" de uma bolha subindo até a superficie
    
    Args:     
    - lista: lista de números que desejamos organizar
    """
    for i in range(len(lista) -1):
        trocou = False
        for j in range(len(lista) -i -1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
                trocou = True
        if not trocou:
            break
       
    return lista

grupo = [98, 56, 4, 87, 0, 5, 77]

resultado_ordenado = bubbleSort(grupo)
print("Lista Ordenada:", resultado_ordenado)