#Programa que solicite a algun alumno que desea coonsultar de su escuela
#Objeto: Escuela
#Campos o atributos: Materias
#Metodos: Salones

print("¿Desea consultar la información acerca de los grupos disponibles en su escuela?")
print("1. Si | 2. No")
R = input("Opcion: ")

def Consulta_Escolar():
    FIME = Escuela()

    print("¿Qué salon desea consultar?")
    print("1. Salon 1 | 2. Salon 2 | 3. Salon 3")

    C = input("Opcion: ")
    if C == "1":
        return FIME.Salon1
    elif C == "2":
        return FIME.Salon2
    elif C == "3":
        return FIME.Salon3

if R == "1":
    Consulta_Escolar()
elif R == "2":
    print("¡Gracias vuelva pronto!")

class Escuela: #Clase escuela

    def Salon1(): #Metodo Void
        Materia = "Espanol "
        Maestro = "Rodolfo "
        Num_Salon = "1001 "

        salon = Materia + Maestro + Num_Salon
        return salon

    def Salon2(): #Metodo Void
        Materia = "Matematicas "
        Maestro = "Arrambide "
        Num_Salon = "1002 "

        salon = Materia + Maestro + Num_Salon
        return salon

    def Salon3(): #Metodo Void
        Materia = "Computacion "
        Maestro = "Alei "
        Num_Salon = "1003 "

        salon = Materia + Maestro + Num_Salon
        return salon

    
