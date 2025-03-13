#Feito por Frank Vega e Gabriel de Sá
from Utils import *
from datetime import datetime
from reserva import Reserva
from Quartos import Quarto
from produtos import Produtos
from pousada import Pousada

def print_menu(nome):
    menu_arte=f"""
╔══{'═'*len(nome)}══╗
║  {nome}  ║
╚══{'═'*len(nome)}══╝
╔═══════════════════════════════════╗
║ 1. Consultar disponibilidade      ║
║ 2. Consultar reserva              ║
║ 3. Realizar reserva               ║
║ 4. Cancelar reserva               ║
║ 5. Realizar check-in              ║
║ 6. Realizar check-out             ║
║ 7. Registrar consumo              ║
║ 8. Salvar                         ║
║                                   ║
║ 0. Sair                           ║
╚═══════════════════════════════════╝
"""
    print(menu_arte)
def menu(nome, pousada):
    running = True
    while running:
        try:
            purge()
            print_menu(nome)
            choice = ask_number("Escolha uma opção do menu: ", int, 0, 8)
            match choice:
                case 1: #função para pesquisar a disponibilidade de um quarto pelo numero e data
                    while True:
                        try:
                            numero = pousada.consulta_quarto() 
                            break
                        except:
                            return
                    while True:
                        try:
                            data_inicial = ask_date("Digite a data inicial [dd-mm-yyyy]: ")
                            data_final = ask_date("Digite a data final [dd-mm-yyyy]: ")
                            if comparar_inicial_final(data_inicial, data_final):
                                clear_lines(2)
                                print(f"Você escolheu as datas {data_inicial} até {data_final}")
                                if ask_boolean("Confirmar datas? [s/n]: "):
                                    break
                                else:
                                    clear_lines()
                            else:
                                clear_lines()
                        except:
                            return
                    pousada.consulta_disponibilidade(numero,data_inicial,data_final)
                    for x in pousada.quartos:
                        if x.numero == numero:
                            print("Quarto escolhido:")
                            x.print_quarto
                            break
                    print()
                    input("Pressione enter para continuar")
                    
                case 2:
                    #Pergunta para o usuario um nome e mostra as reservas daquele nome
                    pousada.consulta_reserva() 
                case 3:
                    #Pergunta para o usuario, nome, data inicial, data final e quarto e cria uma reserva com essas informações
                    pousada.realiza_reserva() 
                case 4:
                    #Pergunta para o usuario um nome e mostra as reservas daquele nome, e depois pede pro usuario cancelar uma delas
                    pousada.cancela_reserva() 
                case 5:
                    #Pergunta para o usuario um nome e mostra as reservas daquele nome, e depois pede pro usuario fazer check in uma delas
                    pousada.realiza_check_in() 
                case 6:
                    #Pergunta para o usuario um nome e mostra as reservas daquele nome, e depois pede pro usuario fazer check out uma delas
                    pousada.realiza_check_out() 
                case 7:
                    #Entra no menu de consumo e adiciona um item ao consumo
                    pousada.adiciona_consumo() 
                case 8:
                    pousada.salva_dados() #salva dados
                    print("dados salvos com sucesso :D")
                    input("[pressione enter para voltar ao menu inicial]")
                case 0:
                    #salva dados e fecha
                    purge()
                    pousada.salva_dados()
                    print("dados salvos com sucesso :D")
                    print("Programa fechando... até mais!")
                    input(["Pressione enter para sair"])
                    running = False
                    
                case _:
                    print("O número precisa ser entre 0 a 8!")
        except:
            main()


def main():
    pousada = Pousada()
    menu(pousada.nome, pousada)

if __name__ == "__main__":
    main()