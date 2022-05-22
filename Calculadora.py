
import Functions

print("BIENVENIDO A LA SUPER CALCULADORA hecha por Santiago Tabares Acosta")
name=input("Para hacer nuestro proceso más ameno, digita tu nombre: ")
#name="Santiago"

print("Bienvenido ",name)

print("MENU DE OPERACIONES...")
print("1.Suma")
print("2.Resta")
print("3.Multiplicacion")
print("4.Division")
print("5.Seno")
print("6.Coseno")
print("7.Tangente")
print("8.¿Quieres digitar un numero y saber los numeros pares que tiene detras?")
resp=input("\n¿que operacion deseas hacer el dia de hoy?\n R//")

#condicional if 
if(resp=="1"):
    print("Elegiste suma")
    Functions.suma()
elif(resp=="2"):
    print("Elegiste resta")
    Functions.resta()
elif(resp=="3"):
    print("Elegiste multiplicacion")
    Functions.mult()
elif(resp=="4"):
    print("Elegiste division")
    Functions.div()
elif(resp=="5"):
    print("Elegiste seno")
    Functions.sen()
elif(resp=="6"):
    print("Elegiste coseno")
    Functions.cos()
elif(resp=="7"):
    print("Elegiste tangente")
    Functions.tan()
elif(resp=="8"):
    print("Elegiste saber los numeros pares")
    Functions.par()
else:
    print("Elige una opcion valida por favor!")

print("Gracias por utilizar la SUPER CALCULADORA")
