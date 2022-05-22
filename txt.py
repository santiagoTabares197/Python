# File=open('File.txt','w')

# try:
#     File.write("Hola archivo de texto")
# finally:
#     File.close()
# i=1
# while i<=10:    
#     with open('File.txt','a') as f:
#         f.write("Hola mundo " +str(i)+"\n")
#         i+=1


#PRUEBA
from datetime import*



hoy= datetime.today()

a=float(input("Digita un numero: "))
b=float(input("Digita un numero: "))

resta=(a-b)

with open("File.txt","a") as f:
    f.write("\nFecha: "+str(hoy)+" Realizaste la resta entre "+str(a)+"-"+str(b)+" y como resultado obtuviste: "+str(resta))