# Biblioteca para la gestión y persistencia de la lógica de negocio

import modelo as mdl
import vista as vst

def menu_principal():
    mdl.load_file()
    app = vst.crearVentanaPrincipal()
    vst.cargarTareas(mdl.read())
    app.mainloop()
    mdl.write_file()

def agregar_tarea(tarea):
    mdl.create(tarea)
    vst.cargarTareas(mdl.read())

def actualizar_tarea(tarea):
    mdl.update(tarea["id"], tarea)
    vst.cargarTareas(mdl.read())

def eliminar_tarea(id):
    mdl.delete(id)
    vst.cargarTareas(mdl.read())