__author__ = 'jordiblanchsalgado'

from titular import Titular

class Empresa(Titular):
    def __init__(self,nombre,cif):
        Titular.__init__(self,nombre)
        self.cif = cif
    def getNombre(self):
        return self.nombre
    def getCif(self):
        return self.cif

