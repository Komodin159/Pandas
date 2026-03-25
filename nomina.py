import os

TOPE_AUXILIO = 2000000
VALOR_AUXILIO = 160000
DEDUCCIONES = 0.08 #8%


def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

def calcular_nomina(lista_empleados):
    print("---Nomina General---")

    if not lista_empleados:
        print("No hay empleados")
        return

    print("-" * 75)

    total_nomina = 0

    for emp in lista_empleados:

        sueldo_proporcional =  (emp["Salario"] / 30) * emp["Dias"]
        auxilio = 0

        if emp ["Salario"] > TOPE_AUXILIO:
            auxilio = (VALOR_AUXILIO / 30) * emp["Dias"]

        deducciones = sueldo_proporcional * DEDUCCIONES
        neto = sueldo_proporcional + auxilio + deducciones
        total_nomina += neto

        print("Nombre empleado %s y sueldo %d con un auxilio de: %d" % (emp["Nombre"], sueldo_proporcional, auxilio))

    print("-" * 75)
    print(f"Total empleados: {total_nomina:.2f}")
    input("Pressione ENTER para sair...")

def registrar_empleado(lista_empleados):
    print("---Registro de Empleados---")

    nombre = input("Ingrese su nombre:\n")

    try:
        salario_base = float(input("Ingrese su salario mensual:"))
        dias_trabajados = int(input("Ingrese su dias trabajados(1-30):"))

        if dias_trabajados < 1 or dias_trabajados > 30:
            print("Cantidad de dias ingresados no validos")
            return

        empleado = {
        "Nombre":nombre,
        "Salario":salario_base,
        "Dias":dias_trabajados
        }
        lista_empleados.append(empleado)
        print("Empleado %s registrado con exito" % (nombre))

    except ValueError:
        print("Error, ingrese un numero valido para el salario y los dias")

def main():
    empleados = []
    while True:
        print("---- Iniciar programa ----")
        print("1. Registrar empleados")
        print("2. Procesar nomina")
        print("3. Salir")

        opcion = input("Ingrese su opcion:\n")

        if opcion == "1":
            registrar_empleado(empleados)
        elif opcion == "2":
            calcular_nomina(empleados)
        elif opcion == "3":
            print("Salir")

        else:
            print("Opcion incorrecta")

if __name__ == "__main__":
    main()