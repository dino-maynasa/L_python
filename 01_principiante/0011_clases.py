#clases
'''
concepto para definir actuacion del codigo dentro de un area de actuacion'''
class Persona:

    #constructor
    def __init__(self, nombre, edad):
        self.__nombre = nombre
        self.__edad = edad

    def get_nombre(self):
            return self.__nombre
        
    def set_nombre(self, nombre):
            self.__nombre = nombre

    def get_edad(self):
            return self.__edad
        
    def set_edad(self, edad):
            self.__edad = edad
#carga de datos al constructor con datos de persona 1
Persona1 = Persona("Dino", 26)

Persona1.set_nombre("Daniel")
print(Persona1.get_edad())
print(Persona1.get_nombre(),"\n")

#desde acá es otra persona
#carga de datos al constructor con datos de persona 2
Persona2 = Persona("Maria", 30)
print(Persona2.get_nombre())
print(Persona2.get_edad())