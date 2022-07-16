#PROGRAMA QUE CALCULA DATOS CREDITICIOS.
# monto, capital, interes, tasa de interes y tiempo.
#PROGRAMA PROPUESTO POR MILTON ALONSO GUERRERO - FACPYA.

#INICIO

print("Este programa calcula el dato crediticio a elegir.")
print("Introduzca el dato que desea calcular usando la nomenclatura.")
print("Para monto: M, capital: C, interes: I, tasa de interes: Z, tiempo: T")

dato = input("Dato: ")

for valor in dato:
    if valor == "M":
        
        capital = input("Capital: ")
        C = float(capital)
        
        tasa_de_interes = input("Tasa de interes en decimales: ")
        Z = float(tasa_de_interes)

        tiempo = input("Tiempo en años: ")
        T = float(tiempo)
        
        print("El monto es de ",(C*(1+(Z*T))))
        
    elif valor == "C":
        
        monto = input("Monto: ")
        M = float(monto)
        
        tasa_de_interes = input("Tasa de interes en decimales: ")
        Z = float(tasa_de_interes)

        tiempo = input("Tiempo en años: ")
        T = float(tiempo)
        
        print("El capital es de ",(M / (1+(Z*T))))
        
    elif valor == "I":
        
        capital = input("Capital: ")
        C = float(capital)
        
        tasa_de_interes = input("Tasa de interes en decimales: ")
        Z = float(tasa_de_interes)

        tiempo = input("Tiempo en años: ")
        T = float(tiempo)
        
        
        print("El interes es de ", (C*Z*T))
        
    elif valor == "Z":
        
        interes = input("Interes: ")
        I = float(interes)
        
        capital = input("Capital: ")
        C = float(capital)

        tiempo = input("Tiempo en años: ")
        T = float(tiempo)
        
        
        print("La tasa de interes es de ",(I / (C*T)))
        
    elif valor == "T":
        
        capital = input("Capital: ")
        C = float(capital)
        
        tasa_de_interes = input("Tasa de interes en decimales: ")
        Z = float(tasa_de_interes)

        interes = input("Interes: ")
        I = float(interes)
        
        print("El tiempo es de ", (I / (C*Z)), "años")
        
    
#By Rogelio Clemente Balderas
input("Presiona el boton enter para cerrar la ventana.")