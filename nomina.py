import os

def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

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


if __name__ == "__main__":
    pass