from datos import todos

def generate_id() -> int:
    """ Genera el siguiente consecutivo en el almacén de datos    
    """
    ids = set(todos.keys())
    if len(ids) > 0:
        max_id = max(ids)
        return max_id + 1
    
    return 1

def create(task: dict):
    """ Adiciona un nuevo elemento al almacén de datos.
    Parámetros:
        task: Información de la tarea que se desea agregar.
    """
    id = generate_id()
    todos[id] = task

def read_all() -> list:
    """ Devuelve la lista de elementos que se encuentran en el almacén de datos.
    """
    resp = []
    # Creo una copia del valor y le agrego el id
    for key, value in todos.items():
        item = value.copy() 
        item["id"] = key
        resp.append(item)

    return resp

def read_one(id: int) -> dict:
    """ Devuelve la información del elemento que se encuentran en el almacén de datos.
    Parámetros:
        id: Número del identificador del dato a consultar.
    Retorna:
        dict: Colección con los datos del elemento consultado.
    """
    item = todos[id].copy()
    item["id"] = id
    return item

def exist(id: int) -> bool:
    """ Verifica si existe un identificador en el almacén de datos.
    Parámetros:
        id: Número del identificador del dato a consultar.
    Retorna:
        bool: Devuelve True si el id se encuentra en el almacén, de lo contrario, devuelve False.
    """
    ids = set(todos.keys())
    return id in ids
    
def update(id: int, task: dict):
    """Actualiza la información del elemento que se encuentran en el almacén de datos.
    Parámetros:
        id: Número del identificador del dato a modificar.
        task: Información de la tarea que se desea agregar en el identificador dado.
    """
    todos[id] = task

def delete(id: int):
    """Elimina la información del elemento que se encuentran en el almacén de datos.
    Parámetros:
        id: Número del identificador del dato a eliminar.
    """
    todos.pop(id)