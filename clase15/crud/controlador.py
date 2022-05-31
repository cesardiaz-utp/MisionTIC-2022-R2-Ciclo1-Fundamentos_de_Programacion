# Biblioteca para la gestión y persistencia de la lógica de negocio

import modelo as mdl
import vista as vst

def menu_principal():
    mdl.load_file()
    try: 
        mainloop = True
        while mainloop: 
            opcion = vst.opcion_menu_principal()

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
                vst.mostrar_mensaje("Ha salido exitosamente.")
            else:
                vst.mostrar_mensaje("Valor inválido!")
    except Exception as e:
        vst.mostrar_error(e)
        
    mdl.write_file()

def listar_tareas():
    vst.mostrar_titulo("-> Listado de Tareas")

    tareas = mdl.read()
    vst.imprimir_titulo_tarea()
    for tarea in tareas:
        vst.imprimir_tarea(tarea)
    
    vst.espera_enter()

def consultar_tarea():
    vst.mostrar_titulo("-> Consultar Tarea")

    try:
        id = vst.leer_entero("Ingrese identificador de la tarea: ")
        tarea = mdl.read(id)
        vst.imprimir_titulo_tarea()
        vst.imprimir_tarea(tarea)
    except Exception as e:
        vst.mostrar_error(e)
   
    vst.espera_enter()

def adicionar_tarea():
    vst.mostrar_titulo("-> Adicionando Tarea")        
    
    descripcion = vst.leer_cadena("Ingrese descripción de Tarea: ")
    estado = vst.leer_cadena("Ingrese el estado inicial de la Tarea: ")
    tiempo = vst.leer_entero("Ingrese el tiempo de realización: ")
    
    tarea = {
        "descripcion":descripcion,
        "estado" : estado,
        "tiempo" : tiempo
    }
    mdl.create(tarea)

    vst.mostrar_mensaje("Tarea agregada exitosamente!")

    vst.espera_enter()

def actualizar_tarea():
    vst.mostrar_titulo("-> Actualizar Tarea")
    
    id = vst.leer_entero("Ingrese identificador de la tarea: ")   

    try:
        tarea = mdl.read(id)
        vst.imprimir_titulo_tarea()
        vst.imprimir_tarea(tarea)

        tarea_actualizada = dict()

        nuevaDescripcion = vst.leer_cadena("Nueva descripción: ")
        if nuevaDescripcion:
            tarea_actualizada["descripcion"] = nuevaDescripcion

        nuevoEstado = vst.leer_cadena("Nuevo estado: ")
        if nuevoEstado:
            tarea_actualizada["estado"] = nuevoEstado

        nuevoTiempo = vst.leer_entero("Nuevo tiempo: ", opcional = True)
        if nuevoTiempo:
            tarea_actualizada["tiempo"] = nuevoTiempo

        mdl.update(id, tarea_actualizada)      

        vst.mostrar_mensaje("Tarea modificada exitosamente!")
    except Exception as e:
        vst.mostrar_error(e)

    vst.espera_enter()

def eliminar_tarea():
    vst.mostrar_titulo("-> Eliminar Tarea")
    
    try:
        id = vst.leer_entero("Ingrese identificador de la Tarea para eliminar: ")
        mdl.delete(id)
        vst.mostrar_mensaje("Tarea eliminada exitosamente!")
    except Exception as e:
        vst.mostrar_error(e)
    
    vst.espera_enter()