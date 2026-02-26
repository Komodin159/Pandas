A = True
B = True
C = True

if A and B:
    print("Verdadero")
elif A and B or C:
    print("Segunda opcion")
else:
    print("Falso")

print("----BANCO----")

edad = 0
ingreso = 0
reporte = ""
fiador = ""

edad = int(input("Ingrese su edad:\n"))
ingreso = float(input("Ingrese sus ingresos mensuales:\n"))
fiador = input("Tiene fiador? (SI/NO)\n").upper()
reporte = input("Esta usted reportado? (SI/NO)\n").upper()

tieneEdad = (edad >= 18 and edad < 75)
#ingreso = (ingreso >= 2000000.00)
tieneFiador = None 

if fiador == "SI" or ingreso >= 2000000.00:
    tieneFiador = True
else: 
    tieneFiador = False

tieneReporte = (reporte == "SI")

creditoAprovado = tieneEdad and tieneFiador and not tieneReporte

if creditoAprovado:
    creditoAprovado = "Felicitaciones"
else:
    creditoAprovado = "Lo sentimos, no cumples requisitos para tener un credito con nosotros"

print("Edad", tieneEdad)
print("Ingreso o Fiador", tieneFiador) 
print("Reporte", tieneReporte)
print(f"Estado de su credito: {creditoAprovado}.")

print(creditoAprovado)