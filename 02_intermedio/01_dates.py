import datetime as tiempo
fecha = tiempo.datetime.now()
print(fecha.year)
proxima_fecha = fecha.year + 1
print(proxima_fecha-1)

for i in range(0,5,1):
    print(f"El año actual es: {fecha.year}, el próximo año será: {proxima_fecha}")
    if proxima_fecha % 2 == 0:
        print(f"El año {proxima_fecha} es par")
    else: 
        print(f"El año {proxima_fecha} es impar")
    proxima_fecha += 1

from datetime import timedelta 
fecha_str = input("Introduce una fecha (dd/mm/yyyy): ")
datos_fecha = timedelta()
print(datos_fecha)