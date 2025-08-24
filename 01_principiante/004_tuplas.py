# Tuplas

mi_tupla = tuple() # declaracion de un tipo tupla.
mi_primera_tupla = () # declaracion de una tupla vacia, CONSTRUCTOR

# Tomar en cuenta que siempre se debe de definir un constructor de tupla

# una tupla es conjunto de valores
mi_tupla = ("dino", 26, 1.70, 70, 70)
print(mi_tupla[0])

print(type(mi_tupla))
print(f"longitud de la tupla: {len(mi_tupla)}")

print(f"la cantida de dato existentes de: {mi_tupla.count(70)}")

print(f"la posición de index es: {mi_tupla.index(70)}")

# Las tuplas por definición no son mutables, no se pueden modificar sus valores
mi_otra_tupla = tuple()
mi_otra_tupla = ("Maynasa", 30, 1.80, 80, 80)
suma_tuplas = mi_tupla + mi_otra_tupla #se puede realizar la suma de tuplas asignandole en una sola tupla
print(suma_tuplas)
#  se puede realizar el cambio de tipos de datos de tuplas
lista = list(mi_tupla) #convierte la tupla en una lista
print(type(lista))

# no se puede eliminar las tuplas ya que borrarlas es mutar
del mi_otra_tupla
print("Tupla eliminada correctamente")
