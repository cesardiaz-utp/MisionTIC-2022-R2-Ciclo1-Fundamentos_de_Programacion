import tkinter as tk
from tkinter import ttk, messagebox

import controlador as ctr

ventana = None
campos = {}

def crearVentanaPrincipal():
    def prepararInteracción(ventana):
        global campos

        container = ttk.Frame(ventana, borderwidth=2, relief="raised", padding=(10,10))
        container.grid(column=0, row=0, sticky=tk.NS+tk.EW)  
        container.columnconfigure(0, weight=1)
        container.columnconfigure(1, weight=4)
        container.columnconfigure(2, weight=2)

        # Tabla
        ##################################
        tabla = ttk.Treeview(container)

        #Especificación de las columnas
        tabla['columns'] = ('ID', 'Descripción', 'Estado', 'Tiempo')
        tabla.column('#0', width=0, stretch=tk.NO)
        tabla.column('ID', anchor=tk.CENTER, width=40)
        tabla.column('Descripción', anchor=tk.W, width=300)
        tabla.column('Estado', anchor=tk.W, width=100)
        tabla.column('Tiempo', anchor=tk.CENTER, width=80)

        #Especificación del encabezado
        tabla.heading('#0', text='', anchor=tk.CENTER)
        tabla.heading('ID', text='ID', anchor=tk.CENTER)
        tabla.heading('Descripción', text='Descripción', anchor=tk.W)
        tabla.heading('Estado', text='Estado', anchor=tk.CENTER)
        tabla.heading('Tiempo', text='Tiempo', anchor=tk.CENTER)

        tabla.grid(column=0, row=0, columnspan=3) 

        def cargarTareaSeleccionada(event):
            for selected_item in tabla.selection():
                item = tabla.item(selected_item)["values"]

                #Cargar la información extraída
                entryId.delete(0,tk.END)
                entryId.insert(0,item[0])
                entryDescripcion.delete(0,tk.END)
                entryDescripcion.insert(0,item[1])
                comboboxEstado.set(item[2])
                entryTiempo.delete(0,tk.END)
                entryTiempo.insert(0,item[3])

        tabla.bind('<<TreeviewSelect>>', cargarTareaSeleccionada)

        campos["tabla"] = tabla

        # Formulario
        ##################################
        campos["id"] = tk.StringVar()
        label = ttk.Label(container, text = 'ID:')    
        entryId = ttk.Entry(container, textvariable=campos["id"])
        label.grid(column=0, row=1, sticky=tk.E, padx = 5, pady = 2)
        entryId.grid(column=1, row=1, sticky=tk.EW, padx = 5, pady = 2)  

        #Descripción Tarea
        campos["descripcion"] = tk.StringVar()
        label = ttk.Label(container, text = 'Descripción:')    
        entryDescripcion = ttk.Entry(container, textvariable=campos["descripcion"])    
        label.grid(column=0, row=2, sticky=tk.E, padx = 5, pady = 2)
        entryDescripcion.grid(column=1, row=2, sticky=tk.EW, padx = 5, pady = 2)

        #Estado Tarea
        campos["estado"] = tk.StringVar()
        label = ttk.Label(container, text = 'Estado:')    
        comboboxEstado = ttk.Combobox(container, textvariable=campos["estado"])
        comboboxEstado['values'] = ('Pendiente', 'En curso', 'Terminado')
        comboboxEstado['state'] = 'readonly'
        label.grid(column=0, row=3, sticky=tk.E, padx = 5, pady = 2)
        comboboxEstado.grid(column=1, row=3, sticky=tk.EW, padx = 5, pady = 2)

        #Tiempo Tarea
        campos["tiempo"] = tk.StringVar()
        label = ttk.Label(container, text = 'Tiempo:')    
        entryTiempo = ttk.Entry(container, textvariable=campos["tiempo"])
        label.grid(column=0, row=4, sticky=tk.E, padx = 5, pady = 2)
        entryTiempo.grid(column=1, row=4, sticky=tk.EW, padx = 5, pady = 2)

        # Acciones
        def limpiarCampos():
            if len(tabla.selection()) > 0:
                tabla.selection_remove(tabla.selection()[0])

            entryId.delete(0,tk.END)
            entryDescripcion.delete(0,tk.END)
            comboboxEstado.set(comboboxEstado["values"][0])
            entryTiempo.delete(0,tk.END)
            entryId.focus()
        
        btnLimpiarCampos = tk.Button(container, text='Limpiar Campos', command = limpiarCampos)
        btnLimpiarCampos.grid(column=2, row=0, rowspan=5, sticky=tk.S+tk.EW, padx = 5, pady = 2)

        limpiarCampos()
    
    def prepararCRUD(ventana):
        container = ttk.Frame(ventana, borderwidth=2, relief="raised", padding=(10,10))
        container.grid(column=1, row=0, rowspan=5, sticky=tk.NS+tk.EW)

        #Carga de imagen para asociar a widget tipo etiqueta    
        w = 120 
        h = 140   

        from PIL import ImageTk, Image

        imagenCargada = Image.open("tareas.png")
        imagenCargada.thumbnail((w,h))
        imagenListaTareas = ImageTk.PhotoImage(imagenCargada)
        etiquetaImagenListaTareas = tk.Label(container)
        etiquetaImagenListaTareas.config(image=imagenListaTareas, width=w, height=h)    
        etiquetaImagenListaTareas.image = imagenListaTareas
        etiquetaImagenListaTareas.grid(column=1, row=0, sticky=tk.EW, pady = 2)

        def datosFormulario():
            return {
                "id": int(campos['id'].get()),
                "descripcion": campos["descripcion"].get(),
                "estado": campos['estado'].get(),
                "tiempo": int(campos["tiempo"].get())
            }
        
        btnAdicionar = tk.Button(container, text='Adicionar Tarea', command = lambda : ctr.agregar_tarea(datosFormulario()))
        btnAdicionar.grid(column=1, row=1, sticky=tk.EW, pady = 2)
        
        btnActualizar = tk.Button(container, text='Actualizar Tarea', command = lambda : ctr.actualizar_tarea(datosFormulario()))
        btnActualizar.grid(column=1, row=2, sticky=tk.EW, pady = 2)

        btnEliminar = tk.Button(container, text='Eliminar Tarea', command = lambda : ctr.eliminar_tarea(int(campos['id'].get())))
        btnEliminar.grid(column=1, row=3, sticky=tk.EW, pady = 2)
        
        btnSalirGuardar = tk.Button(container, text='Salir y Guardar', command = salirAplicacion) 
        btnSalirGuardar.grid(column=1, row=4, sticky=tk.EW, pady = 2)

        #Etiqueta informativa funcionamiento App
        etiquetaFuncionamiento = tk.Label(container, text="-> Cargar Info antes de CRUD")
        etiquetaFuncionamiento.grid(column=1, row=5, pady = 2) 

    global ventana, campos
    
    ventana = tk.Tk()
    ventana.title('Aplicación CRUD Tareas Pendientes')
    ventana.columnconfigure(0, weight=4)
    ventana.columnconfigure(1, weight=1)

    # Creación de las interfaces
    prepararInteracción(ventana)
    prepararCRUD(ventana)

    # No se puede cambiar el tamaño de la ventana
    ventana.resizable(False, False)

    # Centrar en pantalla
    ventana.eval('tk::PlaceWindow . center')

    return ventana

def cargarTareas(tareas):
    # Eliminar los valores anteriores
    for i in campos["tabla"].get_children():
        campos["tabla"].delete(i)

    #Insertar el listado de tareas cargado en memoria proveniente de la capa de datos en la tabla
    for tarea in tareas:
        identificador = tarea['id']
        campos["tabla"].insert(parent='', index=identificador, iid=identificador, text='', 
                               values=(identificador, tarea['descripcion'], tarea['estado'], tarea['tiempo']) )

def salirAplicacion():
    valor=messagebox.askquestion("Salir","¿Deseas salir de la aplicación?")
    if valor == "yes":
        ventana.destroy()
