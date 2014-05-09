__author__ = 'jordiblanchsalgado'


class Movimientos():
    def __init__(self, fecha, iban, importe, signo):
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

    def ingresar(self,nombre):
        with open('cuentas.txt', mode='r', encoding='utf-8')as archivo:
            contenido = ""
            contModificad = ""
            for linia in archivo:
                titular, iban, moneda, saldo, pin = linia.split(',', 4)
                pin = pin.strip("\n")
                nuevoTit = titular.upper()
                nuevoNom = nombre.upper()
                if nuevoNom != nuevoTit:
                    contenido = contenido + (nuevoTit + "," + self.iban + "," + moneda + "," + saldo + "," + pin + "\n")
                else:
                    varSaldo = int(saldo)
                    saldoAct = varSaldo + self.importe
                    contModificad = titular + "," + self.iban + "," + moneda + "," + str(saldoAct) + "," + pin + "\n"

            contTotal = contenido + contModificad

        with open('cuentas.txt', mode='w', encoding='utf-8')as archivo:
            archivo.write(contTotal)
            print("")
            print("---INGRESADO---")
            print("")


    def updateMovimientos(self):
        contMovi = str(self.fecha) + "," + str(self.iban) + "," + self.signo + "" + str(self.importe) + "\n"
        with open('movimientos.txt', mode='a', encoding='utf-8')as archivo:
            archivo.write(contMovi)
    def retirar(self,nombre):
        with open('cuentas.txt',mode='r',encoding='utf-8')as archivo:
            contenido = ""
            flag = False
            for linia in archivo:
                titular,iban,moneda,saldo, pin = linia.split(',',4)
                pin = pin.strip("\n")

                nuevoTit = titular.upper()
                nuevoNom = nombre.upper()

                if nuevoNom == nuevoTit:
                    if int(saldo) > int(self.importe):
                        saldoAct = int(saldo) - int(self.importe)
                        contModificad = titular+","+iban+","+moneda+","+str(saldoAct)+","+pin+"\n"

                    else:
                        flag = True
                        print("")
                        print("Saldo insuficiente")
                        print("")
                else:
                    contenido = contenido + (nuevoTit+","+iban+","+moneda+","+saldo+","+pin+"\n")
            contTotal = contenido+contModificad
        if flag != True:
            with open('cuentas.txt',mode='w',encoding='utf-8')as archivo:
                archivo.write(contTotal)
                print("")
                print("---RETIRADO---")
                print("")


