import os
import csv
import json
import random

def get_path_actual(nombre_archivo):
    """
    obtiene la ruta del archivo segun el directorio actual

    Parameters:
    nombre_archivo (str): Nombre del archivo a buscar.

    Returns:
    str: Ruta completa del archivo.
    """
    directorio_actual = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(directorio_actual, nombre_archivo)

def cargar_archivo_csv(archivo):
    """
    Carga un archivo CSV y lo convierte en una lista de diccionarios.

    Parameters:
    archivo (str): Nombre del archivo CSV a cargar.

    Returns:
    list: Lista de diccionarios con los datos del archivo CSV.
    """
    bicicletas = []
    path = get_path_actual(archivo)
    if not os.path.exists(path):
        print(f"El archivo {archivo} no existe en la ruta {path}")
        return bicicletas

    with open(path, 'r', encoding='utf-8') as archivo_csv:
        lineas = archivo_csv.readline().strip().split(',')

        for linea in archivo_csv:
            valores = linea.strip().split(',')
            bicicleta = {}
            for i, linea in enumerate(lineas):
                if linea in ['id_bike', 'tiempo']:
                    bicicleta[linea] = int(valores[i])
                else:
                    bicicleta[linea] = valores[i]
            bicicletas.append(bicicleta)
    
    return bicicletas


def imprimir_lista(bicicletas):
    """
    muestra la lista de bicicletas

    Parameters:
    bicicletas (list): Lista de diccionarios con datos de bicicletas.
    """
    for bicicleta in bicicletas:
        print(f"ID: {bicicleta['id_bike']}, Nombre: {bicicleta['nombre']}, Tipo: {bicicleta['tipo']}, Tiempo: {bicicleta['tiempo']}")

def asignar_tiempos(bicicletas):
    """
    Asigna con el randint un tiempo aleatorio entre 50 y 120 minutos a cada bicicleta.

    Parameters:
    bicicletas (list): Lista de diccionarios con datos de bicicletas.

    Returns:
    list: Lista de diccionarios con los tiempos asignados.
    """
    for bicicleta in bicicletas:
        bicicleta['tiempo'] = random.randint(50, 120)
    return bicicletas

def informar_ganador(bicicletas):
    """
    informa el nombre y el tiempo del ganador
    si empatan, informa todos los nombres de las bicicletas que empataron.

    Parameters:
    bicicletas (list): Lista de diccionarios con datos de bicicletas.
    """
    if not bicicletas:
        print("No se cargaron bicicletas.")
        return

    min_tiempo = min(bicicletas, key=lambda x: x['tiempo'])['tiempo']
    ganadores = [bici for bici in bicicletas if bici['tiempo'] == min_tiempo]

    for ganador in ganadores:
        print(f"Ganador: {ganador['nombre']}, Tiempo: {ganador['tiempo']} minutos")

def filtrar_por_tipo(bicicletas, tipo_buscado):
    """
    Filtra bicicletas por tipo y guarda los resultados en un archivo.

    Parameters:
    bicicletas (list): Lista de diccionarios con datos de bicicletas.
    tipo_buscado (str): Tipo de bicicleta a filtrar.

    Returns:
    str: Nombre del archivo creado con el filtro aplicado.
    """
    bicicletas_filtradas = [bici for bici in bicicletas if bici['tipo'] == tipo_buscado]
    nombre_archivo = f"{tipo_buscado}_bicicletas"

    with open(nombre_archivo, 'w', encoding='utf-8') as archivo:
        archivo.write('id,nombre,tipo,tiempo\n')
        for bici in bicicletas_filtradas:
            linea = f"{bici['id_bike']},{bici['nombre']},{bici['tipo']},{bici['tiempo']}\n"
            archivo.write(linea)
    
    return nombre_archivo

def informar_promedio_por_tipo(bicicletas):
    """
    informa el promedio de tiempo por cada tipo de bicicleta.

    Parameters:
    bicicletas (list): Lista de diccionarios con datos de bicicletas.
    """
    if not bicicletas:
        print("No hay bicicletas para evaluar.")
        return

    tipos = set(bici['tipo'] for bici in bicicletas)
    for tipo in tipos:
        tiempos = [bici['tiempo'] for bici in bicicletas if bici['tipo'] == tipo]
        promedio = sum(tiempos) / len(tiempos)
        print(f"Promedio de tiempo para {tipo}: {promedio:.2f} minutos")

def mostrar_posiciones(bicicletas):
    """
    muestra la lista de bicicletas ordenadas por tipo y luego por tiempo ascendente.

    Parameters:
    bicicletas (list): Lista de diccionarios con datos de bicicletas.

    Returns:
    list: Lista de diccionarios ordenada.
    """
    bicicletas_ordenadas = sorted(bicicletas, key=lambda x: (x['tipo'], x['tiempo']))
    imprimir_lista(bicicletas_ordenadas)
    return bicicletas_ordenadas

def guardar_posiciones(bicicletas_ordenadas):
    """
    guarda la lista de bicicletas ordenadas en un archivo JSON.

    Parameters:
    bicicletas_ordenadas (list): Lista de diccionarios con datos de bicicletas ordenadas.
    """
    nombre_archivo = "posiciones.json"
    with open(nombre_archivo, 'w', encoding='utf-8') as archivo_json:
        json.dump(bicicletas_ordenadas, archivo_json, ensure_ascii=False, indent=4)

    print(f"Lista de posiciones guardada en {nombre_archivo}")
