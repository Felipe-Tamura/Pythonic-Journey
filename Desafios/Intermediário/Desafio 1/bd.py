import csv
from dataclasses import dataclass


@dataclass
class banco_de_dados:
    arquivo = 'Pythonic-Journey/Desafios/Intermediário/Desafio 1/contato.csv'

    def adicionar(self, dado):
        with open(self.arquivo, 'w', newline='') as arquivo_saida:
            escrever = csv.writer(arquivo_saida)
            escrever.writerows(dado)

    def excluir(self, dado_para_excluir):
        lista = []
        with open(self.aqruivo, 'r', newline='') as arquivo_entrada:
            leitor = csv.reader(arquivo_entrada)
            for item in leitor:
                if item != dado_para_excluir:
                    lista.append(item)
        
        with open(self.arquivo, 'w', newline='') as arquivo_saida:
            escritor = csv.writer(arquivo_saida)
            escritor.writerows(lista)