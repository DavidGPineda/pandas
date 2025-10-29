import pandas as pd
print("=== PRACTICANDO PANDAS ===")
# print("Pandas funcionando. Versión:", pd.__version__)

# Mi pimer DataFrame
# Creaste una estructura tabular en Pandas llamada DataFrame.
# Cada columna tiene un nombre (Nombre, Edad, Ciudad).
# Cada fila tiene un índice automático (0, 1, 2, 3).
# Crear un DataFrame
# data = {
#     "Nombre": ["Ana", "Luis", "Pedro", "Sofia"],
#     "Edad": [23, 30, 19, 25],
#     "Ciudad": ["Bogota", "Medellin", "Cali", "Barranquilla"]
# }

# df = pd.DataFrame(data)

# print(df)

# 👉 Siguiente paso: explorar el DataFrame
# ✅ Ver columnas
# ✅ Seleccionar columnas
# ✅ Seleccionar filas
# ✅ Entender índices

# print("\nColumnas del DataFrame:")
# print(df.columns)

# print("\nSeleccionar columna 'Nombre':")
# print(df["Nombre"])

# print("\nSeleccionar varias columnas (Nombre y Ciudad):")
# print(df[["Nombre", "Ciudad"]])

# print("\nSeleccionar fila por indice (fila 0):")
# print(df.iloc[0])

# print("\nSeleccionar varias fila (0, 2):")
# print(df.iloc[0:3])

# ✔️ Cómo crear un DataFrame
# ✔️ Cómo ver sus columnas
# ✔️ Cómo seleccionar columnas
# ✔️ Cómo seleccionar filas con iloc
# ✔️ Cómo entender índices

# ✅ PASO 3: Filtrar datos (muy importante)

# 💻 Ejercicio 3 – Filtros básicos

# print("\nPersonas mayores de 21 años:")
# print(df[df["Edad"] > 21])

# print("\nPersonas que viven en Medellín:")
# print(df[df["Ciudad"] == "Medellin"])

# print("\nPersonas entre 20 y 30 años:")
# print(df[(df["Edad"] >= 20) & (df["Edad"] <= 30)])

# print("\n :")
# print()

# ✅ Aprendiste a filtrar usando condiciones
# ✅ Usaste ==, >, >=, & (AND lógico)
# ✅ Esto es clave para análisis de datos y preparación para IA 🔥


# 🚀 PASO 4: Crear nuevas columnas
# Esto es clave cuando transformas datos para IA o Machine Learning. Vamos con práctica.

# Crear una nueva columna "Año de nacimiento"
# df["Año_nacimiento"] = 2025 - df["Edad"]
# print("\nNueva columna calculada (Año de nacimiento):")
# print(df)

# # Crear columna categoria
# df["Mayor_de_edad"] = df["Edad"] >= 18
# print("\n¿Son mayores de edad?:")
# print(df[["Nombre", "Mayor_de_edad"]])

# Crear una nueva columna con años hasta los 30
# df["Años_para_30"] = 30 - df["Edad"]
# print("\nNueva columna 'Años_para_30':")
# print(df)

# # Crear columna con la inicial del nombre
# df["Inicial"] = df["Nombre"].str[0]
# print("\nColumna 'Inicial':")
# print(df[["Nombre", "Inicial"]])

# # Modificar una columna (convertir Ciudad a mayúsculas)
# df["Ciudad"] = df["Ciudad"].str.upper()
# print("\nCiudad en mayúsculas:")
# print(df)

# ✅ Creación de columnas
# ✅ Cálculos con datos
# ✅ Condiciones lógicas
# ✅ Transformación de texto
# ✅ Manipulación real de DataFra
