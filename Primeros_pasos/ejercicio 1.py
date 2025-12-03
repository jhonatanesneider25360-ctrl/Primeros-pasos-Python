# Estructura If elif else Funciones #
# IINICIO CODIGO #

print ("Este programa dira si tu numero es positivo o neegativo")

def Digitar_Numero():
    Numero = int(input("Digite el numero: "))
    return Numero


def validar_numero(Numero):
    
    if Numero > 0:
        Mensaje = "Positivo."
        return Mensaje
    elif Numero==0:
        Mensaje = "Neutro."
        return Mensaje
    else:
        Mensaje = "Negativo."   
    return Numero


def Imprimir_Mensaje(Numero):
    print("El numero es -> " + Numero)


# ZONA CODIGO PRINCIPAL #
Pedir_Numero = Digitar_Numero()
Validar_Numero= validar_numero(Pedir_Numero)
Imprimir=Imprimir_Mensaje(Validar_Numero)
print (Imprimir)
