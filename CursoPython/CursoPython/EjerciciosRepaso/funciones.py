import random
import math
import itertools
#ejercicio 1
def secuenciaNumeros(lista):
    cont=1
    repetido=False
    r=0
    for x in lista:
        if cont==1 :
            r=x
            cont=cont+1
        elif cont>1:
            if x==r:
                repetido=True
            else:r=x

    return repetido



#ejercicio 2

def secuenciaNumerosEliminar3Elemento(lista):
    lista.pop(2)
    return lista

  

#Ejercicio 3

def divisoresNumero(num):
    lista=[]
    for i in range(1,num+1):
        if num%i==0:
            lista.append(i)
    return lista
    


#ejercicio 4

def listaSinDuplicado(lista1,lista2):
    listaComun=[]
    for i in lista1:
        for j in lista2:
            if i==j:
                listaComun.append(i)
    return listaComun
    
    


#ejercicio 5

def piedraPapelTijera():
    
    jugador1=input("Jugador 1: ")
    jugador2=input("Jugador 2: ")
    result=""
    if jugador1==jugador2:
        result+=jugador1+" vs "+jugador2+" :Empate"
    elif jugador1=="piedra" and jugador2=="papel":
        result+=jugador1+" vs "+jugador2+" :Gana jugador 2"
    elif jugador1=="piedra" and jugador2=="tijera":
        result+=jugador1+" vs "+jugador2+" :Gana jugador 1"
    elif jugador1=="tijera" and jugador2=="papel":
        result+=jugador1+" vs "+jugador2+" :Gana jugador 1"
    elif jugador1=="tijera" and jugador2=="piedra":
        result+=jugador1+" vs "+jugador2+" :Gana jugador 2"
    elif jugador1=="papel" and jugador2=="piedra":
        result+=jugador1+" vs "+jugador2+" :Gana jugador 1"
    elif jugador1=="papel" and jugador2=="tijera":
        result+=jugador1+" vs "+jugador2+" :Gana jugador 2"

    print(result)


#ejercicio 6

def Adivinar():
    numero=random.randint(1,10)
    res=""
    n_Adivinado=int(input("Adivina un numero: "))
    while n_Adivinado!=numero:
        if numero>n_Adivinado:
            res="Demasiado Bajo"
            print(res)
        elif numero<n_Adivinado:
            res="Demasiado Alto"
            print(res)
        
        n_Adivinado=int(input("Adivina un numero: "))
    else:
        res="Acertaste"
        print(res)

    
#ejercicio 7
def listaPrimerUltimoElemento(lista):
    return [lista[1],lista[-1]]

#ejercicio 8

def fraseInversa(frase):
    frase_inversa=""
    palabras=frase.split(' ')
    lista=list(palabras)
    lista.reverse()
    for x in lista:
        frase_inversa+=x+" "
    return frase_inversa
    
    


#ejercicio 9
def CombinacionesPosibles(lista):
    return list(itertools.permutations(lista))


#ejercicio 10
def caracteresRepetidos(frase):
    f="letra --> veces repetidos\n"
    chars=list(frase)
    diccionario={}

    for i in chars:
        if i in diccionario:
            diccionario[i]+=1
        else:
            diccionario[i]=1
    
                

    for i in diccionario:
        f=f+i+"---"+str(diccionario[i])+"\n"


    return f

#ejercicio 11

def sumaSecuencias(lista):
    suma=0
    for x in lista:
        suma=suma+x
    return suma
    
#ejercicio 12

def productoSecuencias(lista):
    producto=1
    for x in lista:
        producto=producto*x
    return producto    

#ejercicio 13
def mayorNumero(lista):
    return max(lista)

#ejercicio 14
def menorNumero(lista):
    return min(lista)

#ejercicio 15
def ordenarLista(lista):
    lista.sort()
    return lista

#ejercicio 16
def desordenarListaAleatorio(lista):
    lista2=[]
    lenAleatorio=[random.randint(1,len(lista)) for p in range(0,len(lista))]
    for x in lista:
        lista2.append(lista[x])
    return lista2
    
    
print([1,2,3,4,5])    
print(desordenarListaAleatorio([1,2,3,4,5]))

    