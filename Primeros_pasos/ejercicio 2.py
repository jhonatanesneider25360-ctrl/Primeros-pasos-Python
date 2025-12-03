# Estructura de Do-While #
# IINICIO CODIGO FUNCIONES#

print ("Interactua con el programa")
def capturar_letras():
    while True:
        print("Digite la letra A para Actualziar Sistema")
        print("Digite la letra E para Eliminar Catalogo")
        print("Digite la letra C para Crear Productos")
        print("Digite la letra S para salir del programa")
        letra=str(input("Seleccione una opción: "))
        return letra
A=("Actualizando.. ")
E=("Eliminando Catalogo.. ")
C=("Creando Productos.. ")
S=("saliendo.. ")

def validar_letra(letra):
    if letra== "A" or letra== "a" :
        mensaje = ( A, " Programa Actualizado.")
        return mensaje
    elif letra== "E" or letra== "e":
        mensaje = ( E, " Catalogo Eliminado.")
        return mensaje
    elif letra== "C" or letra== "c":
        mensaje = ( C, " Producto Creado.")
        return mensaje
    elif letra== "S" or letra== "s":
        mensaje= ( S, " El pograma a finalizado. ")
        return mensaje
    else:
        print("sigue dentro del proceso del DO-WHILE")
        
        
def imprimir_mensaje(mensaje):
    print("Estás ",  mensaje)
    
    
# ZONA CODIGO PRINCIPAL #
dato_letra = capturar_letras()
dato_mensaje = validar_letra(dato_letra)
imprimir=imprimir_mensaje(dato_mensaje)
print(imprimir)
