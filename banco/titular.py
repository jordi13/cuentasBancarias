__author__ = 'jordiblanchsalgado'

class Titular:
    def __init__(self,varNombre):
        self.nombre = varNombre
    def escribirTitular(self,nombrePersona,nif,pin):
        with open('titulares.txt', mode='a', encoding='utf-8')as archivo:
            archivo.write(nombrePersona+","+nif+","+pin+"\n")