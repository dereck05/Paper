# -*- coding: utf-8 -*-
"""
Created on Fri Nov  3 11:02:27 2017


"""


import numpy
from GeneradorDatos import GeneradorDatos
import matplotlib.pyplot as plt
from Graficador import Graficador


class AmontonadorKmedias:
    def __init__(self, K, X):   #K = numero de pares aleatorios
        self.__generadorDatos = GeneradorDatos();
        self.__K = K
        self.__X = X;           #matrix
        self.__N = len(X[0])    #size of matrix of random points
    
        print("-----------------------------------------")
        self.__N = len(X[0])
        
        self.puntoMenorX = self.minimoX();
        print("Punto menorX: ", self.puntoMenorX)
        self.puntoMaximoX = self.maximoX();
        print("Punto maximoX: ", self.puntoMaximoX )
        self.puntoMenorY = self.minimoY();
        print("Punto menorY: ", self.puntoMenorY )
        self.puntoMaximoY = self.maximoY();
        print("Punto maximoY: ", self.puntoMaximoY)
        
        deltaX = numpy.linalg.norm(self.puntoMaximoX - self.puntoMenorX);
        deltaY = numpy.linalg.norm(self.puntoMaximoY - self.puntoMenorY);
        print("DeltaX: ", deltaX)
        print("DeltaY: ", deltaY)
        
    
        
        self.__matrizCentroides = numpy.zeros((2 , K));
        self.__matrizPesos = numpy.zeros((self.__N, K))
        
        #Inicializa aleatoriamente los centroides
        for i in range(0, K):
            puntoAleatorio = self.__generadorDatos.generarPuntoAleatorio(self.puntoMenorX - 10, self.puntoMaximoX + 10, self.puntoMenorY - 10, self.puntoMaximoY + 10);
            self.__matrizCentroides[0, i] = puntoAleatorio[0];
            self.__matrizCentroides[1, i] = puntoAleatorio[1];
        
        print("Centroides:",self.__matrizCentroides)
    
    def getCentroides(self):
        return self.__matrizCentroides;
    
    def getMatrizPesos(self):
        return self.__matrizPesos
    
    def setValor(self, fila, columna, valor):
        self.__X[fila][columna] = valor
        
    def setCentroides(self, valor):
        self.__matrizCentroides = valor
    
    def setMatrizPesos(self, valor):
        self.__matrizPesos = valor

            
    def minimoX(self):
       
        cont = self.__X.shape[1];
        minimoX = self.__X[: , 0][0];
        
        for i in range(0, cont):
             par = self.__X[: , i];
             if(par[0] < minimoX):
                 minimoX = par[0];
        
        return minimoX
    
    def minimoY(self):
       
        cont = self.__X.shape[1];
        minimoY = self.__X[: , 0][1];
        
        for i in range(0, cont):
             par = self.__X[: , i];
             if(par[1] < minimoY):
                 minimoY = par[1];
       
        return minimoY
    
    def maximoX(self):
       
        cont = self.__X.shape[1];
        maximoX = self.__X[: , 0][0];
        
        for i in range(0, cont):
             par = self.__X[: , i];
             if(par[0] > maximoX):
                 maximoX = par[0];
        
        return maximoX
    
    def maximoY(self):
       
        cont = self.__X.shape[1];
        maximoY = self.__X[: , 0][1];
        
        for i in range(0, cont):
             par = self.__X[: , i];
             if(par[1] > maximoY):
                 maximoY = par[1];
        
        return maximoY
             
 
    def etiquetar(self):
        resultado = self.__matrizPesos
        
        contadorIndices = 0   #contador para colocar bien el resultado en la matriz pesos
        
        for i in range(0, self.__N):
            parOrdenado= [self.__X[0][i] , self.__X[1][i]]
            distancia = numpy.linalg.norm(parOrdenado - self.__matrizCentroides[:, 0])
            numCentroide = 0
            
            for i in range(0 , self.__K):   #calcula cual centroide es mas cercano a un par
                distancia2 = numpy.linalg.norm(parOrdenado - self.__matrizCentroides[:, i])#calcula distancia euclideana dados dos pares :o
                if(distancia2 < distancia):
                    numCentroide = i;       #obtiene la posicion del centroide mas cercano en el array
                    distancia = distancia2
            
            for i in range(0 ,self.__K):       #fase de etiquetado de matriz de pesos
                
                if (i == numCentroide):   
                    resultado[contadorIndices, :][i] = 1
                else:
                    resultado[contadorIndices, :][i] = 0
            contadorIndices += 1
                
                
        self.setMatrizPesos(resultado)
        
    def amontonarK(self, K):
        etiquetas = self.__matrizPesos
        for i in range (0, self.__N):
            if (etiquetas[i, K] == 1):
                #Adjunto el dato correspondiente al centroide en X y en Y
                datosx = [self.__matrizCentroides[0, 0]] + [self.__X[0, i]]
                datosy = [self.__matrizCentroides[0, 1]] + [self.__X[1, i]]
                
                #Añado las líneas con los puntos al plot
            else:
                datosx = [self.__matrizCentroides[1, 0]] + [self.__X[0, i]]
                datosy = [self.__matrizCentroides[1, 1]] + [self.__X[1, i]]
                
            plt.plot(datosx, datosy, marker="o")
        
'''
    def etiquetar(self):
        resultado = self.__matrizPesos
        
        contadorIndices = 0   #contador para colocar bien el resultado en la matriz pesos
        distancia1 = 0    #acumulador distancia 1
        distancia2 = 0    #acumulador distancia 2
        
        for i in range(0, self.__N):
            parOrdenado= [self.__X[0, i], self.__X[1, i]]
            print("pba:",parOrdenado)
            distancia1 = numpy.linalg.norm(parOrdenado - self.puntoMenor)#Ambos parametros suponen un par ordenado
            distancia2 = numpy.linalg.norm(parOrdenado - self.puntoMax)
            valor = 1
            if (distancia1 < distancia2):   #Ponemos 1 si es el elemento mas cercano a etiqueta 1
                resultado[contadorIndices, 0] = valor
                contadorIndices += 1
            else:
                #Sino ponemos 1 a etiqueta 2
                resultado[contadorIndices, 1] = valor
                contadorIndices += 1
                
       
            
        return resultado
'''
'''
    def amontonarK(self, K):
        etiquetas = self.__matrizPesos
        for i in range (0, self.__N):
            if (etiquetas[i, K] == 0):
                #Adjunto el dato correspondiente al centroide en X y en Y
                datosx = [self.__matrizCentroides[0, 0]] + [self.__X[0, i]]
                datosy = [self.__matrizCentroides[0, 1]] + [self.__X[1, i]]
                #Añado las líneas con los puntos al plot
            else:
                datosx = [self.__matrizCentroides[1, 0]] + [self.__X[0, i]]
                datosy = [self.__matrizCentroides[1, 1]] + [self.__X[1, i]]
            plt.plot(datosx, datosy, marker="o")
                
'''  
    
def principal():
    K = 4;
    graficador = Graficador();
    generadorDatos = GeneradorDatos();
    
    N = 100; #cantidad de datos
    matrizXc1 = generadorDatos.generarDatosGauss2D(28, 3, 20, 10, N);
    graficador.graficarPuntos(matrizXc1);
    
    Y = AmontonadorKmedias(K, matrizXc1);
 
    
    centroides = AmontonadorKmedias.getCentroides(Y)
    plt.plot(centroides[0, :], centroides[1, :], "o")
    etiquetas = Y.etiquetar()
    #amontonadoCentroide1 = Y.amontonarK(0)
    #amontonadoCentroide2 = Y.amontonarK(1)
    #plt.show()
    #print("Etiquetas: ", etiquetas)
    
    
principal()
        
                
                      
            
                
               