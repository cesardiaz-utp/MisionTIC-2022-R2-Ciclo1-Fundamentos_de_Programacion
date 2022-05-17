# Arquitectura de la aplicación de ejemplo

Aunque hay aplicaciones que pueden tener muchas capas, este ejemplo solo usa las 3 principales:

- Presentación 
- Lógica del Negocio
- Acceso a Datos

![](https://vfpavanzado.files.wordpress.com/2017/12/capas011.png)

## Capa de presentación (presentacion.py)
En esta capa se encuentra todas las funciones necesarias para interactuar con el usuario, incluyendo el menu de acceso a las diferentes funcionalidades del sistema.  

Esta capa concentra todos las instrucciones **input** y **print** de toda la aplicación. 

Solo se comunica (a partir del import de biblioteca) con la capa de lógica de negocio.

Esta capa puede ser intercambiable. Se puede desarrollar diferentes funciones que usen la lógica de negocio asi no sea usando prints e inputs. Por ejemplo: una aplicación que recibe datos de otra aplicación, servicios web, etc.

En este ejemplo, encontraremos los métodos necesarios para mostrar el menú y capturar o mostrar los datos de las tareas por hacer:
- `def menu_principal()`
- `def imprimir_titulo(mensaje: str)`
- `def imprimir_titulo_tarea()`
- `def imprimir_tarea(tarea)`
- `def listar_tareas()`
- `def consultar_tarea()`
- `def adicionar_tarea()`
- `def actualizar_tarea()`
- `def eliminar_tarea()`

**Cabe resaltar** que las funciones que se crean en la _capa de presentación_, por lo general no devuelven valores. si se encuentra una función que devuelva algo, es importante revisar si hace parte de la lógica de aplicación o simplemente es una utilidad de la capa.

## Capa de lógica de negocio (logica.py)
En esta capa encontraremos la definición de las funciones necesarias para el correcto funcionamiento del sistema.

Se comunica con la capa de datos para obtener la información que le sea solicitada y le aplica la lógica (algoritmos) para realizar las operaciones solicitadas. 

En este ejemplo, encontraremos los métodos necesarios para el CRUD de las tareas por hacer:
- `def generate_id() -> int`
- `def create(task: dict)`
- `def read_all() -> list`
- `def read_one(id: int) -> dict`
- `def exist(id: int) -> bool`
- `def update(id: int, task: dict)`
- `def delete(id: int)`

**Cabe resaltar** que las funciones que se crean en la capa de _lógica de negocio_, por lo general devuelven valores. Si encontramos una función que no devuelva valor, es una señal que no debe estar en esta capa.

## Capa de acceso a datos (datos.py)
En este ejemplo sencillo, en la capa de datos solo tenemos el diccionario que nos sirve de sistema de almacenamiento en memoria.

Esta capa puede ser utilizada para acceder a diferentes sistemas de almacenamiento persistente (archivos, bases de datos, servicios web, etc)

En este ejemplo, solo encontraremos un diccionario llamado `todos` con la información inicial con la que inicia el sistema.

**Cabe resaltar** que las funciones que se crean en la capa de _acceso a datos_, por lo general devuelven valores. Si encontramos una función que no devuelva valor, es una señal que no debe estar en esta capa.

## Aplicación Principal (main.py)
Este archivo solo llama al metodo inicial que se encuentra en la capa de presentación.

Este archivo tambien se puede llamar _Launcher_ o _lanzador_