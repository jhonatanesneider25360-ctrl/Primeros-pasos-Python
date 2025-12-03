# Estructura del While #
# IINICIO CODIGO FUNCIONES#

print("El programa dira si tu numero es par o immpar. ")

def Diigitar_Numero():
    Numero = int(input("Digite un numero: "))
    return Numero


def Comprobar_Numero(Numero):
    while Numero!=0:
        if Numero%2==0:
            Mensaje = "Par."
            return Mensaje
        elif Numero %2!= 0 :
            Mensaje = "Impar."
            return Mensaje
    else:
        Mensaje=(f"{Numero} Par")
        return Mensaje


def Imprimir_Dato(Mensaje):
    print("El numero ingresado es",  Mensaje)
    
# ZONA CODIGO PRINCIPAL #
Pedir_Numero=Diigitar_Numero()
Llamar_Comprobante=Comprobar_Numero(Pedir_Numero)
Imprimir=Imprimir_Dato(Llamar_Comprobante)
print(Imprimir)