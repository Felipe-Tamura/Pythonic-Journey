import csv
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import os
import cores
import bd


class Janela(tk.Tk):
    """ 
        Criando uma janela onde ficará os contatos, com botões de:
            - Adicionar
            - Excluir
            - Editar
    """
    
    def __init__(self):
        # Lendo o arquivo CSV e adicionando-o em uma lista
        self.arquivo = "Desafios/Intermediário/Desafio 1/contato.csv"

        # Chamando o inicializado da classe pai para criar uma janela
        super().__init__()
        
        # Adicionando um título
        self.title("Contatos")
        
        # Colocando um espaçamento de 10 para cada canto da janela
        self.configure(padx=10, pady=10, background=cores.fundo_janela)

        # Criando um frame (cena dentro da janela) para a direita
        self.cena_direita = tk.Frame(self, bg=cores.fundo_cena)
        self.cena_direita.grid(row = 0, column = 1, padx = 5)

        # Criando um frame (cena dentro da janela) para a esquerda
        self.cena_esquerda = tk.Frame(self, bg=cores.fundo_cena, padx = 5, pady = 5)
        self.cena_esquerda.grid(row = 0, column = 0, padx = 5)
        
        # Garantindo que o nome do cabeçalho das colunas sejam a primeira
        # linha do arquivo csv
        dados = self.ler_dado()
        
        # Criando colunas
        self.treeview = ttk.Treeview(self.cena_direita, columns=(dados[0]), height = 12, show="headings")
        self.treeview.grid(row = 0, column = 1, columnspan = 4, rowspan = 4, pady=5, padx=5)
        
        # Chamando a função para adicionar tudo nas colunas
        self.exibir_dados_lista()
        
        # Criando um botão para adicionar um novo contato
        bt_add = tk.Button(
            self.cena_esquerda,
            text = "Adicionar",
            command = self.botao_adicionar,
            width = 10,
            height = 2,
            background = cores.fundo_botao,
            foreground = cores.fonte_botao,
            activebackground = cores.fundo_botao_click, # referente a quando clicamos no botão
            activeforeground = cores.fonte_botao_click # referente a quando clicamos no botão
        )
        bt_add.grid(row = 0, column = 0, sticky=tk.S, pady = 5)

        # Criando um botão para excluir contato selecionado
        bt_del = tk.Button(
            self.cena_esquerda,
            text = "Excluir",
            command = self.botao_excluir,
            width = 10,
            height = 2,
            background = cores.fundo_botao,
            foreground = cores.fonte_botao,
            activebackground = cores.fundo_botao_click, # Referente a quando clicamos no botão
            activeforeground = cores.fonte_botao_click # Referente a quando clicamos no botão
        )
        bt_del.grid(row = 1, column = 0, pady = 5)

        # Criando um botão para editar o contato selecionado
        bt_edit = tk.Button(
            self.cena_esquerda,
            text = "Editar",
            command = self.botao_editar,
            width = 10,
            height = 2,
            background = cores.fundo_botao,
            foreground = cores.fonte_botao,
            activebackground = cores.fundo_botao_click, # Referente a quando clicamos no botão
            activeforeground = cores.fonte_botao_click # Referente a quando clicamos no botão
        )
        bt_edit.grid(row = 2, column = 0, sticky=tk.N, pady = 5)

    def exibir_dados_lista(self):
        """ 
            Adicionando itens a caixa_lista e retornando a exibição
        """
        # Instanciando os dados
        dados = self.ler_dado()

        # Limpando lista antiga
        for row in self.treeview.get_children():
            self.treeview.delete(row)
        
        # Criando uma função para adicionar nome a coluna
        adicionar_nome = lambda coluna: self.treeview.heading(coluna, text=coluna)
        tamanho_coluna = lambda width_coluna: self.treeview.column(width_coluna, width = 150)

        # Iterando/mapeando lista de colunas e adicionando nome da coluna
        list(map(adicionar_nome, dados[0]))
        list(map(tamanho_coluna, dados[0]))

        # Criando uma função para adicionar novos itens a lista
        adicionar = lambda item: self.treeview.insert('', tk.END, values=item)
         
        # Iterando/Mapeando lista de dados e adicionando itens
        list(map(adicionar, dados[1]))

    def ler_dado(self):
        """ 
            Lendo o arquivo csv e adicionando os dados em uma lista
        """
        # Lendo arquivo
        with open(self.arquivo, 'r') as arquivo_entrada:
            leitor = csv.reader(arquivo_entrada)
            
            # Lendo nome das colunas
            nome_coluna = next(leitor)

            # Realizando iteração e adicionando na lista
            dados = [row for row in leitor]
            
        # Retornando tudo em uma tupla
        return nome_coluna, dados
    
    def botao_adicionar(self):
        """ 
            Este comando faz com que adicione um novo contato no arquivo
            csv para ser exibido na janela de contatos.
            Ele irá abrir uma janela de formulário com dois botões e
            3 caixas de entrada. O botão irá chamar a função do arquivo
            bd onde adiciona definitivo o contato no arquivo.
        """
        # Criando uma nova janela de formuário
        forms = tk.Toplevel(self, padx = 10, pady = 10, bg = cores.fundo_janela)
        # Focando na janela do formulário
        forms.transient(self)
        # Colocando um titulo
        forms.title("Adicionar Novo Contato")

        # Criando 2 frames para o formulário
        frame_forms_cima = tk.Frame(forms, bg = cores.fundo_cena, pady = 5, padx = 5)
        frame_forms_baixo = tk.Frame(forms, bg = cores.fundo_cena, pady = 5, padx = 5)
        frame_forms_cima.grid(row = 0, column = 0, pady = 5, padx = 5)
        frame_forms_baixo.grid(row = 1, column = 0, pady = 5, padx = 5)

        # Criando 3 rotulos com informação sobre o que colocar na entrada
        rl_nome = tk.Label(frame_forms_cima, text="Nome:", bg = cores.fundo_cena, foreground = cores.fonte_rotulo)
        rl_numero = tk.Label(frame_forms_cima, text="Número:", bg = cores.fundo_cena, foreground = cores.fonte_rotulo)
        rl_email = tk.Label(frame_forms_cima, text="Email:", bg = cores.fundo_cena, foreground = cores.fonte_rotulo)
        # Adicionando na grade
        rl_nome.grid(row = 0, column = 0, sticky = tk.E)
        rl_numero.grid(row = 1, column = 0, sticky = tk.E)
        rl_email.grid(row = 2, column = 0, sticky = tk.E)

        # Criando 3 entradas para o formulário
        ent_nome = tk.Entry(frame_forms_cima, width = 30)
        ent_numero = tk.Entry(frame_forms_cima, width = 30)
        ent_email = tk.Entry(frame_forms_cima, width = 30)
        # Adicionando na grade
        ent_nome.grid(row = 0, column = 1, columnspan = 2)
        ent_numero.grid(row = 1, column = 1, columnspan = 2)
        ent_email.grid(row = 2, column = 1, columnspan = 2)

        # Função para fechar a janela do formulário
        def forms_cancel(): forms.destroy()

        def forms_add():
            """ 
                Adicionando o contato na lista com base nas informações
                do formulário
            """
            # Colocando os dados do formulário em uma lista
            preenchimento = [ent_nome.get(), ent_numero.get(), ent_email.get()]

            # Criando uma função para verificar se os itens da lista
            # estão preenchidos
            vazio = lambda valor: valor != ''

            # Fazendo uma iteração nos itens da lista usando a função "vazio"
            verificar = list(filter(vazio, preenchimento))

            if len(verificar) == 3: # Caso o formulário estiver preenchido

                # Instanciando o bd
                banco_dados = bd.banco_de_dados()

                # Adicionando cada item do formulário no arquivo
                banco_dados.adicionar(
                    nome = ent_nome.get(),
                    numero = ent_numero.get(),
                    email = ent_email.get()
                )

                # Atualizando a janela
                self.exibir_dados_lista()

                # Fechando o formulário
                forms.destroy()
                
            else:
                messagebox.showinfo(title = "AVISO!", message = "Favor preencher todos os campos")
            

        # Criando 2 botões, um de cancelar e outro de adicionar
        bt_forms_add = tk.Button(
            frame_forms_baixo,
            text="Criar Contato",
            command = forms_add,
            width = 10,
            background = cores.fundo_botao,
            foreground = cores.fonte_botao,
            activebackground = cores.fundo_botao_click, # Referente a quando clicamos no botão
            activeforeground = cores.fonte_botao_click # Referente a quando clicamos no botão
        )
        bt_forms_cancel = tk.Button(
            frame_forms_baixo,
            text="Cancelar",
            command=forms_cancel,
            width = 10,
            background = cores.fundo_botao,
            foreground = cores.fonte_botao,
            activebackground = cores.fundo_botao_click, # Referente a quando clicamos no botão
            activeforeground = cores.fonte_botao_click# Referente a quando clicamos no botão
        )
        bt_forms_add.grid(row = 3, column = 1, sticky = tk.E, padx = 2)
        bt_forms_cancel.grid(row = 3, column = 2, sticky = tk.W, padx = 2)

        
        # Iniciando a janela do formulário
        forms.mainloop()
    
    def botao_editar(self):
        """ 
            Por enquanto usando para depuração
        """
        selecao = self.treeview.selection()[0]
        filho = self.treeview.get_children()[0]
        print(
            selecao,
            filho
        )
    
    def botao_excluir(self):
        """ 
            Esta função deleta o contato do arquivo ao selecionar o
            contato da lista
        """
        try:
            # Instanciando a classe de banco de dados
            banco_dados = bd.banco_de_dados()
            
            # Pegando o ID do item selecionado na lista
            selecao = self.treeview.selection()[0]
            print(selecao)
            # Excluindo o item do arquivo usando a função do banco de dados
            banco_dados.excluir(self.ler_dado()[1][int(selecao[3]) - 1][1])
            
            # 1. Aqui estamos selecionando o segundo item da tupla: [1]
            # 2. Selecionando o item da lista dentro da tupla selecionada
            # logo de primeira: [int(selecao[3]) - 1] (Colocamos o -1
            # pois esta parte estamos retornando um número fora da lista)
            # 3. Por fim selecionamos a coluna do número para exclui-lo: [1]

        except Exception as x:

            print(selecao)
            print(f"Erro inesperado: {x}")

    @property
    def limpar_console(self):
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def iniciar_janela(self):
        self.mainloop()

if __name__ == "__main__":
    janela1 = Janela()
    janela1.limpar_console
    janela1.iniciar_janela()