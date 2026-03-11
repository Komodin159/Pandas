import pandas as pd

edad = [25, 30, 35, 40]
print("SERIES")
serie_edad = pd.Series(edad)
print(serie_edad)
print(edad)

print("DATAFRAME")
datos = {
    "Nombre": ["Ana", "Luis", "Carlos", "Sara"],
    "Edad": [25, 30, 22, 28],
    "Ciudad": ["Bogotá", "Medellín", "Cali", "Bogotá"]
}

df = pd.DataFrame(datos)
print(df)
print("==========")
print(df.head()) #las primeras filas
print(df.head(2)) #las 2 primeras filas
print("==========")
print(df.tail()) #De la ultima a la primera
print(df.tail(2)) #Las ultimas 2 filas
print("==== INFO ====")
print(df.info()) #Muestra informacion sobre el dataframe
print("==== DESCRIBE ====")
print(df.describe()) #Muestra estadisticas descriptivas
print("===== COLUMNAS =====")
print(df.columns) #Muestra las columnas
print(df["Nombre"]) #Muestra la columna "Nombre"
print("=== SHAPE ====")
print(df.shape) #Muestra las dimensiones

print("==== ACCESO A DATOS ====")
resumen = df[["Nombre" , "Edad"]]
print(resumen) #Muestra solo las columnas "Nombre" y "Edad"

lista = [2, 3, 4, 5]
lista2 = lista
lista2.append(6)
print(lista)
print("==== MODIFICACIONDE DATAGRAME ====")
resumen["Correo"] = ["teste@cesde.net", "prueba@teste.com", None, None]
print(resumen)