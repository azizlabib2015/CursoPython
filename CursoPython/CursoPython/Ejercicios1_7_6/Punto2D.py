class Punto2D:
    """description of class"""
    #miembros

    x=0.0
    y=0.0

    #constructores 
    #constructor con dos parametros de entrada 
    def __init__(self,x,y):
        self.x=x
        self.y=y

    #constructor vacio
    def __init__(self):
        self.x=0.0
        self.y=0.0
    
    def __str__(self):
        return "X=" +str(self.x)+ " Y="+str(self.y)
    
        


