
import numpy


class GeneradorDatos:
    """
    @param media1, media de la dimension 1
    @param media2, media de la dimension 2 
    @param desv1, desviacion estandar de la dimension 1
    @param desv2, desviacion estandar de la dimension 2
    @param cantidadDatos, cantidad de muestras a generar aleatoriamente
    """
    def generarDatosGauss2D(self, media1, desv1, media2, desv2, cantidadDatos):
        #se generan las muestras aleatoriamente, con una distribucion normal, para cada dimension
        muestrasDimension1 = numpy.random.normal(media1, desv1, cantidadDatos);
        muestrasDimension2 = numpy.random.normal(media2, desv2, cantidadDatos);
        matrizX = numpy.zeros((2, cantidadDatos));
        for i in range(0, cantidadDatos):
            #se concatena cada muestra en la matriz X
            matrizX[0, i] = muestrasDimension1[i];
            matrizX[1, i] = muestrasDimension2[i];
            
        return matrizX;
        
    """
    Genera un punto en 2D (R^2) aleatoriamente
    @param min1, minimo valor posible para la dimension 1
    @param max1, maximo valor posible para la dimension 1
    @param min2, minimo valor posible para la dimension 2
    @param max2, maximo valor posible para la dimension 2    
    """
    def generarPuntoAleatorio(self, min1, max1, min2, max2):
        
        punto2D = numpy.zeros((2,1));
        punto2D[0, :] = numpy.random.uniform(min1, max1, 1);
        punto2D[1, :] = numpy.random.uniform(min2, max2, 1);
        return punto2D;
