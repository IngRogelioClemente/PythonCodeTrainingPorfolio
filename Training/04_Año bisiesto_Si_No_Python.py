#PROGRAMA QUE INDICA SI ES YEAR BISIESTO O NO 

year = input("Introduzca el year: ")
y = float(year)

if y % 4 == 0:
    print("El year es bisiesto")
elif y % 400 == 0:
    print("El year es bisiesto")
elif y % 100 != 0:
    print("El year es bisiesto")
else:
    print("El year no es bisiesto")

#By Rogelio Clemente Balderas
input("Presiona el boton enter para cerrar la ventana.")