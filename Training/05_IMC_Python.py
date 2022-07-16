#PROGRAMA QUE CALCULA EL IMC DE UNA PERSONA

#INICIO

#DATOS
peso = input("Introduzca su peso en kilogramos: ")
p = float(peso)

altura = input("Introduzca su altura en metros: ")
a = float(altura)

#PROCESAMIENTO
IMC = p / (a*a) 

#SALIDA
print("Su IMC es: ", IMC) 

#FIN

#By Rogelio Clemente Balderas
input("Presiona el boton enter para cerrar la ventana.") 