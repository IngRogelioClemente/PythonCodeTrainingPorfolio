#CONTADOR DE VOCALES PYTHON.
#ESTE PROGRAMA SOLICITARA UN TEXTO O PALABRA.
#ASI MISMO ARROJARA LA CANTIDAD DE VOCALES QUE EL TEXTO O PALABRA TIENE.

word = input("Escriba un texto o palabra: ")
count = 0

#Loop and counting
for letter in word:

#LETRAS MINUSCULAS
    if letter == "a":
        count = count + 1
    elif letter == "e":
        count = count + 1
    elif letter == "i":
        count = count + 1
    elif letter == "o":
        count = count + 1
    elif letter == "u":
        count = count + 1
        
#LETRAS MAYUSCULAS
    elif letter == "A":
        count = count + 1
    elif letter == "E":
        count = count + 1
    elif letter == "I":
        count = count + 1
    elif letter == "O":
        count = count + 1
    elif letter == "U":
        count = count + 1
    
print(count)

#By Rogelio Clemente Balderas
input("Presiona el boton enter para cerrar la ventana.")
