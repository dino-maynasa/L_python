# sets
mi_set = set() # declaración de un conjunto
mi_primer_set = set() # declaración de un conjunto vacío, CONSTRUCTOR
# otra manera de tambien definir los sets es con {}
mi_set = {"dino", 26, 1.70, 70, 70}

# Tomar en cuenta que siempre se debe de definir un constructor de conjunto

# un conjunto es un conjunto de valores únicos
mi_set = {"dino", 26, 1.70, 70, 70}
print(mi_set)

mis_sets = mi_set.copy()  # copia el conjunto en una nueva variable

print(type(mi_set))
print(f"longitud del conjunto: {len(mi_set)}")

mi_set.add("nuevo valor")
print(mi_set)

mi_set.remove(70)
print(mi_set)

# no se puede eliminar un conjunto ya que borrarlas es mutar
del mi_set
print("Conjunto eliminado correctamente")
# se puede realizar la conversión de un conjunto a una lista
lista = list(mis_sets)
print(type(lista))
# se puede realizar la conversión de un conjunto a una tupla
tupla = tuple(mis_sets)
print(type(tupla))
# los almacenamientos dentro de los sets son  desordenados, no tienen un índice como las listas o tuplas
print(mis_sets)
# un dato en set no admite duplicados, por lo tanto si se agrega un dato que ya existe no se agregará
mis_sets.add(75)
print(mis_sets)
mis_sets.add(75)
print(mis_sets)

# se tiene la posibilidad de realizar las busquedas
print("dino" in mis_sets)

#se puede realizar la eliminación de datos 
mis_sets.discard(26)  # elimina el elemento 26 si existe, no genera error si no existe+
print(mis_sets)
# se puede realizar la eliminación de todos los elementos del conjunto
mis_sets.clear()
print(len(mis_sets))

mi_set2 = {1, 2, 3}
mi_set2.add(4)  # agrega el elemento 4 al conjunto
print(mi_set2)
mi_set2.update([5, 6])  # agrega múltiples elementos al conjunto
mi_set3 = {5, 6, 7, 8}

mi_set4 = mi_set2.union(mi_set3)  # une dos conjuntos
print(mi_set4)
print(mi_set2.intersection(mi_set3))  # intersección de dos conjuntos
print(mi_set2.difference(mi_set3))  # diferencia entre dos conjuntos

mi_set5 = mi_set4.union(mi_set3) #no puede unir por que no se puede repetir
print(mi_set5)