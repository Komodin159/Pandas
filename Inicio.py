#VARIABLES
print("----------VARIABLES----------")
nombre = "Juan"
numero = 3239944071
estatura = 1.77
edad = 21

#Nombre
print("Hola " + nombre +" Bienvenido")

#Nombre+Numero
print("Hola " + nombre + " tu numero es " + str(numero))
print(f"Hola {nombre} tu numero es {numero}")

#Nombre+Numero+Estatura
print(f"Hola {nombre} tu numero es {numero} y tu estatura es {estatura}")
print(f"Hola {nombre} tu numero es {numero}, tu estatura es {estatura} y la edad que tienes es {edad}")

#Tipo de dato
print(type(nombre))
print(type(numero))
print(type(estatura))
print(type(edad))

#OPERADORES ARITMETICOS
print("----------OPERADORES ARITMETICOS----------")
    #Pedir numeros
numero1 = (int(input("Introduce un numero: (1)\n")))
numero2 = int(input("Introduce un numero: (2)\n"))

#Imprimir resultados
    #suma
print(f"La suma del numero es {numero1 + numero2}")
    #resta
print(f"La resta del numero es {numero1 - numero2}")
    #multiplicacion
print(f"La muliplicacion del numero es {numero1 * numero2}")
    #division
print(f"La division del numero es {numero1 / numero2}")
    #modulo
print(f"La resto de la division de los numeros es {numero1 % numero2}")

#OPERADORES LOGICOS
print("----------OPERADORES LOGICOS----------")
'''
and =  Retorna True si ambos operandos son True
or = Retorna True si al menos uno de los operandos es True
not =  Invierte el valor booleano, convirtiendo True en False y viceversa
'''

a= True
b= False

print(a and b)

print(a or b)

print(not a)

print(not b)

#OPERADORES RACIONALES
print("----------OPERADORES RACIONALES----------")
'''
== (Igual a): Verifica si dos valores son iguales. Ej: 5 == 5 es True. ¡Importante no confundir con = (asignación)!.
!= (Distinto de): Verifica si dos valores son diferentes. Ej: 5 != 3 es True.
> (Mayor que): Verifica si el valor izquierdo es mayor que el derecho. Ej: 5 > 3 es True.
< (Menor que): Verifica si el valor izquierdo es menor que el derecho. Ej: 3 < 5 es True.
>= (Mayor o igual que): Verifica si el valor izquierdo es mayor o igual que el derecho. Ej: 5 >= 5 es True.
<= (Menor o igual que): Verifica si el valor izquierdo es menor o igual que el derecho. Ej: 3 <= 5 es True.
'''

a = 5
b = 8

print(a == b)
print(a != b)
print(a > b)
print(a >= b)
print(a < b)
print(a <= b)


#OPERADORES DE ASIGNACION
print("----------OPERADORES DE ASIGNACION----------")
'''
= (Asignación Simple): Asigna el valor de la derecha a la variable de la izquierda (ej. x = 5).
+= (Suma y asignación): Suma el valor derecho al izquierdo y actualiza la variable (ej. x += 3 es x = x + 3).
-= (Resta y asignación): Resta el valor derecho al izquierdo y actualiza (ej. x -= 2).
*= (Multiplicación y asignación): Multiplica y actualiza.
/= (División y asignación): Divide y actualiza.
%= (Módulo y asignación): Calcula el resto y actualiza.
'''

numero = 4

#numero = numero + 5=
numero += 5
print(numero)

#numero = numero - 5=
numero -= 5
print(numero)

#numero = numero * 5=
numero *= 5
print(numero)

#numero = numero / 5=
numero /= 5
print(numero)

#numero = numero % 5=
numero %= 5
print(numero)

#ACTIVIDADES

    #Pedir numeros al usuario

primer_numero = int(input("Ingrese un numero: (3)\n"))
segundo_numero =  int(input("Ingrese un numero: (4)\n"))

    #Operaciones de comparacion
print(f"¿Los numero son iguales?: {primer_numero == segundo_numero}")

print(f"¿El primero numero es menor que el segundo?: {primer_numero < segundo_numero}")

print(f"¿El segundo numero es mayor o igual que el primero?: {segundo_numero >= primer_numero}")

#CONDICIONALES
print("----------CONDICIONALES----------")

# if = si
# else = si no
# elif = si no, si (analizar varias instrucciones del programa)

