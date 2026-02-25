def main():
    print("Inicio Programa")
    producto = {}

    nombre = input("Ingrese el nombre del producto:\n")
    precio = float(input("Ingrese el precio del producto:\n"))
    cantidad = int(input("Ingrese la cantidad del producto:\n"))

    producto["nombre"] = nombre
    producto["precio"] = precio
    producto["cantidad"] = cantidad
    print("El diccionario es:",producto)
    print("Finalizo el programa")


if __name__ == "__main__":
    main()