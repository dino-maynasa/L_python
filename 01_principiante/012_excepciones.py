# Ejemplos claros de Excepciones en Python con mensajes explicativos

# 1. ZeroDivisionError
try:
    a = 10
    b = 0
    resultado = a / b
except ZeroDivisionError:
    print("ZeroDivisionError: No se puede dividir 10 entre 0.")

# 2. ValueError
try:
    numero = int("hola")
except ValueError:
    print("ValueError: No se puede convertir la cadena 'hola' en un número entero.")

# 3. TypeError
try:
    a = "10"
    b = 5
    suma = a + b
except TypeError:
    print("TypeError: No se puede sumar un texto '10' con un número 5.")

# 4. IndexError
try:
    lista = [1, 2, 3]
    print(lista[5])
except IndexError:
    print("IndexError: El índice 5 no existe en la lista [1, 2, 3].")

# 5. KeyError
try:
    diccionario = {"nombre": "Juan", "edad": 25}
    print(diccionario["apellido"])
except KeyError:
    print("KeyError: La clave 'apellido' no existe en el diccionario.")

# 6. AttributeError
try:
    texto = 123
    texto.lower()
except AttributeError:
    print("AttributeError: Los números enteros no tienen el método 'lower()'.")

# 7. FileNotFoundError
try:
    archivo = open("archivo_inexistente.txt", "r")
except FileNotFoundError:
    print("FileNotFoundError: No se encontró el archivo 'archivo_inexistente.txt'.")

# 8. ImportError
try:
    import modulo_inexistente
except ImportError:
    print("ImportError: No se pudo importar el módulo 'modulo_inexistente'.")

# 9. ModuleNotFoundError
try:
    import modulo_desconocido
except ModuleNotFoundError:
    print("ModuleNotFoundError: El módulo 'modulo_desconocido' no existe.")

# 10. NameError
try:
    print(variable_no_definida)
except NameError:
    print("NameError: La variable 'variable_no_definida' no ha sido definida.")

# 11. StopIteration
def generador():
    yield 1

gen = generador()
try:
    next(gen)
    next(gen)
except StopIteration:
    print("StopIteration: Se alcanzó el final del generador y no hay más elementos.")

# 12. OverflowError
try:
    import math
    resultado = math.exp(1000)
except OverflowError:
    print("OverflowError: El número resultante es demasiado grande para manejarlo.")

# 13. MemoryError
try:
    a = "a" * (10**10)
except MemoryError:
    print("MemoryError: No hay suficiente memoria para crear esta cadena gigante.")

# 14. RuntimeError
try:
    raise RuntimeError("Este es un error de ejecución simulado.")
except RuntimeError as e:
    print(f"RuntimeError: {e}")

# 15. AssertionError
try:
    x = 10
    assert x < 5, "x no es menor que 5"
except AssertionError as e:
    print(f"AssertionError: {e}")

# 16. EOFError
try:
    raise EOFError("Simulación de EOFError al no recibir datos de entrada.")
except EOFError as e:
    print(f"EOFError: {e}")

# 17. FloatingPointError
try:
    import numpy as np
    np.seterr(all='raise')
    a = np.array([1.0])
    b = np.array([0.0])
    c = a / b
except FloatingPointError:
    print("FloatingPointError: División por cero detectada en operación de punto flotante.")

# 18. NotImplementedError
try:
    def metodo():
        raise NotImplementedError("Método no implementado aún.")
    metodo()
except NotImplementedError as e:
    print(f"NotImplementedError: {e}")

# 19. OSError
try:
    raise OSError("Simulación de error del sistema.")
except OSError as e:
    print(f"OSError: {e}")

# 20. BlockingIOError
try:
    raise BlockingIOError("Simulación de operación bloqueante no permitida.")
except BlockingIOError as e:
    print(f"BlockingIOError: {e}")

# 21. ConnectionError
try:
    raise ConnectionError("Simulación de fallo de conexión a red.")
except ConnectionError as e:
    print(f"ConnectionError: {e}")

# 22. UnicodeError
try:
    b = b'\x80'
    b.decode('utf-8')
except UnicodeError:
    print("UnicodeError: El byte '\x80' no puede decodificarse usando UTF-8.")

# 23. RecursionError
try:
    def recursivo():
        return recursivo()
    recursivo()
except RecursionError as error:
    print(f"RecursionError: {error}")

print("\nTodas las excepciones demostradas con mensajes claros.")


# Ejemplo completo de try, except, else y finally

# Datos cargados
numeros = [10, 5, 0]
indice = 1  # Cambiar a 2 para probar división por cero

try:
    # Intentamos realizar una operación
    a = numeros[indice]          # Número elegido
    b = numeros[indice + 1]      # Siguiente número
    resultado = a / b
except ZeroDivisionError:
    # Se ejecuta si ocurre una división por cero
    print(f"Error: No se puede dividir {a} entre {b} (ZeroDivisionError).")
except IndexError:
    # Se ejecuta si el índice no existe en la lista
    print(f"Error: Índice fuera de rango. Intentaste acceder a posiciones {indice} y {indice + 1}.")
else:
    # Se ejecuta si NO ocurre ninguna excepción
    print(f"Operación exitosa: {a} dividido entre {b} es {resultado}.")
finally:
    # Se ejecuta siempre, haya ocurrido o no un error
    print("Operación finalizada, recursos liberados si los hubiera.")
