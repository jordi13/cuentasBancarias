__author__ = 'alumne'
import re
class ComprovacioDni:
    def validacio_dni(nif):
        numeros="1234567890"
        taula_lletres="TRWAGMYFPDXBIJZSQVHLCKE"
        if (len(nif)==9):
            lletraControl=nif[8].upper()
            dni=nif[:8]
            if (len(dni)==len([n for n in dni if n in numeros])):
                if taula_lletres[int(dni)%23]==lletraControl:
                    print("Nif correcto")
                    return True
                else:
                    print("Error:Nif Introducido no es correcto")
            else:
                print("Error:Nif Introducido no es correcto")
                return False
        else:
            print("Error:Nif Introducido no es correcto")
            return False
    def validacioCif(cif):
        letraCif=cif[0].upper()
        numcif=cif[1:]
        #print (letraCif)
        #print (numcif)
        if not re.match("\d{8}", numcif):
            print ("---Error: Cif Introducido No valido---")
            return False

        if not re.match("[A-W]", letraCif):
            print ("---Error: Cif Introducido No valido---")
            return False
        else:
            return True