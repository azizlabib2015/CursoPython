import math

#numeroF=float(input("introduce un numero float: "))

def numeroNormalizado(numero):
    if numero in range(0,100):
        c=numero/100
        print(c)
    else:
        print("Error: El numero debe ser entre 0 y 100")
    

def areaTriangulo(base,altura):
    return (base*altura)/2

def areaCirculo(radio):
    return math.pi*math.pow(radio,2)
    
def rangoPar(a,b):
    return list(x if(x%2 == 0) else "" for x in range(a,b+1))
        
print("area del circulo(radio 3): "+str(areaCirculo(3)))
print("area del triangulo(base=3,altura5): "+str(areaTriangulo(3,5)))
print(rangoPar(0,15))

#resultado=numeroNormalizado(numeroF)

