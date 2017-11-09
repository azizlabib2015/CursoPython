#importamos la libreria random
import random

#primera parte:craer una tupla de numeros aleatorios
mi_lista = []
numero_Elementos = 15
#lista creada por for
#for i in range(numero_Elementos):
#    aleatorio=random.randint(0,50)
#    mi_lista.append(aleatorio)
 
#lista creada por comprension
#mi_lista=[random.randint(0,50) for i in range(numero_Elementos)]

#tupla creada por comprension
mi_tupla = tuple(random.randint(0,50) for i in range(numero_Elementos))


#segunda parte crear un diccionario donde las claves son los numeros y el valor
#son las repeticiones
mi_diccionario = dict()

#opcion 1 diccionario con un for
#for i in mi_tupla:
#    if i in mi_diccionario:
#        mi_diccionario[i]=mi_diccionario[i]+1
#    else:
#        mi_diccionario[i]=1

#opcion 2 diccionario con compresion
mi_diccionario={x:mi_tupla.count(x) for x in set(mi_tupla)}
print("clave -- valor")
for k,v in mi_diccionario.items():
    print("%s -> %s" % (k,v))
#tercrea parte :imprimir por pantala el diccionario con el formato
'''
0 -> 2
'''
    