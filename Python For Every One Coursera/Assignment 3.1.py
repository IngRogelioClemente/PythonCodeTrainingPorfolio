#Input values; 45 hours, 10.50 per hour
#Se paga por tarifa hasta 40 horas
#Más de 40 horas se paga la tarifa 1.5 veces por hora

hrs = input("Enter Hours: ")
h = float(hrs)

pay = input("Enter pay per hour: ")
p = float(pay)

if h <= 40:
    print(h * p)
elif h > 40:
    exh = h - 40
    exp = 1.5 * p
    ex = exh * exp
    h = 40
    print(h * p + ex)
    
    
    