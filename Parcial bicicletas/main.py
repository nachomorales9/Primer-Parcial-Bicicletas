from funciones import *

def mostrar_menu():
    """
    esta funcion lo que hace es mostrar el menu del programa
    """
    print("\nMenú de Opciones:")
    print("1) Cargar archivo .CSV")
    print("2) Imprimir lista")
    print("3) Asignar tiempos")
    print("4) Informar ganador")
    print("5) Filtrar por tipo")
    print("6) Informar promedio por tipo")
    print("7) Mostrar posiciones")
    print("8) Guardar posiciones")
    print("9) Salir")

def menu_principal():
    bicicletas = []
    bicicletas_ordenadas = []
    
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        match opcion:
            case '1':
                archivo = input("Ingrese el nombre del archivo CSV: ")
                bicicletas = cargar_archivo_csv(archivo)
            case '2':
                imprimir_lista(bicicletas)
            case '3':
                bicicletas = asignar_tiempos(bicicletas)
                imprimir_lista(bicicletas)
            case '4':
                informar_ganador(bicicletas)
            case '5':
                tipo_buscado = input("Ingrese el tipo de bicicleta a filtrar (BMX/PLAYERA/MTB/PASEO): ")
                nombre_archivo = filtrar_por_tipo(bicicletas, tipo_buscado)
                print(f"Archivo guardado como {nombre_archivo}")
            case '6':
                informar_promedio_por_tipo(bicicletas)
            case '7':
                bicicletas_ordenadas = mostrar_posiciones(bicicletas)
            case '8':
                guardar_posiciones(bicicletas_ordenadas)
            case '9':
                print("Saliendo del programa...")
                break
            case _:
                print("Opción no válida. Por favor, intente de nuevo.")

menu_principal()