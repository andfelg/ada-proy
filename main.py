from src.classes.Figura import Figura


# f = figura

f1 = [(1, 1), (1, 4), (4, 4), (4, 1)]
f2 = [(1, 1), (3, 5), (5, 1), (1, 1)]
f3 = [(1, 1), (1, 3), (6, 3), (6, 1)]
f4 = [(3, 1), (1, 3), (3, 5), (5, 3)]

# Ejemplo de implementacion de la clase figura
fTest = Figura(
    "cuadrado",
    [(1, 1), (1, 4), (4, 4), (4, 1)]
)


fTest.mostrar_informacion()

figuras = [f1, f2, f3, f4]


