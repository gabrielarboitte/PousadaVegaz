#Feito por Frank Vega e Gabriel de Sá
from Utils import *

class Quarto():
    def __init__(self, numero: int, categoria: str, diaria: float):
        self._numero = int(numero)
        self._categoria = categoria
        self._diaria = diaria
        self._consumo = []
    
    @property
    def numero(self):
        return self._numero
    @numero.setter
    def numero(self, other):
        self._numero = other
    
    @property
    def categoria(self):
        return self._categoria
    @categoria.setter
    def categoria(self, other):
        self._categoria = other    
    
    @property
    def diaria(self):
        return float(self._diaria)
    @diaria.setter
    def diaria(self, other):
        self._diaria = other
    
    @property
    def consumo(self):
        return self._consumo
    @consumo.setter
    def consumo(self, other):
        self._consumo = other

    def calcula_diaria(self, num_dias): # calculo do preço da diaria do quarto
        num_dias = int(num_dias)
        return round(num_dias * self.diaria, 2)

    def check_categoria(self):    #confere a categoria do quarto
        match self.categoria.lower():
            case "s":
                return "Standard"
            case "m":
                return "Master"
            case "p":
                return "Premium"

    def print_quarto(self): #print infos do quarto com diaria e a categoria dele
        print(f"Quarto número [{self.numero}] | Diária: {self.diaria} [{self.check_categoria()}]")
    
    def lista_consumo(self): #lista com todos itens consumidos em ordem.
        print("Lista de produtos consumidos:")
        for each in self._consumo:
            print(each)                
