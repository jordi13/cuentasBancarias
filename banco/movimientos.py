__author__ = 'jordiblanchsalgado'

class Movimientos():
    def __init__(self,fecha,iban,importe,signo):
        self.fecha = fecha
        self.iban = iban
        self.importe = importe
        self.signo = signo
    def getFecha(self):
        return self.fecha
    def getIban(self):
        return self.iban
    def getImporte(self):
        return self.importe
    def getSigno(self):
        return self.signo
