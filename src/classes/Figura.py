class Figura:

    def __init__(self, tipo, puntos):
        """ 
        tipos: Rectángulo, Cuadrado, 
        un Triángulo Acutángulo 
        y un Triángulo Rectángulo
        """
        self.tipo = tipo
        self.puntos = puntos
        self.area = 0

    def obtener_puntos(self):
        return self.puntos

    def mostrar_informacion(self):
        print("Tipo:", self.tipo)
        print("Puntos:", self.puntos)
        print("Área:", self.area)