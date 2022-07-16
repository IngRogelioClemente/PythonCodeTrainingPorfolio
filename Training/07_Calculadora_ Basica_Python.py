#CALCULADORA BASICA PARA 2 VARIABLES
#EL PROGRAMA SOLO OPERA UNA OPERACION POR EJECUCION


#INICIO 

#VALORES A Y B
Valor_A = input("Valor: ")
a = float(Valor_A)

Valor_B = input("Valor: ")
b = float(Valor_B)

#OPERADOR

op = input("Operacion: ")


#CICLO FOR
for symbol in op:
    if symbol == "+":
        print(a+b)
    elif symbol == "-":
        print(a-b)   
    elif symbol == "*":
        print(a*b)  
    elif symbol == "/":
        print(a/b)
#FIN

#By Rogelio Clemente Balderas
input("Presiona el boton enter para cerrar la ventana.") 
