#PROGRAMA QUE SOLICITE HORAS TRABAJADAS Y TARIFA POR HORA TRABAJADA
#HASTA 40 HORAS DE TRABAJO TENDRA UNA TARIFA ASIGNADA POR HORA 
#MÁS DE 40 HORAS LABORALES SE PAGARAN 1.5 VECES POR HORA EXTRA


#FUNCTION DEF
def computepay(h, r):
    if h > 40:
        p = (h - 40) * (r * 1.5) + (40*r)
    else:
        p = h*r
    return p


#INPUT STATEMENTS
hrs = input("Enter Hours: ")
hs = float(hrs)

rate = input("Enter pay per hour: ")
rt = float(rate)


#OUTPUT
p = computepay(hs, rt)
print("Pay", p)


    
    
 