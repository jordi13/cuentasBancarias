__author__ = 'jordiblanchsalgado'

#-*_ coding: UTF-8 _*_

from persona import Persona
from cuenta import Cuenta
from empresa import Empresa
from movimientos import Movimientos
import datetime


def menu():
    print("")
    print("-----> BIENVENIDO AL GEORGE NATIONAL BANK <-----")
    print("")
    print("¿Que desea hacer?")
    print(" 1-.Consultar saldo ")
    print(" 2-.Realizar un movimiento")
    print(" 3-.Salir")

eleccion = 0
eleccionMovi = 0
varNombre = ""
menu()
while eleccion != 3:
    eleccion = int(input())
    #CONSULTAR SALDO
    if eleccion == 1:
        print("Introduce bla bla (saldo)")
        print("Introduce :")
        print("1-. Cuenta de un particular")
        print("2-. Cuenta de una empresa")
        tipo = int(input())
        #PARTICULAR
        if tipo == 1:
            nombre = ""
            apellido1 = ""
            apellido2 = ""
            print("nombre y apellidos(ej: Jordi Blanch Salgado):")
            nombreCompleto = str(input())
            var = nombreCompleto.split()
            nombre = var[0]
            apellido1 = var[1]
            apellido2 = var[2]
            print("Dni/Nif:")
            dni = str(input())

            persona = Persona(nombre,apellido1,apellido2,dni)
            nombrePersona = persona.getNombreCompleto()
            nif = persona.getNif()
            print(nombrePersona,nif)
        #EMPRESA
        if tipo == 2:
            print("Razón social:")
            varNombre = str(input())
            print("Cif:")
            varCif = str(input())

            empresa = Empresa(varNombre,varCif)
            nombreEmpresa = empresa.getNombre()
            cif = empresa.getCif()
            print(nombreEmpresa,cif)

    #MOVIMIENTOS
    if eleccion == 2:
        print("Debemos identificar la cuenta:")
        print("Introduce tu nombre completo (ej: Jordi Blanch Salgado):")
        nombre = str(input())
        print("Introduce el tipo de moneda:")
        moneda = str(input())
        print("Introduce el IBAN:")
        iban = str(input())

        cuenta = Cuenta(iban,nombre,moneda)

        varIban = cuenta.getIban()
        varMoneda = cuenta.getMoneda()
        print(nombre,varIban,varMoneda)

        print("¿Que desea hacer en la cuenta ?")
        print("1-. Ingresar")
        print("2-. Retirar")
        eleccionMovi = int(input())

        #INGRESAR
        if eleccionMovi == 1:
            print("Introduzca la cantidad a ingresar:")
            importe = str(input())
            signo = "+"
            now = datetime.datetime.now()

            movimiento = Movimientos(now,varIban,importe,signo)

            fecha = movimiento.getFecha()
            iban = movimiento.getIban()
            importe = movimiento.getImporte()
            signo = movimiento.getSigno()
            print(fecha,iban,importe,signo)
        #RETIRAR
        if eleccionMovi == 2:
            print("Introduzca la cantidad a retirar:")
            importe = str(input())
            signo = "-"
            now = datetime.datetime.now()

            movimiento = Movimientos(now,varIban,importe,signo)

            fecha = movimiento.getFecha()
            iban = movimiento.getIban()
            importe = movimiento.getImporte()
            signo = movimiento.getSigno()
            print(fecha,iban,importe,signo)



    #SALIR
    if eleccion != 1 and eleccion != 2:
        print("Introduce una opcion válida")

