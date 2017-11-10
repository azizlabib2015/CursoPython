def succesionFibonacci(n):
    f0=0
    f1=1
    succesion=[f0,f1]
    for i in range(n):
        f2=f0+f1
        succesion.append(f2)
        f0=f1
        f1=f2
    return succesion

#La sucesión de Padovan es la secuencia de números 
#enteros P(n) definida por los siguientes valores iniciales

#P(0)=P(1)=P(2)=1,

#y la siguiente relación de recurrencia

#P(n)=P(n-2)+P(n-3)

def succesionPadovan(n):
    succesion=[]
    for i in range(n):
        if i==0 or i==1 or i==2:
            succesion.append(1)
        else:
            valor=succesion[-3]+succesion[-2]
            succesion.append(valor)
        
    return succesion


