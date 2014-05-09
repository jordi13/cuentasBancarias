__author__ = 'jordiblanchsalgado'
from random import randrange
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
    def genIban(self):
        iban = str(randrange(2000,2999))
        iban += " "+str(randrange(0,9999)).zfill(4)
        iban += " "+str(randrange(0, 99)).zfill(2)
        iban += " "+str(randrange(1000000000, 9999999999))
        return iban
    def creacionCuenta(self,pin,iban):
        iban = str(randrange(2000,2999))
        iban += " "+str(randrange(0,9999)).zfill(4)
        iban += " "+str(randrange(0, 99)).zfill(2)
        iban += " "+str(randrange(1000000000, 9999999999))
        with open('cuentas.txt',mode='a', encoding='utf-8')as archivo:
            archivo.write(self.titular +","+iban+","+self.moneda+","+"0"+","+pin+"\n")
        print("")
        print("Cuenta creada con éxito ")
        print("Su numero de cuenta: "+iban)
    # def consultarSaldo(self,varTitularN,intrPin):
    #     with open('cuentas.txt',mode='r',encoding='utf-8')as archivo:
    #         for linia in archivo:
    #             titularN, iban, moneda, saldo, pin= linia.split(',',4)
    #             varPin = pin.strip("\n")
    #
    #             if titularN.upper() == varTitularN.upper() and varPin == intrPin:
    #                 print(saldo,moneda)
    #                 encontrado = True
    #                 validPin = True
    #                 main.menu()
    #
    #             if intrPin==varPin:
    #                 validPin=True
    #             if titularN.upper() == varTitularN.upper():
    #                 encontrado = True
    #
    #         if encontrado == False or validPin == False:
    #             print("ERROR:")
    #         if encontrado == False and validPin == True:
    #             print("-No se ha encontrado este titular en la base de datos")
    #             #menu()
    #         if validPin == False and encontrado== True:
    #             print("-Numero pin erroneo")
    #             #menu()
    #         if validPin == False and encontrado== False:
    #             print("-No se ha encontrado este titular en la base de datos")
    #             print("-Numero pin erroneo")




