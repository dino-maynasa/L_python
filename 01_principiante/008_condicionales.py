### condicionales###
'''dentro de las condicionales se puede aplicar las tablas de verdad:
- Si A es verdadero y B es verdadero, entonces A y B es verdadero.
- Si A es verdadero y B es falso, entonces A y B es falso.
- Si A es falso y B es verdadero, entonces A y B es falso.
- Si A es falso y B es falso, entonces A y B es falso.
- Si A es verdadero o B es verdadero, entonces A o B es verdadero.
- Si A es falso o B es falso, entonces A o B es verdadero.
- Si A es verdadero y B es falso, entonces A o B es verdadero.
'''
valor = False
if valor == True:
    print("El valor es verdadero")
else:
    print("El valor es falso")

edad = int(input("Ingrese su edad: "))
if edad >=0 and edad <= 2:
    print("Eres mayor de Bebé")
elif edad > 2 and edad <= 12:
    print("Eres un niño")
elif edad > 12 and edad <= 18:
    print("Eres un adolescente")
elif edad > 18 and edad <= 60:
    print("Eres un adulto")
elif edad > 60:
    print("Eres un anciano")

#otra prueba de código
numero = int(input("Ingrese un número: "))
if numero % 2 == 0:
    print(f"El número {numero} es par")
else:
    print(f"El número {numero} es impar")

valor_1 = "M"
valor_2 = "g"
if valor_1 =="k" or  valor_2 == "ñ":
    print("Verdadero")
else:
    print("Falso")

cadenas = "jlk"
if not cadenas:
    print("La cadena no está vacía")
else:
    print("La cadena está vacía")
    # Se puede verificar si la cadena está vacía o llena