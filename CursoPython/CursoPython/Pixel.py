class Pixel(Punto2D):
    """description of class"""

    #miembros

    color=""

    #constructor

def __init__(self,x,y,color):
    # llamamos al constructor de Punto2D
    Punto2D.__init__(self,x,y)

    # agregamos el nuevo atributo
    self.color=color

