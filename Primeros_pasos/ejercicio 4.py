# Estructura For #
# ZONA CODIGO FUNCIONES #

print ("Este programa es para hacer solo sumas.")

def Ingresar_Cantidad():
    Cantidad= int(input("Digitar la cantidad de numeros que desesas sumar: "))
    return Cantidad

def Sumar_Numeros(Cantidad):
    suma=0
    for i in range (Cantidad) :
        print ("Digite el numero", str(i+1),": ")
        numero=int(input("-> "))
        suma=(suma+numero)
    return suma


def Imprimir_Numero(Total):
    print(f"La suma de los numeros igresados es: {str(Total)} \n" )
 
   
# ZONA CODIGO PRINCIPAL #
Pedir_Cantidad=Ingresar_Cantidad()
Llamar_suma=Sumar_Numeros(Pedir_Cantidad)
Imprimir=Imprimir_Numero(Llamar_suma)
print (Imprimir)