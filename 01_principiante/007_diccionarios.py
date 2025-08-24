#diccionarios
mi_diccionario = dict()

mi_diccionario = {"Nombre": "Dino",
                  "Edad": 26,
                  "Estatura": 1.75,
                  "Lenguajes": {"Python", "Java", "Kotlin"}
                  }
print(len(mi_diccionario))
print(mi_diccionario)
print(mi_diccionario["Nombre"])
mi_diccionario["Nombre"] = "Daniel"
print(f"El nombre modificado es: {mi_diccionario["Nombre"]}")

# agregar valor al diccionario
mi_diccionario["Lenguaje Favorito"] = "Python"
print(mi_diccionario["Lenguaje Favorito"])

# Eliminar un elemento del diccionario
del mi_diccionario["Lenguaje Favorito"]
print(mi_diccionario)

# Preguntar si un dato esta en el diccionario
print("Edad" in mi_diccionario)  # True

# Dupliucar en otro elemento
mi_diccionario_2 = mi_diccionario.copy()
print(mi_diccionario_2)

print(mi_diccionario.get("Nombre"))  # Obtener el valor de la clave "Nombre"
print(mi_diccionario.get("Apellido", "No existe"))  # Obtener el valor de la clave "Apellido" con valor por defecto
print(mi_diccionario.items())
print(f"Las claves del diccionario son: {mi_diccionario.keys()}")  # Obtener las claves del diccionario
print(f"los valores del diccionario son: {mi_diccionario.values()}")  # Obtener los valores del diccionario
print(mi_diccionario.pop("Edad"))  # Elimina la clave "Edad" y devuelve su valor
print(mi_diccionario.fromkeys)
print(mi_diccionario)