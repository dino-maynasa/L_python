#list comprensión

mi_lista = []
valor = int(input("Ingrese un valor a elevar: "))
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
cuadrados = [numero ** valor for numero in numeros]
print((cuadrados))