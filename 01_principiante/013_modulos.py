import fichero  # importar modulo completo
import math as mate # importar una function en concreto de un modulo 
import datetime  as tiempo # importar modulo completo
# importar modulo en concreto una function
from fichero import sumas, restas,multiplicaciones,divisiones
print(sumas(5, 3))
print(restas(5, 3))
print(multiplicaciones(5, 3))
print(round(divisiones(5, 3),2))
print(mate.sqrt(16))
print(tiempo.datetime.now())
print(tiempo.datetime.now().month)