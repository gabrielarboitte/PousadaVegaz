#Feito por Frank Vega e Gabriel de Sá
from Utils import *
from datetime import datetime
from reserva import Reserva
from Quartos import Quarto
from produtos import Produtos


class Pousada():
    menu_pousada = '''         ╔══════════════════════════╗
         ║ Qual reserva deseja ver? ║
    ╔════╩══════════════════════════╩═══╗
    ║ 1. Pesquisar por nome do cliente  ║
    ║ 2. Pesquisar por número do quarto ║
    ║ 3. Pesquisar por data             ║
    ║                                   ║
    ║ 0. Sair                           ║
    ╚═══════════════════════════════════╝
        '''
    
    menu_produtos='''          ╔═══════════════╗
          ║   Produtos    ║
    ╔═════╩═══════════════╩════╗
    ║ 1. Água - R$ 3,00        ║
    ║ 2. Refri - R$ 5,00       ║
    ║ 3. Café - R$ 4,00        ║
    ║ 4. Chá - R$ 4,00         ║
    ║ 5. Energético - R$ 10,00 ║
    ║ 6. Cerveja - R$ 11,00    ║
    ║ 7. Vinho Lata - R$ 15,00 ║
    ║ 8. Champagne - R$ 29,70  ║
    ║                          ║
    ║ 0. Voltar                ║
    ╚══════════════════════════╝
    '''

    def __init__(self,arq1= "pousada.txt", arq2 = "reservas.txt", arq3 = "quartos.txt", arq4 = "produtos.txt", arq5 = "consumo.txt"):
        self._arq_pousada = arq1 #nome do arquivo que pousada esta chamando para info
        self._arq_reservas = arq2 #nome do arquivo que pousada esta chamando para reservas
        self._arq_quartos = arq3 #nome do arquivo que pousada esta chamando para quartos
        self._arq_items = arq4 #nome do arquivo que pousada esta chamado para os items
        self._arq_cons = arq5 #nome do arquivo que pousada esta chamado para os consumiveis
        self._nome = None
        self._contato = None
        self._quartos = []
        self._produtos = []
        self._reservas = []
        self._reservas_inativas = []
        self._consumo = []
        self.carrega_dados()


    @property
    def arq_pousada(self,):
        return self._arq_pousada
    @arq_pousada.setter
    def arq_pousada(self, other):
        self._arq_pousada = other

    @property
    def _arq_quartos(self,):
        return self.__arq_quartos
    @_arq_quartos.setter
    def _arq_quartos(self, other):
        self.__arq_quartos = other

    @property
    def arq_reservas(self,):
        return self._arq_reservas
    @arq_reservas.setter
    def arq_reservas(self, other):
        self._arq_reservas = other

    @property
    def arq_pousada(self,):
        return self._arq_pousada
    @arq_pousada.setter
    def arq_pousada(self, other):
        self._arq_pousada = other

    @property
    def _arq_quartos(self,):
        return self.__arq_quartos
    @_arq_quartos.setter
    def _arq_quartos(self, other):
        self.__arq_quartos = other

    @property
    def arq_cons(self,):
        return self._arq_cons
    @arq_cons.setter
    def arq_cons(self, other):
        self._arq_cons = other

    @property
    def nome(self):
        return self._nome
    @nome.setter
    def nome(self, other):
        self._nome = other

    @property
    def contato(self):
        return self._contato
    @contato.setter
    def contato(self, other):
        self._contato = other

    @property
    def quartos(self):
        return self._quartos
    @quartos.setter
    def quartos(self, other):
        self._quartos = other

    @property
    def produtos(self):
        return self._produtos
    @produtos.setter
    def produtos(self, other):
        self._produtos = other
    
    @property
    def reservas(self):
        return self._reservas
    @reservas.setter
    def reservas(self, other):
        self._reservas = other
    
    @property
    def reservas_inativas(self):
        return self._reservas_inativas
    @reservas_inativas.setter
    def reservas_inativas(self, other):
        self._reservas_inativas = other

    
    def carrega_dados (self): #carrega os dados dos txt para as variaveis
        with open(self._arq_pousada,"r") as file:
            content = file.read()
            info = content.splitlines()
            if len(info) > 1:
                info = info [1:]
                for x in info:
                    x = x.split(", ")
                    self._nome = x[0]
                    self._contato = x[0]
        
        with open(self._arq_reservas, "r") as file:
            vistos = []
            content = file.read()
            info = content.splitlines()
            if len(info) > 1:
                info = info [1:]
                for x in info:
                    x = x.split(", ")
                    if x[4].lower() in ["c", "o"]:
                        reserva = Reserva (x[0],x[1],x[2],x[3],x[4])
                        self._reservas_inativas.append(reserva)
                    else:
                        vistos.append(x[3])
                        reserva = Reserva (x[0],x[1],x[2],x[3],x[4])
                        self._reservas.append(reserva)
                
        with open(self._arq_quartos, "r") as file:
            content = file.read()
            info = content.splitlines()
            if len(info) > 1:
                info = info [1:]
                for x in info:
                    x = x.split(", ")
                    quartos = Quarto (x[0],x[1],x[2])
                    self._quartos.append(quartos)

        with open(self._arq_items, "r", encoding='utf-8')as file:  # encoding='utf-8' aqui para o compilador ler acentos.
            content = file.read()
            info = content.splitlines()
            if len(info) > 1:
                info = info [1:]
                for x in info:
                    x = x.split(", ")
                    produtos = Produtos (x[0],x[1],x[2])
                    self._produtos.append(produtos)

        with open(self._arq_cons, "r", encoding='utf-8')as file:              
            content = file.read()
            info = content.splitlines()
            if len(info) > 1:
                info = info [1:]
                for x in info:
                    x = x.split(', ', 1)
                    lista_consumo = x[1].split(', ')
                    consumo = (x[0],lista_consumo)
                    self._consumo.append(consumo)

    def salva_dados (self): #salva os dados no arquivo txt
        reservas = []
        for x in self._reservas:
            reservas.append(x.serializar())
        escrever_arquivo(self.arq_reservas, reservas) #serializa e coloca no arquivo linha por linha

        self.atualiza_consumo_todos() 
        consumo = []
        for x in self._consumo:
            serializado = serializar (x[1])
            final = serializar([x[0], serializado])
            consumo.append(final)
        escrever_arquivo_reserva(self.arq_cons, consumo)#serializa e coloca no arquivo linha por linha

############### as tres proximas funções que servem pra consultar reservas ###################
    def consulta_quarto(self):  #essa função pede pro usuario escolher um dos quartos
        while True:
            purge()
            print("╔═══════════╗")
            print("║  Quartos  ║")
            print("╚═══════════╝")
            print()
            temp_quartos = []
            for x in self.quartos:
                x.print_quarto()
                temp_quartos.append(str(x.numero))
            escolha = ask_from_list("Escolha qual quarto voce quer consultar: ", temp_quartos)
            print (f"\nVocê escolheu o quarto [{escolha}]")
            return escolha

    def consulta_disponibilidade(self, quarto, tempo_inicio, tempo_final): #consulta disponibilidade dos quarto escolhido no tempo escolhido
        reservas_filtradas = [x for x in self.reservas if x.quarto == int(quarto)]
        if reservas_filtradas:
            for x in reservas_filtradas:
                if comparar_datas(tempo_inicio, tempo_final, x.dia_inicio, x.dia_fim):
                    print ("Essas datas ja estão reservadas")
                    return False
            
            print ("Não há reservas desse quarto nessas datas")
            return True
        else:
            print ("Não há reservas desse quarto")
            return True
        
    def consulta_quartos_disponiveis(self, tempo_inicio, tempo_final): #consulta os quartos disponiveis no tempo escolhido
        quartos_disp = []
        quartos_disp_cls = []
        for x in self.quartos:
            quartos_disp.append(x.numero)
        for x in self.reservas:
            if x.status in ["a", "i"]:
                if comparar_datas(tempo_inicio, tempo_final, x.dia_inicio, x.dia_fim):
                    if x.quarto in quartos_disp:
                        quartos_disp.remove(x.quarto)
        for x in self.quartos:
            if x.numero in quartos_disp:
                quartos_disp_cls.append(x)
        return quartos_disp_cls, quartos_disp



    def consulta_reserva(self): #consulta status das reserva
        while True:
            purge()
            print(self.menu_pousada)
            escolha = ask_from_list("Selecione sua opção: ", ["1","2","3","0"])
            print(escolha)
            match escolha:
                case "1":
                    while True:
                        purge()
                        print("Lista de nomes registrados: ")
                        print()
                        lista = []
                        for x in self._reservas:
                            lista.append(x.cliente)

                        for x in set(lista):
                            print (x)
                        print()
                        nome = input("Digite o nome que deseja pesquisar: ")
                        purge()
                        print ("Essas são as reservas que você pesquisou:")
                        check = True
                        for x in self._reservas:
                            if x.cliente.lower() == nome.lower():
                                print("╬══════════════════════════════════════════╬")
                                x.print_info()
                                check = False
                        if check:
                            print ("\nNenhuma reserva foi encontrada.")
                            if ask_boolean("Deseja tentar de novo? [s/n]: "):
                                continue
                            else:
                                return
                        else:
                            print("╬══════════════════════════════════════════╬")
                            input("Pressione enter para voltar\n")
                            return
                    break
                case "2":
                    while True:
                        purge()
                        print("Lista de quartos com reservas: ")
                        print()
                        lista = []
                        for x in self._reservas:
                            lista.append(x.quarto)
                        for x in set(lista):
                            print(f"Quarto número [{x}]")
                        print()
                        numero = ask_number("Digite o número que deseja pesquisar: ", int)
                        purge()
                        print ("Essas são as reservas que você pesquisou:")
                        check = True
                        for x in self._reservas:
                            if x.quarto == numero:
                                print("╬══════════════════════════════════════════╬")
                                x.print_info()
                                check = False
                        if check:
                            print ("\nNenhuma reserva foi encontrada.")
                            if ask_boolean("Deseja tentar de novo? [s/n]: "):
                                continue
                            else:
                                return
                        else:
                            print("╬══════════════════════════════════════════╬")
                            input("Pressione enter para voltar\n")
                            return
                    break
                case "3":
                    while True:
                        purge()
                        data = ask_date("Digite a data que deseja pesquisar[dd-mm-yyyy]: ")
                        
                        print ("Essas são as reservas que você pesquisou:")
                        check = True
                        for x in self._reservas:
                            if comparar_data_meio(data, x.dia_inicio, x.dia_fim):
                                print("╬══════════════════════════════════════════╬")
                                x.print_info()
                                check = False
                        if check:
                            print ("\nNenhuma reserva foi encontrada.")
                            if ask_boolean("Deseja tentar de novo? [s/n]: "):
                                continue
                            else:
                                return
                        else:
                            print("╬══════════════════════════════════════════╬")
                            input("Pressione enter para voltar\n")
                            return
                    break
                case "0":
                    break
                case _:
                    print ("quê???")
                    input ("")


    def realiza_reserva(self): #realiza reserva perguntando pro usuario todas as informações
        while True:
            purge()
            print ("Você está agora realizando a reserva \n[digite 'cancelar' para cancelar]\n")
            cliente = input("Digite seu nome: ")
            if cliente == 'cancelar':
                return
            dia_inicio = ask_date("Digite a data inicial, utilize [DD-MM-YYYY]: ")
            dia_final = ask_date("Digite a data final, utilize [DD-MM-YYYY]: ")
            if comparar_inicial_final(dia_inicio, dia_final):
                clear_lines(2)
                print(f"Você escolheu as datas {dia_inicio} até {dia_final}")
                if ask_boolean("Confirmar datas? [s/n]: "):
                    pass
                else:
                    purge()
                    continue
            else:
                clear_lines(2)
                print(f"Digite uma data depois de {dia_inicio}")
            quartos_disp, numeros = self.consulta_quartos_disponiveis(dia_inicio, dia_final)
            if quartos_disp:
                print ("Quartos disponíveis nessa data:")
                for x in quartos_disp:
                    x.print_quarto()
                print (numeros)
                quarto = ask_from_list("Selecione o quarto que deseja alugar: ", numeros)
                print ("╬══════════════════════════════════════════╬")
                print ("[Informações da reserva:]")
                print (f"Reserva do cliente:{cliente}, quarto:{quarto}")
                print (f"Datas {dia_inicio} até {dia_final}")
                print ("╬══════════════════════════════════════════╬")
                if ask_boolean("Você deseja confirmar essa reserva? [s/n]: "):
                    break
            else:
                print ("Não há quartos disponíveis nessas datas :(")
                ask_boolean("deseja tentar de novo? [s/n]: ")
        reserva = Reserva(dia_inicio, dia_final, cliente, quarto, "a")
        self._reservas.append(reserva)
        
    def cancela_reserva(self): #pergunta pro usuario pesquisar uma das reservas e cancela ela
        while True:
            purge()
            print("[Você está agora cancelando uma reserva]")
            print("Lista de nomes registrados: ")
            print()
            lista = []
            for x in self._reservas:
                lista.append(x.cliente)
            for x in set(lista):
                print (x)
            print()
            nome = input("Digite o nome que deseja pesquisar: ")
            purge()
            print ("Essas são as reservas que você pesquisou:\n")
            print("╬══════════════════════════════════════════╬")
            check = True
            opções = []
            for id, x in enumerate(self._reservas):
                if x.cliente.lower() == nome.lower() and x.status in ["a"]:
                    print (f"id da reserva: [{id}]")
                    x.print_info_curto()
                    print("╬══════════════════════════════════════════╬")
                    opções.append(id)
                    check = False
            if check:
                print ("\nNenhuma reserva foi encontrada.")
                if ask_boolean("Deseja tentar de novo? [s/n]: "):
                    continue
                else:
                    return
            else:
                opções.append("voltar")
                print()
                print("Digite 'voltar' para voltar ao menu principal")
                remove = ask_from_list("Digite qual reserva deseja cancelar: ", opções)
                clear_lines(1)
                if remove == "voltar":
                    return
                if ask_boolean(f"tem certeza que deseja cancelar a reserva com id [{remove}]? [s/n]: "):
                    remove = int(remove)
                    purge()
                    self.reservas[remove].status = "c"
                    print()
                    self.reservas[remove].print_info()
                    print()
                    input("[Removido com sucesso, pressione enter para continuar]")
                    return
                else:
                    print("Nada foi cancelado")
                    input("[voltando ao menu principal, pressione enter para continuar]")
                return
            
    def realiza_check_in(self): #pergunta pro usuario pesquisar uma das reservas e faz check in nela
        while True:
                nome, remove = self.procura_reserva("[menu de check in]", ["a"])
                if remove == "voltar":
                    return
                clear_lines()
                if remove == "voltar":
                    return
                remove = int(remove)
                self.reservas[remove].print_info()
                for x in self.quartos:
                    if self.reservas[remove].quarto == x.numero:
                        valor = x.calcula_diaria(self.reservas[remove].num_dias())
                        break
                purge()
                print("╬══════════════════════════════════════════╬")
                self.reservas[remove].print_info()
                print (f"O valor será de R${valor}")
                print("╬══════════════════════════════════════════╬")
                if ask_boolean(f"Deseja fazer check-in na reserva com id [{remove}]? [s/n]: "):
                    purge()
                    self.reservas[remove].status = "i"
                    print()
                    self.reservas[remove].print_info()
                    print()
                    input("[Check-in feito com sucesso, pressione enter para continuar]")
                    return
                else:
                    print("\nNada foi feito")
                    input("[Voltando ao menu principal, pressione enter continuar]")
                    return
                
    def realiza_check_out(self): #pergunta pro usuario pesquisar uma das reservas e faz check out nela
        while True:
                nome, remove = self.procura_reserva("[menu de check out]", ["i"])
                if remove == "voltar":
                    return
                clear_lines()
                if remove == "voltar":
                    return
                remove = int(remove)
                self.reservas[remove].print_info()
                for id, x in enumerate(self.quartos):
                    if self.reservas[remove].quarto == x.numero:
                        valor = x.calcula_diaria(self.reservas[remove].num_dias())
                        break
                purge()
                print("╬══════════════════════════════════════════╬")
                self.reservas[remove].print_info()
                print (f"O valor das diárias será de R${valor}")
                self.atualiza_consumo_todos()
                print("------------------------------------------")
                id, valor_consumo = self.calcula_consumo(nome)
                print()
                
                print (f"O valor total será de R${valor + valor_consumo}")
                print("╬══════════════════════════════════════════╬")
                if ask_boolean(f"Deseja fazer check-out na reserva com id [{remove}]? [s/n]: "):
                    purge()
                    self.reservas[remove].status = "o"
                    if id:
                        self._consumo.pop(id)
                        print("Consumo removido")
                    print(f'Conta de {nome} foi paga com sucesso')
                    print()
                    self.reservas[remove].print_info()
                    print()
                    input("[Check-out feito com sucesso, pressione enter para continuar]")
                    return
                else:
                    print("\nNada foi feito")
                    input("[Voltando ao menu principal, pressione enter continuar]")
                    return
    
    def atualiza_consumo_todos(self): #agrupa todos os consumos de todos os quartos em variaveis simples.
        temp_consumo = []
        for x in self.quartos:
            if x.consumo:
                temp_consumo.append(x.consumo)
        for x in self._consumo:
            if x:
                temp_consumo.append(x)
        consumo = agrupar_consumo(temp_consumo)
        self._consumo = consumo

    def calcula_consumo(self, nome): #calcula o valor de todos os consumos da pessoa e printa
        id = None
        consumo_valor = 0
        consumo_valor = float(consumo_valor)
        for id, x in enumerate(self._consumo):
            if x[0].lower() == nome.lower():
                for y in x[1]:
                    match y:
                        case "1":
                            print(f"{self.produtos[0].preco}-----{self.produtos[0].nome}")
                            consumo_valor += self.produtos[0].preco
                        case "2":
                            print(f"{self.produtos[1].preco}-----{self.produtos[1].nome}")
                            consumo_valor += self.produtos[1].preco
                        case "3":
                            print(f"{self.produtos[2].preco}-----{self.produtos[2].nome}")
                            consumo_valor += self.produtos[2].preco
                        case "4":
                            print(f"{self.produtos[3].preco}-----{self.produtos[3].nome}")
                            consumo_valor += self.produtos[3].preco
                        case "5":
                            print(f"{self.produtos[4].preco}----{self.produtos[4].nome}")
                            consumo_valor += self.produtos[4].preco
                        case "6":
                            print(f"{self.produtos[5].preco}----{self.produtos[5].nome}")
                            consumo_valor += self.produtos[5].preco
                        case "7":
                            print(f"{self.produtos[6].preco}----{self.produtos[6].nome}")
                            consumo_valor += self.produtos[6].preco
                        case "8":
                            print(f"{self.produtos[7].preco}-----{self.produtos[7].nome}")
                            consumo_valor += self.produtos[7].preco
                        case "9":
                            print(f"{self.produtos[8].preco}-----{self.produtos[8].nome}")
                            consumo_valor += self.produtos[8].preco
                        case "10":
                            print(f"{self.produtos[9].preco}-----{self.produtos[9].nome}")
                            consumo_valor += self.produtos[9].preco
                        case "_":
                            print ("[Erro: Produto com código não registrado]")
                return id, consumo_valor
        return None, consumo_valor

    def adiciona_consumo(self): # Função para adicionar consumo por cliente da pousada, só funciona com a função de achar reserva porque tem que ser uma reserva existente
        cliente, id = self.procura_reserva("[Menu de consumo]", ["i"])
        if id == "voltar":
            return
        while True:
            purge()
            print()
            print(self.menu_produtos)
            item = ask_from_list("Qual item você deseja? ", ["1","2","3","4","5","6","7","8","0"])
            if item == "0":
                print("Compra encerrada.")
                input("[Pressione enter para continuar]")
                return
            else:
                self._consumo.append([cliente, [item]])
                print("Compra adicionada com sucesso!")
                if ask_boolean ("Deseja comprar mais alguma coisa? [S/N]"):
                    continue
                else:
                    return

    def procura_reserva(self, prompt, status): #a função mais util de todas, ela procura a reserva
        while True:
            purge()
            print(prompt)
            print("Lista de nomes registrados: ")
            print()
            lista = []
            for x in self._reservas:
                if x.status in status:
                    lista.append(x.cliente)
            for x in set(lista):
                print (x)
            print()
            nome = input("Digite o nome que deseja pesquisar: ")
            purge()
            print ("Essas são as reservas que você pesquisou:\n")
            print("╬══════════════════════════════════════════╬")
            check = True
            opções = []
            for id, x in enumerate(self._reservas):
                if x.cliente.lower() == nome.lower() and x.status in status:
                    print (f"id da reserva: [{id}]")
                    x.print_info_curto()
                    print("╬══════════════════════════════════════════╬")
                    opções.append(id)
                    check = False
            if check:
                print ("\nNenhuma reserva foi encontrada.")
                if ask_boolean("Deseja tentar de novo? [s/n]: "):
                    continue
                else:
                    return "voltar", "voltar"
            else:
                opções.append("voltar")
                print("Digite 'voltar' para voltar ao menu principal")
                choice = ask_from_list("Digite qual reserva deseja acessar: ", opções)
                return nome, choice


