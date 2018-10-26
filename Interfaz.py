

import tkinter as tk
from Controlador import Controlador
from PIL import Image, ImageTk
import time


class Interfaz:
    
    """
    Constructor de la interfaz gráfica
    @param principal, es el root para crear la interfaz
    Especificaciones de los objetos de la interfaz gráfica:
    bg especifica el color de fondo de un objeto
    fg especifica el color del texto de un objeto
    text especifica el texto que se muestra en un objeto
    font especifica el tipo y tamaño de letra del texto de un objeto
    """
    def __init__(self,principal):
        
        #Se asigna el root
        self.principal = principal
        #Se le da un título a la ventana principal
        principal.title("Algoritmo Kmedias")
        #Dimensiones de la ventana principal
        principal.geometry("960x600+250+80")
        
        
        """Fondo""" 
        
        self.Fondo = tk.Label(principal, bg="grey", width=200,height=100).place(x = -3, y = -2)
        self.Titulo= tk.Label(principal, bg="red", fg="white", text="Algoritmo Kmedias", font="Verdana 20").place(x = 350, y = 20)
        
        """Entradas"""
        
        #Label, input y entry para la cantidad de datos
        self.LabelA1 = tk.Label(principal, bg="black", fg="white", text="# Datos:", font="Verdana 14").place(x=260,y=120) 
        self.datos = tk.StringVar()
        self.EntryDatos = tk.Entry(principal, bg="black", fg="white", font = "Verdana 12", textvariable=self.datos).place(x = 410, y = 123)
        
        #Label, input y entry para la cantidad de iteraciones
        self.LabelA2 = tk.Label(principal, bg="black", fg="white", text="Iteraciones:", font="Verdana 14").place(x=260,y=162)
        self.iteraciones = tk.StringVar()
        self.EntryIteraciones = tk.Entry(principal, bg="black", fg="white", font = "Verdana 12", textvariable=self.iteraciones).place(x = 410, y = 166)
        
        #Label, input y entry para la cantidad de clases
        self.LabelA3 = tk.Label(principal, bg="black", fg="white", text="# Clases:", font="Verdana 14").place(x=260,y=202)
        self.clases = tk.StringVar()
        self.EntryClases = tk.Entry(principal, bg="black", fg="white", font = "Verdana 12", textvariable=self.clases).place(x = 410, y = 209)

        
        """Clase 1 """
        
        #Label para clase 1
        self.LabelB1 = tk.Label(principal, bg="red", fg="white",text="Clase 1:" ,font="Verdana 14").place(x=160,y=300)
        
        #Label, input y entry para eje X de centroide en K = 1
        self.LabelB2 = tk.Label(principal, bg="black", fg="white",text="Centroide 1:" ,font="Verdana 14").place(x=15,y=360)
        self.centroide1X = tk.StringVar()
        self.Entrycentroide1X = tk.Entry(principal, bg="black",fg="white", font = "Verdana 12", textvariable=self.centroide1X).place(x = 170, y = 363)
        
        #Label, input y entry para eje X de desviación en K = 1
        self.LabelB3 = tk.Label(principal, bg="black", fg="white",text="Desviacion 1 :" ,font="Verdana 14").place(x=15,y=400)
        self.desviacion1X = tk.StringVar()
        self.EntryDesviacion1X = tk.Entry(principal, bg="black",fg="white", font = "Verdana 12", textvariable=self.desviacion1X).place(x = 170, y = 403) #captador de texto de Label 2
        
        #Label, input y entry para eje Y de centroide en K = 1
        self.LabelB4 = tk.Label(principal, bg="black", fg="white",text="Centroide 2 :" ,font="Verdana 14").place(x=15,y=440)
        self.centroide2X = tk.StringVar()
        self.Entrycentroide2X = tk.Entry(principal, bg="black",fg="white", font = "Verdana 12", textvariable=self.centroide2X).place(x = 170, y = 443)
        
        #Label, input y entry para eje Y de desviación en K = 1
        self.LabelB5 = tk.Label(principal, bg="black", fg="white",text="Desviacion 2 :" ,font="Verdana 14").place(x=15,y=480)
        self.desviacion2X = tk.StringVar()
        self.EntryDesviacion2X = tk.Entry(principal, bg="black",fg="white", font = "Verdana 12", textvariable=self.desviacion2X).place(x = 170, y = 483)
        
       
        """Clase 2"""
        
        #Label para clase 2
        self.LabelC1 = tk.Label(principal, bg="red", fg="white", text="Clase 2:", font="Verdana 14").place(x = 650, y = 300)
        
        #Label, input y entry para eje X de centroide en K = 2
        self.LabelC2 = tk.Label(principal, bg="black", fg="white", text="Centroide 1:", font="Verdana 14").place(x = 510, y = 360)
        self.centroide1Y = tk.StringVar()
        self.Entrycentroide1Y = tk.Entry(principal, bg="black",fg="white",font = "Verdana 12",textvariable=self.centroide1Y).place(x = 665, y = 363)
        
        #Label, input y entry para eje X de desviación en K = 2
        self.LabelC3 = tk.Label(principal, bg="black", fg="white", text="Desviacion 1 :", font="Verdana 14").place(x = 510, y = 400)
        self.desviacion1Y = tk.StringVar()
        self.EntryDesviacion1Y = tk.Entry(principal, bg="black",fg="white",font = "Verdana 12",textvariable=self.desviacion1Y).place(x = 665, y = 403)
        
        #Label, input y entry para eje Y de centroide en K = 2
        self.LabelC4 = tk.Label(principal, bg="black", fg="white", text="Centroide 2 :", font="Verdana 14").place(x = 510, y = 440)
        self.centroide2Y = tk.StringVar()
        self.Entrycentroide2Y = tk.Entry(principal, bg="black",fg="white",font = "Verdana 12",textvariable=self.centroide2Y).place(x = 665, y = 443)
        
        #Label, input y entry para eje Y de desviación en K = 2
        self.LabelC5 = tk.Label(principal, bg="black", fg="white", text="Desviacion 2 :", font="Verdana 14").place(x = 510, y = 480)
        self.desviacion2Y = tk.StringVar()
        self.EntryDesviacion2Y = tk.Entry(principal, bg="black",fg="white",font = "Verdana 12",textvariable=self.desviacion2Y).place(x = 665, y = 483)
        
        
        """Botón"""
        #Botón que ejecuta las funciones combinadas al ser presionado
        self.Boton = tk.Button(principal, bg="black", fg="white", font = "Arial 15", text="Ingresar", command = lambda:self.combinarFunciones() ).place(x = 850, y = 560)


    """Crea una ventana extra que muestra el resultado
    """
    def ventanaExtra(self):
        #Se llama al root para una ventana extra
        top = tk.Toplevel()
        #Se da un título a la ventana
        top.title("Resultado")
        #Define las dimensiones de la ventana
        top.geometry("600x400+250+80")
        #Abre la imagen
        self.foto = Image.open("figura.jpg")
        #Crea una iteración de PhotoImage con la imagen abierta
        self.imagen = ImageTk.PhotoImage(self.foto)
        #Le asigna la imagen a un label y este se coloca en la ventana
        self.Label = tk.Label(top,image=self.imagen).place(x=80,y=70)


    """Función que conecta los datos con el algoritmo
    @param datos, es el input de la cantidad de datos que se desean generar
    @param iteraciones, son la cantidad de iteraciones que se desean ejecutar
    @param clases, la cantidd de clases que se desean implementar (en este caso, el dato siempre sería 2)
    @param c1X, centroide en eje X para la primera clase
    @param d1X, desviación en eje X para la primera clase
    @param c2X, centroide en eje Y para la primera clase
    @param d2X, desviación en eje Y para la primera clase
    @param c1Y, centroide en eje X para la segunda clase
    @param d1Y, desviación en eje X para la segunda clase
    @param c2Y, centroide en eje Y para la segunda clase
    @param d2Y, desviación en eje Y para la segunda clase
    """
    def conectorKmedias(self, datos, iteraciones, clases, c1X, d1X, c2X, d2X, c1Y, d1Y, c2Y, d2Y):
        #Conseguir cantidad de datos
        valor_datos = int(datos.get())
        #Consigue iteraciones
        valor_iteraciones = int(iteraciones.get())
        #Consigue cantidad de clases
        valor_clases = int(clases.get())
        #Consigue centroide en X de K = 1
        valor_c1X = int(c1X.get())
        #Consigue desviación en X de K = 1
        valor_c1Y = int(c1Y.get())
        #Consigue centroide en Y de K = 1
        valor_c2X = int(c2X.get())
        #Consigue desviación en Y de K = 1
        valor_c2Y = int(c2Y.get())
        #Consigue centroide en X de K = 2
        valor_d1X = int(d1X.get())
        #Consigue desviación en X de K = 2
        valor_d1Y = int(d1Y.get())
        #Consigue centroide en Y de K = 2
        valor_d2X = int(d2X.get())
        #Consigue desviación en Y de K = 2
        valor_d2Y = int(d2Y.get())
        #Se llama a la clase Controlador con todos los datos recibidos
        controlador= Controlador(valor_datos, valor_clases, valor_iteraciones, valor_c1X, valor_d1X, valor_c2X, valor_d2X, valor_c1Y, valor_d1Y, valor_c2Y, valor_d2Y)
        #Ejecuta el iterador en la clase Controlador
        controlador.iteradorKmedias()
   
 
        
    """Ayuda a ejecutar dos acciones con un lapso de retraso al presionar el botón
    """
    def combinarFunciones(self):
        #Funcion Kmedias, donde se realizan los cálculos necesarios
        self.conectorKmedias(self.datos,self.iteraciones,self.clases,self.centroide1X,self.desviacion1X,self.centroide2X,self.desviacion2X,self.centroide1Y,self.desviacion1Y,self.centroide2Y,self.desviacion2Y)
        #Retrasa 1 segundo para crear la imagen
        time.sleep(1)
        #Funcion donde se crea la ventana con el resultado
        self.ventanaExtra()
        
        


"""Ejecuta la interfaz
"""
#Crea el root
root= tk.Tk()
#Llama a la clase Interfaz con el root
interfaz= Interfaz(root)
#Mantiene abierta la ventana emergente
root.mainloop()