#Feito por Frank Vega e Gabriel de Sá
from datetime import datetime



class Reserva():
    def __init__(self, dia_inicio, dia_fim, cliente, quarto, status):
        self._dia_inicio = dia_inicio
        self._dia_fim = dia_fim
        self._cliente = cliente
        self._quarto = int(quarto)
        self._status = status

    @property
    def dia_inicio(self):
        return self._dia_inicio
    @dia_inicio.setter
    def dia_inicio(self, other):
        self._dia_inicio = other
    
    @property
    def dia_fim(self):
        return self._dia_fim
    @dia_fim.setter
    def dia_fim(self, other):
        self._dia_fim = other 

    @property
    def cliente(self):
        return self._cliente
    @cliente.setter
    def cliente(self, other):
        self._cliente = other
    
    @property
    def quarto(self):
        return int(self._quarto)
    @quarto.setter
    def quarto(self, other):
        self._quarto = other 

    @property
    def status(self):
        return self._status
    @status.setter
    def status(self, other):
        self._status = other

    

    def serializar(self):
        serializar = [self.dia_inicio, self.dia_fim, self.cliente, self.quarto, self.status]
        return serializar
    
    def num_dias(self):
        return self.calcula_tempo(self.dia_inicio, self.dia_fim)

    def calcula_tempo(self, tempo1, tempo2):
        tempo1 = datetime.strptime(tempo1, "%d-%m-%Y")
        tempo2 = datetime.strptime(tempo2, "%d-%m-%Y")

        tempo = tempo2 - tempo1
        return tempo.days
    
    def check_status (self): #confere status do quarto
        match self.status.lower():
            case "a":
                return "aberto"
            case "c":
                return "cancelado"
            case "i":
                return "check in"
            case "o":
                return "check out"
            
    def print_info(self): #da print em todas as informações ao mesmo tempo
        print (f"Informações da reserva do quarto {self.quarto}")
        print()
        print (f"Datas: {self.dia_inicio} até dia {self.dia_fim}")
        print (f"Um total de {self.calcula_tempo(self.dia_inicio, self.dia_fim)} dias")
        print (f"O quarto está em nome de {self.cliente}")
        print (f"O quarto está no status [{self.check_status()}]")

    def print_info_curto(self): #da print sómente nas informações nescessarias
        print (f"Reserva do quarto {self.quarto} em nome de {self.cliente}")
        print (f"O quarto está no status [{self.check_status()}]")


