__author__ = 'jordiblanchsalgado'

class Cuenta():
    def __init__(self,iban,titular,moneda):
        self.iban = iban
        self.titular = titular
        self.moneda = moneda
    def getIban(self):
        return self.iban
    def getTitular(self):
        return self.titular
    def getMoneda(self):
        return self.moneda