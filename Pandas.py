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
print(df)

data = pd.read_csv("MOCK_DATA.csv")
print(data.head())
print(data.tail())
print(data.info())

data ["Precio_Total"] = data["Cantidad"] * data["Precio_Unitario"]
print(data[["Precio_Total"]])

promedio_Total = data["Precio_Total"].mean()
suma_Total= data["Precio_Total"].sum()

print(f"El promedio es: {promedio_Total:.2f}")
print(f"La suma de precios es: {suma_Total:.2f}")
data = pd.read_csv("MOCK_DATA (1).csv")
print(data.info())

print(data.isna())

cant_nulos = data.isna().sum()
print(cant_nulos)

print("===========================")
cant_nulos = data.duplicated().sum()
print(cant_nulos)

print("===========================")
copiaDecopia = data.dropna()
print(copiaDecopia.info())
print("===========================")
data ["Vendedor"] = data["Vendedor"].fillna("N/A")
print(data["Vendedor"])

print("===========================")
filtroCiudades = data[data["Ciudad"] == "New York City"]
print(filtroCiudades)

print("===========================")
data["Producto"] = data["Producto"].str.upper()
print(data["Producto"])

data2 = data[["Producto", "Cantidad", "Precio_Unitario"]]
print(data2)
