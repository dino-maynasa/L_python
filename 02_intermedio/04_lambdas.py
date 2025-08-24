from functools import reduce

# 1. Lambda básica (suma)
s = lambda a, b: a + b
print("1. Suma con lambda:", s(5, 3))

# 2. Ordenar con sorted usando lambda
numeros = [(1, 'uno'), (3, 'tres'), (2, 'dos')]
ordenados = sorted(numeros, key=lambda x: x[0])
print("2. Ordenados por primer valor:", ordenados)

# 3. Usar lambda con map (cuadrados)
lista = [1, 2, 3, 4, 5]
cuadrados = list(map(lambda x: x**2, lista))
print("3. Cuadrados con map:", cuadrados)

# 4. Usar lambda con filter (pares)
pares = list(filter(lambda x: x % 2 == 0, lista))
print("4. Números pares con filter:", pares)

# 5. Usar lambda con reduce (producto)
producto = reduce(lambda x, y: x * y, lista)
print("5. Producto con reduce:", producto)

# 6. Función condicional
mayor = lambda a, b: a if a > b else b
print("6. El mayor entre 10 y 20 es:", mayor(10, 20))

# 7. Ordenar lista de diccionarios
personas = [
    {"nombre": "Ana", "edad": 25},
    {"nombre": "Luis", "edad": 30},
    {"nombre": "Marta", "edad": 20}
]
ordenado = sorted(personas, key=lambda p: p["edad"])
print("7. Personas ordenadas por edad:", ordenado)

# 8. Función generadora rápida (potencias)
potencia = lambda n: lambda x: x ** n
cuadrado = potencia(2)
cubo = potencia(3)
print("8. Cuadrado de 4:", cuadrado(4))
print("   Cubo de 2:", cubo(2))
