class Instrumento:

    def __init__(self,marca,tipo,fecha_invencion,material,afinado=True):
        self.marca = marca
        self.tipo = tipo
        self.fecha_invencion = fecha_invencion
        self.material = material
        self.afinado = afinado

    def afinar(self):
        self.afinado = True

    def sonar(self):
        print("...")


class Piano(Instrumento):
    def __init__(self, marca, tipo, fecha_invencion, material, afinado,numero_teclas,electrico):
        super().__init__(marca, tipo, fecha_invencion, material, afinado)
        self.numero_teclas=numero_teclas
        self.electrico=electrico
    
    def sonar(self):
        print("din dan dun!")


class Trompeta(Instrumento):
    def __init__(self, marca, tipo, fecha_invencion, material, afinado,tonalidad,atril_incluido=False):
         super().__init__(marca, tipo, fecha_invencion, material, afinado)
         self.tonalidad=tonalidad
         self.atril_incluido=atril_incluido


    def sonar(self):
        print("fñohjfokj")
    
    
