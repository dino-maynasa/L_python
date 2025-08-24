### loops ###
condicion = 1
while condicion <= 100:
    if condicion % 2 == 0:
        print(f"{condicion} es un número par")
        if condicion  == 50:
            break
    condicion += 1
else: #este el uso del else es opcional
    print("El ciclo ha terminado")

#for#
print("\nCiclo for:")
for condicion in range(1, 101, 3):
    if condicion % 2 == 0:
        print(f"{condicion} es un número par")
    else:
        print(f"{condicion} es un número impar")    
