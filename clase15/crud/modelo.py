# Biblioteca para la gestión y persistencia de las tareas

import json

__tareas = []

def create(tarea: dict) -> dict:
    """ Crea una nueva tarea en el sistema
    Parámetros:
    -----------
        tarea (dict): Tarea con la información a guardar
    Retorna:
    -----------
        dict: Tarea guardado en lista con el consecutivo
    """
    tarea["id"] = generar_consecutivo()
    __tareas.append(tarea)
    return tarea

def read(id: int = None) -> dict or list:
    """ Consulta las tareas que existen en el sistema
    Parámetros:
    -----------
        id (int) [Opcional]: Identificación de la tarea a consultar. Por defecto, el valor es None.
    Retorna:
    -----------
        dict: Tarea que coincide con el 'id' enviado.
        list: Tarea guardado en lista con el consecutivo
    """
    resultado = obtener_tarea(id) if id != None else __tareas
    return resultado

def update(id: int, tarea_actualizada: dict) -> dict :
    """ Actualiza una tarea existente en el sistema
    Parámetros:
    -----------
        id (int): Identificación de la tarea a consultar.
        tarea_actualizada (dict): Tarea con la información a guardar
    Retorna:
    -----------
        dict: Tarea actualizada en lista
    """
    tarea = obtener_tarea(id)
    __tareas.remove(tarea)

    for id_campo, campo in tarea_actualizada.items():
        if campo:
            tarea[id_campo] = campo

    __tareas.append(tarea)
    __tareas.sort(key=(lambda x: x["id"]))
    return tarea

def delete(id: int) -> dict:
    """ Elimina una tarea existente en el sistema
    Parámetros:
    -----------
        id (int): Identificación de la tarea a eliminar.
    Retorna:
    -----------
        dict: Tarea que coincide con el 'id' enviado.
    """
    tarea = obtener_tarea(id)
    __tareas.remove(tarea)
    return tarea

def generar_consecutivo() -> int:
    """ Genera el consecutivo para persistir la tarea
    Retorna:
    -----------
        int: Número a usar para registrar una nueva tarea.
    """
    new_id = 1 if len(__tareas) == 0 else (max([tarea["id"] for tarea in __tareas]) + 1)
    return new_id

def obtener_tarea(id: int) -> dict or list:
    """ Consulta las tareas existentes que tengan el 'id' dado
    Parámetros:
    -----------
        id (int): Identificación de la tarea a consultar.
    Retorna:
    -----------
        dict: Tarea que coincide con el 'id' enviado.
        list: En caso que existen varias tareas con el mismo 'id'
    Lanza:
    -----------
        Exception: Excepción lanzada si ocurre un error en el proceso
    """
    lista_tareas = list(filter(lambda x : x["id"] == id, __tareas))

    if len(lista_tareas) == 0:
        raise Exception(f"Error al consultar la tarea '{id}'. Tarea no existe.")
            
    tarea = lista_tareas[0] if len(lista_tareas) == 1 else lista_tareas

    return tarea

def load_file(ruta_archivo: str = "tareas.json"):
    """ Carga la información del archivo
    Parámetros:
    -----------
        ruta_archivo (str): Nombre del archivo a leer
    Lanza:
    -----------
        Exception: Excepción lanzada si ocurre un error en el proceso
    """
    try:
        global __tareas    
        with open(ruta_archivo) as archivo:
            __tareas = json.load(archivo)
    except:
        with open(ruta_archivo, "w") as archivo:
            json.dump([], archivo)

def write_file(ruta_archivo: str = "tareas.json"):
    """ Guarda las tareas gestionadas en un archivo
    Parámetros:
    -----------
        ruta_archivo (str): Nombre del archivo a escribir
    Lanza:
    -----------
        Exception: Excepción lanzada si ocurre un error en el proceso
    """
    try:
        with open(ruta_archivo, 'w') as archivo_json:
            json.dump(__tareas, archivo_json, indent=2)
    except:
        raise Exception("No se pudo guardar la información en la capa de datos.")