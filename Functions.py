#Funcion suma
import math
#from Calculadora import name
from datetime import *


hoy= datetime.today()

def suma():
    a=float(input("Digita un numero: "))
    b=float(input("Digita otro numero: "))
    c=(a+b)
    with open("File.txt","a") as f:
           f.write("Fecha: "+str(hoy)+"\nOperacion: Suma de "+str(a)+" + "+str(b)+"\nResultado obtenido: "+str(c)+"\n")    
    # print("La suma es: ",c)

#Funcion resta
def resta():
    a=float(input("Digita un numero: "))
    b=float(input("Digita otro numero: "))
    if(a>b):
        c=(a-b)
        with open("File.txt","a") as f:
            f.write("\nFecha: "+str(hoy)+"\nOperacion: Resta de "+str(a)+" - "+str(b)+"\nResultado obtenido: "+str(c)+"\n")
    else:
         c=(b-a)
         with open("File.txt","a") as f:
            f.write("\nFecha: "+str(hoy)+"\nOperacion: Resta de "+str(b)+" - "+str(a)+"\nResultado obtenido: "+str(c))+"\n"
    # print("La resta es: ",c)

def mult():
    a=float(input("Digita un numero: "))
    b=float(input("Digita otro numero: "))
    c=(a*b)
    with open("File.txt","a") as f:
            f.write("\nFecha: "+str(hoy)+"\nOperacion: Multiplicacion de "+str(a)+" X "+str(b)+"\nResultado obtenido: "+str(c)+"\n")
    # print("La multiplicacion es: ",c)
    
def div():
     a=float(input("Digita un numero: "))
     b=float(input("Digita otro numero: "))
     if(a==0):
        #print("0")
        with open("File.txt","a") as f:
            f.write("0")
     elif(b==0):
        #print("No se puede dividir ",a," entre 0")
        with open("File.txt","a") as f:
            f.write("\nFecha: "+str(hoy)+"\nOperacion: Dividicion entre "+str(a)+" X "+str(b)+"\nResultado obtenido: No es posible dividir",str(a),"entre 0\n")
     else:
        c=(a/b)
        #print("La division  es: ",c)
        with open("File.txt","a") as f:
            f.write("\nFecha: "+str(hoy)+"\nOperacion: Division entre "+str(a)+" / "+str(b)+"\nResultado obtenido: "+str(c)+"\n")

def sen():
    a=float(input("Digita el angulo: "))
    #print("El seno de ",a," es: ",math.sin(a))
    with open("File.txt","a") as f:
            f.write("\nFecha: "+str(hoy)+"\nOperacion: Seno de "+str(a)+"\nResultado obtenido: "+str(math.sin(a))+"\n")

def cos():
    a=float(input("Digita el angulo: "))
    #print("El coseno de ",a," es: ",math.cos(a))
    with open("File.txt","a") as f:
            f.write("\nFecha: "+str(hoy)+"\nOperacion: Coseno de "+str(a)+"\nResultado obtenido: "+str(math.cos(a))+"\n")

def tan():
    a=float(input("Digita el angulo: "))
    #print("La tangente de ",a," es: ",math.tan(a))
    with open("File.txt","a") as f:
            f.write("\nFecha: "+str(hoy)+"\nOperacion: Tangente de "+str(a)+"\nResultado obtenido: "+str(math.tan(a))+"\n")
    
def par():
    lista=[]
    a=int(input("Digita un numero: "))
    for item in range(a):
        item=item+1
        if(item%2==0):
            lista.append(item)
    #print(lista)
    with open("File.txt","a") as f:
            f.write("\nFecha: "+str(hoy)+"\nOperacion: Numero pares de "+str(a)+"\nResultado obtenido: "+str(lista)+"\n")
    
    
    
    
    
    

