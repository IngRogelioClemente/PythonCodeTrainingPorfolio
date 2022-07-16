#Rogelio Clemente Balderas
#Python 3.7
#Spyder
#Apodaca, Nuevo Leon.

# CALCULADORA DE DATOS CREDITICIOS 2.0.
# Este programa imprime el dato a buscar. 
# Monto, capital, interes, tasa de interes y tiempo.

print("Este programa calcula datos crediticios.")
input("Presiona enter para continuar")
print("Para cada dato teclee el numero indicado.")
print("Monto: 1, Capital: 2, Interes: 3, Tasa de interes: 4, Tiempo: 5")

#ESTE BLOQUE DE CODIGO EJECUTA EL CALCULO DE LA VARIABLE ELEGIDA.
def monto():
    print("Monto.")
    
    C = float(input("Capital: "))
        
    Z = float(input("Tasa de interes en decimales: "))

    T = int(input("Tiempo en años: "))
    
    print("El monto es de ",(C*(1+(Z*T))))
    return True

#ESTE BLOQUE DE CODIGO EJECUTA EL CALCULO DE LA VARIABLE ELEGIDA.
def capital():
    print("Capital.")
    
    M = float(input("Monto: "))
   
    Z = float(input("Tasa de interes en decimales: "))

    T = int(input("Tiempo en años: "))
        
    print("El capital es de ",(M / (1+(Z*T))))
    return True

#ESTE BLOQUE DE CODIGO EJECUTA EL CALCULO DE LA VARIABLE ELEGIDA.
def interes():
    print("Interes.")
        
    C = float(input("Capital: "))
            
    Z = float(input("Tasa de interes en decimales: "))

    T = int(input("Tiempo en años: "))
        
    print("El interes es de ", (C*Z*T))
    return True

#ESTE BLOQUE DE CODIGO EJECUTA EL CALCULO DE LA VARIABLE ELEGIDA.
def tasa_de_interes():
    print("Tasa de interes.")
    
    I = float(input("Interes: "))
        
    C = float(input("Capital: "))
    
    T = int(input("Tiempo en años: "))
                
    print("La tasa de interes es de ",(I / (C*T)))
    return True

#ESTE BLOQUE DE CODIGO EJECUTA EL CALCULO DE LA VARIABLE ELEGIDA.
def tiempo():
    print("Tiempo.")
    
    C = float(input("Capital: "))
        
    Z = float(input("Tasa de interes en decimales: "))

    I = float(input("Interes: "))
        
    print("El tiempo es de ", (I / (C*Z)), "años")
    return True
    
#ESTE BLOQUE DE CODIGO ASIGNA LA FUNCION 
#QUE SE DESEA UTILIZAR SOLICITANDO AL USUARIO UN DIGITO.
def dato(opcion): 
    if opcion == 1: 
        return monto() 
    if opcion == 2:
        return capital()
    if opcion == 3:
        return interes()
    if opcion == 4:
        return tasa_de_interes()
    if opcion == 5:
        return tiempo()
    return False

#ESTE BLOQUE DE CODIGO EJECUTA EL PROGRAMA.
#SE ALMACENAN LAS BLOQUES DE FUNCIONES UNO DETRAS DE OTRO.
#EN ESTE CASO LA "OPCION" SE SUSTITUYE EN LA FUNCION DATO, EJECUTANDO DICHA 
#FUNCION Y ASI SUCESIVAMENTE.
def ejec():
    opcion = int(input("¿Que desea calcular?: "))
    return dato(opcion)

#SE EJECUTA LA FUNCION ASIGNADA.
ejec()

# By Rogelio Clemente Balderas
# 24/12/2021


#ESTA LINEA DE CODIGO SE UTILIZA PARA PODER EJECTURAR EL PROGRAMA .py
input("Presiona el boton enter para cerrar la ventana.")