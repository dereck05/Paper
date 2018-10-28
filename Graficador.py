
import matplotlib.pyplot as plt


class Graficador:
    """
    @param matrizDatos, 2 filas y N columnas
    """
    def graficarPuntos(self, matrizDatos):
        plt.plot(matrizDatos[0, :], matrizDatos[1, :], "o")
        
    