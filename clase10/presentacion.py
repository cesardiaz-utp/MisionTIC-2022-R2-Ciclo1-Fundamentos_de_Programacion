from logica import create, read_one, read_all, update, delete, exist

def menu_principal():
    mainloop = True

    while mainloop: 
        print(" ")
        print("-- Aplicación CRUD TareasPendientes ---")
        print("1. Listar tareas")
        print("2. Consultar una tarea")
        print("3. Adicionar Tarea")
        print("4. Actualizar Tarea")
        print("5. Eliminar Tarea")
        print("0. Salir")

        entrada = True
        while entrada:
            try:
                opcion = int(input("Ingrese una opción: "))
                if opcion in range(6):
                    entrada = False
                else:
                    print("Numero de opción inválido. Intente de nuevo.")
            except:
                print("La entrada no es válida. Intenta de nuevo.")
        
        if opcion == 1:
            listar_tareas()
        elif opcion == 2:
            consultar_tarea()
        elif opcion == 3:
            adicionar_tarea()
        elif opcion == 4:
            actualizar_tarea()
        elif opcion == 5:
            eliminar_tarea()
        elif opcion == 0:
            mainloop = False
            print("Ha salido exitosamente.")
        else:
            print("Valor inválido!")

def imprimir_titulo(mensaje: str):
    print()
    print("->", mensaje.upper())
    print("=" * 30)

def imprimir_titulo_tarea(): 
    print(f"{'Id':>3s} {'Descripción':30s} {'Estado':15s} {'Tiempo(min)'}")
    print("-" * 63)

def imprimir_tarea(tarea): 
    print(f"{tarea['id']:3d} {tarea['descripcion'].capitalize():30s} {tarea['estado'].capitalize():15s} {tarea['tiempo']:10d}")

def listar_tareas():
    imprimir_titulo("Listado de Tareas")

    tareas = read_all()
    imprimir_titulo_tarea()
    for tarea in tareas:
        imprimir_tarea(tarea)
    
    input("Presiona Enter para continuar.")

def consultar_tarea():
    imprimir_titulo("Consultar Tarea")

    #Solicitar al usuario el identificador
    id = int(input("Ingrese identificador de la Tarea para modificar: "))
   
    #Lectura de tareas
    if exist(id):
        tarea = read_one(id)
        imprimir_titulo_tarea()
        imprimir_tarea(tarea)
    else:
        print("No ha sido encontrada la Tarea!")

    input("Presiona Enter para continuar.")

def adicionar_tarea():
    imprimir_titulo("Adicionando Tarea")
    
    descripcion = input("Ingrese descripción de Tarea: ")
    estado = input("Ingrese el estado inicial de la Tarea: ")
    tiempo = int(input("Ingrese el tiempo de realización: "))
    
    tareaNueva = {
        "descripcion":descripcion,
        "estado" : estado,
        "tiempo" : tiempo
    }
    
    #Adicionar la tarea
    create(tareaNueva)

    print("Tarea agregada exitosamente!")

    input("Presiona Enter para continuar.")

def actualizar_tarea():
    imprimir_titulo("Actualizar Tarea")
    
    #Solicitar al usuario el identificador
    identificador = int(input("Ingrese identificador de la Tarea para modificar: "))     

    #Revisar si se encuentra el elemento solicitado        
    if exist(identificador):
        tarea = read_one(identificador)

        # Mostrar la información actual
        imprimir_titulo()
        imprimir_tarea(identificador, tarea)
        
        #Capturar los campos de interés
        nuevaDescripcion = input("Nueva descripción: ")
        if nuevaDescripcion:
            tarea["descripcion"] = nuevaDescripcion

        nuevoEstado = input("Nuevo estado: ")
        if nuevoEstado:
            tarea["estado"] = nuevoEstado

        nuevoTiempo = input("Nuevo tiempo: ")
        if nuevoTiempo:
            tarea["tiempo"] = int(nuevoTiempo)

        update(identificador, tarea)            

        print("Tarea modificada exitosamente!")
    else:
        print("No ha sido encontrada la Tarea!")

    input("Presiona Enter para continuar.")

def eliminar_tarea():
    imprimir_titulo("Eliminar Tarea")
    
    #Solicitar al usuario el identificador
    identificador = int(input("Ingrese identificador de la Tarea para eliminar: "))

    #Revisar si se encuentra el elemento solicitado        
    if exist(identificador):
        delete(identificador)

        print("Tarea eliminada exitosamente!")
    else:
        print("No ha sido encontrada la Tarea!")

    input("Presiona Enter para continuar.")

