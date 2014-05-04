__author__ = 'jordiblanchsalgado'

from titular import Titular

class Persona(Titular):
    def __init__(self,nombre,apellido1,apellido2,nif):
        Titular.__init__(self,nombre)
        self.apellido1 = apellido1
        self.apellido2 = apellido2
        self.nif = nif
    def getNombreCompleto(self):
        return self.nombre+" "+self.apellido1+" "+self.apellido2
    def getNif(self):
        return self.nif
    #def writePersonas(self):
