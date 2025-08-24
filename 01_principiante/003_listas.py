#listas
# definiendo desde cero las listas
my_list=list()  #constructor literal para las listas.
my_other_list=[] #usa la notación literal para las listas

print(f"la medida de la lista es: {len(my_list)}")
print(f"El tipo de dato de la primera lista es: {type(my_list)}")

print(f"la medida de la lista es: {len(my_list)}")
print(f"El tipo de dato de la segunda lista es: {type(my_other_list)}")

#una lista es un conjunto de datos, que cada una tiene una posicion


edades = [25, 30, 35, 40]
print("La lista de edades es:", edades)
print(len(edades))  # Imprime la longitud de la lista

# lista en edades de datos
datos_Dino = [26, "Dino", 1.73, 70]
print(type(datos_Dino))
print(datos_Dino)

# acceder a la lista por separados
# las cosas que aprendemos son listas  o array

edades = [31,33,33,33,34,56,45]
print(edades[3])

# diferencia entre tuplas, listas y array
# para definir las tuplas se utiliza las palabras reservadas tupla()
# cadena = tupla(); mientra que listas con list() o []

print(edades.count(33))  # cuenta cuantas veces aparece el 33 en la lista

#impresion de desempaque de elementos
edad, nombre, estatura, peso = datos_Dino #esta haciendo referencia a la lista creada datos_Dino
print(nombre)

datos_Dino.append("Bolivia") #agrega un elemento al final de la lista
print(datos_Dino)
datos_Dino.insert(1, "Celeste") #inserta un elemento en la posición 1
print(datos_Dino)
datos_Dino.remove(datos_Dino[2]) #remueve el elemento en la posición 2, solo actua con datos encontrados dentro de la lista
print(datos_Dino)
datos_Dino.pop() #remueve el último elemento de la lista
print(datos_Dino)
dato_eliminado=datos_Dino.pop(1) #remueve el elemento en la posición 1
print(dato_eliminado)
print(datos_Dino)
print(len(datos_Dino)) #muestra la longitud de la lista
del datos_Dino[0] #elimina el elemento en la posición 0, elimina por indice
print(datos_Dino)

datos_Dino1 = datos_Dino.copy() #esta copiando la lista en una nueva y esta siendo asignado a una nueva variable
print(datos_Dino1)
datos_Dino.clear() #elimina todos los elementos de la lista
print(datos_Dino)

datos_Dino1.append(100) #ordena la lista de forma ascendente
print(datos_Dino1)
datos_Dino1.sort() #ordena la lista de forma ascendente
print(datos_Dino1)
datos_Dino1.reverse() #ordena la lista de forma descendente
print(datos_Dino1)

def sumar_lista(lista):
    return sum(lista)
