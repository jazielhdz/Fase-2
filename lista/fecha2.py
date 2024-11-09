import datetime
hoy = datetime.date.today()
prox_semana = hoy + datetime.timedelta(days= 7)
print(prox_semana)
10/10/2024

año_ant = hoy - datetime.timedelta(days= 365)
print(año_ant)