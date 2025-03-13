#Feito por Frank Vega e Gabriel de Sá
class Produtos():
    def __init__(self,codigo: int,nome: str,preco: float):
        self.codigo = codigo
        self.nome = nome
        self.preco = float(preco)
    
    @property
    def codigo(self):
        return self._codigo
    @codigo.setter
    def codigo(self, other):
        self._codigo = other
    
    @property
    def nome(self):
        return self._nome
    @nome.setter
    def nome(self, other):
        self._nome = other
    
    @property
    def preco(self):
        return round(self._preco,2)
    @preco.setter
    def preco(self, other):
        self._preco = other

