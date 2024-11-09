from datetime import date  
date.today()
hoy = date.today()
print(f"el dia de hoy es: {hoy}")

print(hoy.year)

print(hoy.day)

print(hoy.month)

print(hoy.strftime ("%d-%m-%Y"))

print(hoy.strftime("%B, %d, %Y"))

print(hoy.strftime("%m-%d-%y"))

print(hoy.strftime("%b,%d,%y"))

print(hoy.strftime("%d-%B-%Y"))

from datetime import datetime

fecha = datetime.strptime("03/10/2024", "%d/%m/%Y") 
print(fecha)

from datetime import date 
date.today()



