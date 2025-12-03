# Estructura Match #
# ZONA CODIGO FUNCIONES #

print("Este programa Seleccionara el mes segun el numero dado.")

def Dar_opciones():
    print ("opciones:\n 1. Enero.\n 2. Febrero.\n 3. Marzo.\n 4. Abril.\n 5. Mayo.\n 6. Junio.\n 7. Julio.\n 8. Agosto.\n 9. Octubre.\n 10. Septiembre.\n 11. Noviembre.\n 12. Diciembre.\n ")


def Pedir_num_segun_mes(Opcion):
    Opcion_dada= int(input("Digite el numero segun el mes que eligiras: "))
    return Opcion_dada



def numero_correspondiente(Opcion_dada):
    match Opcion_dada:
        
        case 1:
           return "Enero"
        case 2:
            return "Febrero"
        case 3:
            return "Marzo"
        case 4:
            return "Abril"
        case 5:
            return "Mayo"
        case 6:
            return "Junio"
        case 7:
            return "Julio"
        case 8:
            return "Agosto"
        case 9:
            return "Septiembre"
        case 10:
            return "Octubre"
        case 11:
            return "Noviembre"
        case 12:
            return "Diciembre"
    return Opcion_dada
        
def Imprimir_mes(dato_mes):
    print("El nombre de tu mes segun el numero que selecionaste es: " + str(dato_mes))
    
    
# ZONA CODIGO PRINCIPAL #
Entregar_opciones=Dar_opciones()
Llamar_num_segun_mes=Pedir_num_segun_mes(Entregar_opciones)
Llamar_num_corresondiente=numero_correspondiente(Llamar_num_segun_mes)
Imprimir=Imprimir_mes(Llamar_num_corresondiente)
print(Imprimir)