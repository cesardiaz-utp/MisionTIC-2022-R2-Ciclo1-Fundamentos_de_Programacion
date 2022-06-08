import vista as vst

import turtle as t
import random

def lineaHorizontalDiscontinua(longitud=5, x=0, y=0, numeroRayas=10):
    alternador = True
    t.penup()
    t.goto(x,y)
    t.pendown()
    for _ in range(numeroRayas):
        t.goto(x + longitud, y)
        x += longitud
        if alternador:
            t.penup()
            alternador = False
        else:
            t.pendown()
            alternador = True        
    #Retornar al origen
    t.penup()
    t.goto(0,0)

def lineaDiagonalDiscontinua(longitud=5, x=0, y=0, numeroRayas=10):
    alternador = True
    t.penup()
    t.goto(x,y)
    t.pendown()
    for _ in range(numeroRayas):
        t.goto(x+longitud, y+longitud)
        x += longitud
        y += longitud
        if alternador:
            t.penup()
            alternador = False
        else:
            t.pendown()
            alternador = True        
    #Retornar al origen
    t.penup()
    t.goto(0,0)

def poligonoConvexo4LadosRelleno():
    t.begin_fill()
    t.fillcolor('cyan')
    t.goto(0,0)
    t.pendown()
    t.goto(100,50)
    t.dot(10,'blue')
    t.goto(100,-50)
    t.dot(10,'red')
    t.goto(50,-50)
    t.dot(10,'orange')
    t.goto(0,0)
    t.dot(10,'black')
    t.end_fill()

def poligonoConvexo4Lados():    
    t.goto(0,0)
    t.pendown()
    t.goto(100,50)
    t.dot(10,'blue')
    t.goto(100,-50)
    t.dot(10,'red')
    t.goto(50,-50)
    t.dot(10,'orange')
    t.goto(0,0)
    t.dot(10,'black')

def polilineaManual():
    #Polilínea (polígono que se va generando) con coordenadas ingresadas por el usuario
    t.goto(0,0)
    recogiendoCoordenadas = True
    
    relleno = input('Rellenar poli-línea? (s)').lower() == 's'
    if relleno:
        t.begin_fill()
        t.fillcolor('cyan')
    
    colores = ['blue','orange','red','black','yellow','cyan']
    while(recogiendoCoordenadas):
        x,y = vst.recogerCoordenadasTeclado()
        t.goto(x,y)
        t.dot(10, colores[ random.randint(0,len(colores)-1) ] )
        recogiendoCoordenadas = vst.controlParada()
    if relleno:
        t.end_fill()



def inicioAplicacion():
    t.setup(800,600,0,0)#Ver del área de trabajo
    t.screensize(800,600)#Área de trabajo
    t.title("Ventana Trabajo Tortuga")
    t.showturtle()

    vst.mensajeBienvenida()

    mainloop = True
    while mainloop:
        opcion = vst.formularioMenuAppTortuga()

        if opcion == 1:       
            vst.mensaje("-> Dibujado de Líneas Discontinuas")
            
            longitud = 15
            t.clear()
            lineaHorizontalDiscontinua(longitud)        
            t.clear()
            lineaDiagonalDiscontinua(longitud, -100, -100)        
            t.clear()
            lineaHorizontalDiscontinua(5, -300,numeroRayas=25)      
            
        elif opcion == 2:
            vst.mensaje("-> Dibujando Polígono Irregular de 4 Lados sin Relleno")       
            t.clear()
            poligonoConvexo4Lados()
            
        elif opcion == 3:
            vst.mensaje("-> Dibujando Polígono Irregular de 4 Lados con Relleno")       
            t.clear()
            poligonoConvexo4LadosRelleno()

        elif opcion == 4:
            vst.mensaje("-> Dibujando Poli-línea Coordenadas por Consola")        
            t.clear()
            polilineaManual()
               
        elif opcion == 5:
            vst.mensajeDespedida()
            input('Presione cualquier tecla para cerrar ventana.')
            t.bye()
            
            mainloop = False
        else:
            vst.mensaje("Opción inválida!")