#JUEGO PARA ENCONTRAR NUMERO 
#BASADO EN ED TEAM

#ASIGNACION DE VALORES.
num = 10
user = 0

#CICLO WHILE.
while user != num:
    user = int(input("Which is the number?: "))
    
#CONDICIONALES.
    if user > num:
        print("Down")
    elif user < num:
        print("Up")
    else:
        print("Correct!")
        
#By Rogelio Clemente Balderas
input("Press enter button to end the game.")