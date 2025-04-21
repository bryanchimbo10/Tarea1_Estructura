#1.Solicitar al usuario que ingrese un número y presente si es par o impar.

print('Ejercicio para saber si un numero es par o impar')
numero1 = int(input("Ingrese un numero:"))
if numero1 % 2 == 0:
    print("El numero es Par ")
else:
    print('El número es impar')
#2. Solicitar que el usuario ingrese 3 números y presente cuál es el mayor.
numero2 = int(input("Ingrese un numero:"))
numero3 = int(input("Ingrese un numero:"))
numero4 = int(input("Ingrese un numero:"))

mayor= max(numero2,numero3,numero4)
print(f'El numero mayor es; {mayor}')
print('------------------------------------------------------------')

#3. Solicitar al usuario que ingrese 2 valores y un operador matemático (+ - * /) y presente
# la operación matemática indicada.

numero5 = int(input("Ingrese un numero:"))
numero6 = int(input("Ingrese un numero:"))
operador =input("Ingrese un operador ´+,-,*,/´:")
if operador == "+":
    suma = numero5+numero6
    print(f'La sumas es: {suma}')
elif operador== '-':
    resta = numero5 - numero6
    print(f'La sumas es: {resta}')
elif operador== '*':
    multi = numero5 * numero6
    print(f'La sumas es: {multi}')
else:
    div = numero5 / numero6
    print(f'La sumas es: {div}')
print('------------------------------------------------------------')

#4. Solicitar al usuario que ingrese un año y presente si el año es bisiesto o no.
año = int(input("Ingresá un año: "))
if (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0):
    print("El año es bisiesto")
else:
    print("El año no es bisiesto")
print('------------------------------------------------------------')

#6. Presente la impresión de números del 10 al 50
# Imprimir números del 0 al 100
for numero7 in range(101):
    print(numero7)
print('------------------------------------------------------------')
for numero8 in range(10,51):
    print(numero8)
#7. Presente la impresión de números del 80 al 50 de 5 unidades en 5 unidades de forma descendente.
for i in range(80, 49, -5):
    print(i)
#8. Solicitar al usuario que ingrese un número y realizar la suma desde el 0 hasta llegar al número del usuario.
numero9 = int(input("Ingrese un número: "))
suma1 = 0

for i in range(numero9 + 1):
    suma1 += i

print(f"La suma desde 0 hasta {numero9} es: {suma1}")
print('------------------------------------------------------------')

#9. Solicitar al usuario que ingrese un número y presentar la tabla de multiplicar de ese número.
numero10 = int(input("Ingrese un número: "))

print(f"Tabla de multiplicar del {numero10}:")

for i in range(1, 11):
    resultado = numero10 * i
    print(f"{numero10} x {i} = {resultado}")
print('------------------------------------------------------------')

#10. Presentar en pantalla el promedio de una lista empleando (for in y range)
cantidad = int(input("¿Cuántos números desea ingresar? "))
numeros = []

for i in range(cantidad):
    num = float(input(f"Ingrese el número {i + 1}: "))
    numeros.append(num)

suma = 0
for num in numeros:
    suma += num

promedio = suma / cantidad
print(f"El promedio es: {promedio}")
print('------------------------------------------------------------')

#11. Realizar la búsqueda de un elemento ingresado por el usuario dentro de un arreglo.
arreglo1 = input("Ingrese elementos separados por espacio: ").split()

buscado = input("Ingrese el elemento a buscar: ")
encontrado1 = False
for elemento1 in arreglo1:
    if elemento1 == buscado:
        encontrado1 = True
        break
if encontrado1:
    print("Elemento encontrado en el arreglo.")
else:
    print("Elemento no encontrado.")
print('------------------------------------------------------------')
#12. Realizar la inversión de un arreglo.
arreglo = [1, 2, 3, 4, 5]
invertido = []

for i in range(len(arreglo) - 1, -1, -1):
    invertido.append(arreglo[i])

print("Arreglo invertido:", invertido)
print('------------------------------------------------------------')

#13. Presente en pantalla la frecuencia de los elementos que se encuentran dentro de un array.
arreglo2 = input("Ingrese elementos separados por espacio: ").split()
for elemento2 in set(arreglo2):
    frecuencia = arreglo2.count(elemento2)
    print(f"{elemento2}: {frecuencia} vez/veces")
print('------------------------------------------------------------')

#14. Elimine los elementos duplicados dentro de un array.
arreglo3 = input("Ingrese elementos separados por espacio: ").split()

sin_duplicados = []
for elemento3 in arreglo3:
    if elemento3 not in sin_duplicados:
        sin_duplicados.append(elemento3)

print("Arreglo sin duplicados:", sin_duplicados)
print('------------------------------------------------------------')

#15. Ordene los elementos de un array sin emplear el método sort()
entrada = input("Ingrese números separados por espacio: ")
arreglo5 = list(map(int, entrada.split()))
n = len(arreglo5)
for i in range(n):
    for j in range(0, n - i - 1):
        if arreglo5[j] > arreglo5[j + 1]:
            arreglo5[j], arreglo5[j + 1] = arreglo5[j + 1], arreglo5[j]  # Intercambiar

print("Arreglo ordenado:", arreglo5)

print('------------------------------------------------------------')
