nombre = str(input("Ingrese su nombre: "))
def saludar(nombre):
    print(f"Hola, {nombre}!")
saludar(nombre)

numero_1=int(input("Ingrese un número: "))
numero_2=int(input("Ingrese otro número: "))
def sumar(numero_1, numero_2):
    return numero_1 + numero_2

print(type(numero_1))

resultado = sumar(numero_1, numero_2)
print(f"La suma de {numero_1} y {numero_2} es: {resultado}")


#nombre 
nombre_2 = str(input("Ingrese su nombre: "))
apellido_2 = str(input("Ingrese su apellido: "))
def saludar(nombre, apellido):
    return (print(f"Hola, {nombre} {apellido}!"))

#impresion multiple, numero de parametros dinamico
def varios_textos(*textos):
    return (print(textos))
varios_textos("Hola", "Mundo", "Desde", "Python")