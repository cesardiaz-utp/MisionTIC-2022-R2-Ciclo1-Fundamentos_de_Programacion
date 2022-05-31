def mostrar_titulo(titulo):
    print()
    print(titulo.upper())
    print("=" * 30)

def mostrar_mensaje(mensaje=''):
    print()
    print(mensaje)
    print()

def mostrar_error(mensaje=''):
    print()
    print("Ha ocurrido un problema:", mensaje)
    print()

def espera_enter():
    leer_cadena("Presiona Enter para continuar.")

def leer_cadena(mensaje="Ingrese un valor: "):
    return input(mensaje)

def leer_entero(mensaje="Ingrese un valor: ", opcional = False):
    valor = None
    if not opcional:
        while valor == None:
            try:
                valor = int(input(mensaje))
            except:        
                print("Entrada inválida: Se debe ingresar una opción numérica.") 
    else:
        try:
            valor = int(input(mensaje))
        except:
            valor = None

    return valor

def imprimir_titulo_tarea(): 
    print(f"{'Id':>3s} {'Descripción':40s} {'Estado':15s} {'Tiempo(min)'}")
    print("-" * 73)

def imprimir_tarea(tarea: dict): 
    print(f"{tarea['id']:3d} {tarea['descripcion'].capitalize():40s} {tarea['estado'].capitalize():15s} {tarea['tiempo']:10d}")

def opcion_menu_principal():
    print(" ")
    print("-- Aplicación CRUD Tareas Pendientes ---")
    print("1. Listar tareas")
    print("2. Consultar una tarea")
    print("3. Adicionar tarea")
    print("4. Actualizar tarea")
    print("5. Eliminar tarea")
    print("0. Salir")

    valor = None
    while valor == None:
        valor = leer_entero("Ingrese una opción: ")
        if valor not in range(6):
            print("Numero de opción inválido. Intente de nuevo.")
            valor = None

    return valor