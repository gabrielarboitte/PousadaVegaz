#Feito por Frank Vega e Gabriel de Sá
import sys
from datetime import datetime
from os import name, system

def clear_lines(amount=1): # limpa linhas
    for _ in range(amount):
        print("\033[A", end="\033[K")

def ask_number(prompt:str="", desired_type=int, minimum=None, maximum=None): #pergunta pro usuario escolher um numero entre dois pre-determinados
    while True:
        try:
            user_input = input(prompt)
        except KeyboardInterrupt:
            print()
            raise KeyboardInterrupt
        finally:
            clear_lines()

        try:
            user_input = desired_type(user_input)
        except ValueError:
            if desired_type is int:
                print("(coloque um número valido!)", end=" ")
            else:
                print("(coloque um número valido!)", end=" ")
            continue


        if desired_type is not int:
            user_input = round(user_input, 3)


        if minimum is not None and user_input < minimum:
            print(f"(Seu número deve ser maior ou igual a {minimum}!)", end=" ")
            continue


        if maximum is not None and user_input > maximum:
            print(f"(Seu número deve ser menor ou igual a {maximum}!)", end=" ")
            continue

        return user_input  
    
def ask_boolean(prompt=""): # pergunta pro usuario escolher entre Sim ou Não, e considera Y para sim também por questão de prática. traduz para um boolean em 1 ou 2. 
    while True: 
        try:                         
            print(prompt)
            selection = input()
        except KeyboardInterrupt:     
            return
        finally:                       
            clear_lines()

        match selection.lower():
            case "y":
                clear_lines()
                return True
            case "n":
                clear_lines()
                return False
            case "s":
                clear_lines()
                return True
            case _:
                clear_lines()
                print("(Selecione somente s ou n!)", end=" ")


#def append_arquivo(nome_arq, nova_linha):
#    with open(nome_arq, "a") as file:
#        info = csv.writer(file)
#        info.writerow(nova_linha)

def ask_date(prompt): # pergunta a data no padrão dia-mês-ano e se nao for escrita corretamente não aceita o input.
    print()
    while True:
        try:
            date_input = input(prompt)
            specific_date = datetime.strptime(date_input, "%d-%m-%Y")
            clear_lines(2)
            print(f"Você escolheu: {specific_date.strftime('%d-%m-%Y')}")
            return date_input
        except ValueError:
            clear_lines(2)
            print("Data inválida, por favor somente utilize DD-MM-YYYY.")

#ask_date("test: ")

def purge():  # limpa todas as linhas
        system("cls")

def serializar(lista): #transforma var lista em string
    if isinstance(lista, (list, tuple, str)):
        serializado = ', '.join(map(str, lista))
        return serializado
    elif isinstance(lista, str):
        return lista
    else:
        return ', '.join(lista)

def escrever_arquivo(nome_arquivo, lista): # adiciona texto linha por linha
    with open(nome_arquivo,"r") as file:
        linha = file.readlines()
        linhas = []
        linhas.append(linha[0])

        for x in lista:
            texto = serializar(x)
            linhas.append(texto + "\n")

    with open(nome_arquivo, "w") as file:
        for x in linhas:
            file.write(x)

def escrever_arquivo_reserva(nome_arquivo, lista): # escreve arquivo do consumo
    with open(nome_arquivo,"r") as file:
        linha = file.readlines()
        linhas = []
        linhas.append(linha[0])

        for x in lista:
            texto = x
            linhas.append(texto + "\n")

    with open(nome_arquivo, "w") as file:
        for x in linhas:
            file.write(x)


def ask_from_list(prompt, lst): # pergunta para o usuario escolher uma opçao dentro de uma lista ex: [1, 2, 3, 4] (ai tu escolhe um numero)
    lst = [str(x) for x in lst]
    while True: 
        try:                          
            user_input = input(prompt).lower()
        except KeyboardInterrupt:      
            print()
            raise KeyboardInterrupt
        finally:                      
            clear_lines()

        try:
            selection = lst.index(user_input)
            return user_input
        except ValueError:
            print("(Por favor selecione uma opção válida)", end=" ") 



def comparar_datas (data_inicial1, data_final1, data_inicial2, data_final2): # comparar datas para ver se a data esta livre
    data_inicial1 = datetime.strptime(data_inicial1, "%d-%m-%Y")
    data_final1 = datetime.strptime(data_final1, "%d-%m-%Y")
    data_inicial2 = datetime.strptime(data_inicial2, "%d-%m-%Y")
    data_final2 = datetime.strptime(data_final2, "%d-%m-%Y")


    return max(data_inicial1, data_inicial2) <= min(data_final1, data_final2)

def comparar_inicial_final(data_inicial, data_final): #compara se a data final esta na frente da data inicial
    data_inicial = datetime.strptime(data_inicial, "%d-%m-%Y")
    data_final = datetime.strptime(data_final, "%d-%m-%Y")
    if data_final > data_inicial:
        return True
    else:
        clear_lines(2)
        print ("data final maior que data inicial")
        input ("[pressione enter para tentar de novo]")
        clear_lines()

def comparar_data_meio(data_meio, data_inicial, data_final): # compara se a data no meio esta entre as outras duas datas
    data_meio = datetime.strptime(data_meio, "%d-%m-%Y")
    data_inicial = datetime.strptime(data_inicial, "%d-%m-%Y")
    data_final = datetime.strptime(data_final, "%d-%m-%Y")

    return data_inicial <= data_meio <= data_final

def agrupar_consumo(lista):  #pega todos os itens do consumo e retorna uma lista
    data_agrupada = {}
    for x in lista:
        item1 = x[0].lower()
        item2 = x[1]
        if item1 in data_agrupada:
            data_agrupada[item1] += item2
        else:
            data_agrupada[item1] = item2[:]
    result = [[item1, list(item2)] for item1, item2 in data_agrupada.items()]
    return result
