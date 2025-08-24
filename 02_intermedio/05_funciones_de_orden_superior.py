#funciones jerarquicos
''''
En Python, las funciones de orden superior (higher-order functions) son aquellas que pueden recibir otras funciones como argumentos o devolver funciones como resultado.
'''
def potencia(n):
    return lambda x: x ** n

cuadrado = potencia(2)
cubo = potencia(3)

print(cuadrado(4))  # → 16
print(cubo(2))      # → 8
