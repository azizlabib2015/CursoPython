#import Fibonacci
#from Pixel import Pixel
from Musica.Musica import *
from Ejercicios1_8_6.ejercicios import *
import io

#print (Fibonacci.succesionFibonacci(8))

#print (Fibonacci.succesionPadovan(8))

#p=Pixel(2.1,3.4,"rojo")
#print(p)


#piano=Piano("Casio","Cuerda Percutida",1656,"Madera",True,88,False)
#trompeta=Trompeta("Yamaha","Viento",1609,"Laton",True,"Bb",True)
#a=str(piano.sonar())+"\n"
#a+=str(trompeta.sonar())+"\n"
data=imprimeAgenda()

file=open("Ejercicios1_8_6/agenda.txt","w")
file.write(data)
file.close()

file=open("Ejercicios1_8_6/agenda.txt","r")
print(file.read())
file.close()
