
import matplotlib.pyplot as plt


class Graficador:
    """
    @param matrizDatos, 2 filas y N columnas
    """
    def graficarPuntos(self, matrizDatos):
        plt.plot(matrizDatos[0, :], matrizDatos[1, :], "o")
        
    def unirPuntos(self, dato, puntoPartida):
        x = [dato[0]] + [puntoPartida[0]]
        y = [dato[1]] + [puntoPartida[1]]
        plt.plot(x, y, "r-")