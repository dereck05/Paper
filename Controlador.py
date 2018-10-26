from Amontonador import AmontonadorKmedias
import matplotlib.pyplot as plt
import numpy
from GeneradorDatos import GeneradorDatos
import time
import os
from datetime import datetime

class Controlador:
    
    """
    Constructor del controlador
    @param N, la cantidad de datos
    @param K, cantidad de clases
    @param P, el numero de iteraciones
    @param Xc1, centroide en eje X para la primera clase
    @param Xd1, desviación en eje X para la primera clase
    @param Xc2, centroide en eje Y para la primera clase
    @param Xd2, desviación en eje Y para la primera clase
    @param Yc1, centroide en eje X para la segunda clase
    @param Yd1, desviación en eje X para la segunda clase
    @param Yc2, centroide en eje Y para la segunda clase
    @param Yd2, desviación en eje Y para la segunda clase
    """
    def __init__(self,N, K,P,Xc1,Xd1,Xc2,Xd2,Yc1,Yd1,Yc2,Yd2):
        self.__K = K
        self.__N = N
        self.__P = P
        self.__centroide1X = Xc1 
        self.__centroide2X = Xc2
        self.__desviacion1X = Xd1
        self.__desviacion2X = Xd2
        self.__centroide1Y = Yc1
        self.__centroide2Y = Yc2
        self.__desviacion1Y = Yd1
        self.__desviacion2Y = Yd2
        #Llama al generador de datos para crear X, osea, la matriz con datos aleatorios
        self.__X = self.generarDatos()
        
        
        
    """
    Función iterativa que realiza el algoritmo Kmedias    
    """
    def iteradorKmedias(self):
        
        #Encuentro el directorio en el que se está trabajando actualmente
        ruta = os.getcwd()
    
    
        #Consigo el tiempo
        tiempo = datetime.now()
        #Le asigno el nombre a la carpeta
        nombreCarpeta = "%s_%s_%s_%s_%s_%s" % (tiempo.day, tiempo.month, tiempo.year, tiempo.hour, tiempo.minute, tiempo.second)
        #Junto la ruta actual con el nombre de la carpeta
        ruta = os.path.join(ruta, nombreCarpeta)
        #Convierto el nombre a un string
        x = str(ruta)
        #Creo la carpeta si no existe
        if not os.path.exists(x):
            os.makedirs(x)

        
        #Llamo al contador
        contador = 1
        #Llamo a amontonar Kmedias
        Y = AmontonadorKmedias(self.__K, self.__X)
        #Se realizan las iteraciones
        while contador <= self.__P:
            #Se espera un segundo
            time.sleep(1)
            if contador == 1:
                
                #Consigo los centroides
                centroides = AmontonadorKmedias.getCentroides(Y)
                
                #Realizo la fase de etiquetado
                Y.etiquetar()
        
                #Se grafican las líneas que unen los puntos con los centroides
                amontonadoCentroide1 = Y.amontonarK(0)
                
                #Grafico los centroides
                plt.plot(centroides[:, 0], centroides[:, 1], "black", marker = "s", ls="--", label = "Centroide original")
                
                #Muestro el gráfico
                plt.plot()
                
                #Busco el segundo actual
                tiempo = time.strftime("%S")
                #Le asigno un nombre con extensión jpg a la imagen de resultado
                rutaPrimera = os.path.join(x, "resultado" + str(tiempo) + ".jpg")
                #Salvo el gráfico como imagen
                plt.savefig(rutaPrimera)
                
                #Cierro el plot
                plt.close()
                #Aumento en 1 el contador para seguir con la iteración siguiente
                contador += 1
                
                
            else:
                #Aquí se guarda la figura final
                #Se realizan los mismos pasos que anteriormente
                if contador == self.__P:
                    Y.recalcularKmedias()
                    #Reasigno las etiquetas
                    Y.etiquetar()
                    centroides = AmontonadorKmedias.getCentroides(Y)
                    
                    #Grafica las líneas que unen los puntos con los centroides
                    amontonadoCentroide1 = Y.amontonarK(0)
                    
                    plt.plot([centroides[0][0], centroides[1][0]], [centroides[0][1], centroides[1][1]], "black", marker="s", ls="--", label = "Centroide Nuevo")
                    plt.legend(loc="upper left")
                    
                    
                    plt.plot()
                    tiempo =time.strftime("%S")
                    plt.savefig(os.path.join(x,"resultado"+str(tiempo)+".jpg"))
                    plt.savefig("figura.jpg")
                    plt.close()
                    contador += 1
                else:
            
                    #Recalculo los centroides
                    Y.recalcularKmedias()
                    #Reasigno las etiquetas
                    Y.etiquetar()
                    centroides = AmontonadorKmedias.getCentroides(Y)
                    
                    
                    #Grafica las líneas que unen los puntos con los centroides
                    amontonadoCentroide1 = Y.amontonarK(0)
                    
                    plt.plot([centroides[0][0], centroides[1][0]], [centroides[0][1], centroides[1][1]], "black", marker="o", ls="--", label = "Centroide Nuevo")
                    plt.legend(loc="upper left")
                    
                    
                    
                    plt.plot()
                    tiempo =time.strftime("%S")
                    plt.savefig(os.path.join(x, "resultado" + str(tiempo) + ".jpg"))
                    plt.close()
                    contador+=1
                
            
    """
    Se generan los datos aleatorios         
    """
    def generarDatos(self):
        #Llama a generados de datos
        generadorDatos = GeneradorDatos()
        #Genera los datos de la clase 1
        matrizXc1 = generadorDatos.generarDatosGauss2D(self.__centroide1X,self.__desviacion1X, self.__centroide2X, self.__desviacion2X, self.__N)
        #Genera los datos de la clase 2
        matrizXc2 = generadorDatos.generarDatosGauss2D(self.__centroide1Y,self.__desviacion1Y, self.__centroide2Y, self.__desviacion2Y, self.__N)
        #Concatena los resultados en una sola matriz "X"
        X = numpy.concatenate((matrizXc1, matrizXc2), axis = 1 )
        #Retorna la matriz de resultado
        return  X          


def principal():
    
    K = 2 #cantidad de clases
    N = 50 #cantidad de datos
    
    control=Controlador(N,K,5,15,10,20,10,5,10,10,10)
    control.iteradorKmedias()
    
principal()               
