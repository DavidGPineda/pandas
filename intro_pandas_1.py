import pandas as pd
print("=== PRACTICANDO PANDAS ===")

# ✅ PASO 5: Limpieza de Datos 🧹 (muy importante en IA)
# Antes de entrenar cualquier modelo de IA, los datos SIEMPRE deben limpiarse:
# Quitar datos vacíos
# Manejar datos duplicados
# Corregir errores
# Rellenar datos faltantes
# Eliminar registros sucios

# 💻 Ejercicio 5 – Dataset sucio (mini práctica)

# Crear un DataFrame con errores
data2 = {
    "Nombre": ["Ana", "Luis", None, "Pedro", "Luis"],
    "Edad": [23, None, 19, 19, 30],
    "Ciudad": ["Bogota", "MEDELLIN", "cali", None, "MEDELLIN"]
}

df2 = pd.DataFrame(data2)
print("=== Datos sucios ===")
print(df2)

# # Encontrar valores faltantes
# print("\nValores faltantes por columna:")
# print(df2.isnull().sum())

# # Eliminar filas con datos vacíos
# df_limpio = df2.dropna()
# print("\nDatos despues de eliminar filas vacias:")
# print(df_limpio)

# # Eliminar duplicados
# df_sin_duplicados = df2.drop_duplicates()
# print("\nDatos sin duplicados:")
# print(df_sin_duplicados)

# ✔️ Detectar datos faltantes (isnull())
# ✔️ Contar datos faltantes
# ✔️ Eliminar filas sucias (dropna())
# ✔️ Eliminar duplicados (drop_duplicates())

# ✅ PASO 6: Rellenar datos faltantes (muy usado en IA)
# A veces NO puedes eliminar datos faltantes porque perderías información valiosa. Lo mejor es rellenar valores vacíos con estrategias como:

# ✔️ Rellenar con la media (mean)
# ✔️ Rellenar con el valor más común (mode)
# ✔️ Rellenar texto faltante con "Desconocido"

# 💻 Ejercicio 6 – Completar datos faltantes
# print("\n=== Rellenar valroes faltantes ===")

# # Rellenar valroes numericos (Edad) con la media
# df2["Edad"] = df2["Edad"].fillna(df2["Edad"].mean())

# # Rellanar valores de texto (Nombre y Ciudad)
# df2["Nombre"] = df2["Nombre"].fillna("Desconocido")
# df2["Ciudad"] = df2["Ciudad"].fillna("SIN CIUDAD")

# print(df2)

# ✅ PASO 7: Ordenar y agrupar datos
# Esto es algo que se usa muchísimo en
# análisis y machine learning para resumir datos y encontrar patrones.

# 💻 Ejercicio 7 – Ordenar y agrupar

print("\n=== Ordenar datos por Edad (ascendente) ===")
print(df2.sort_values(by="Edad"))

print("\n=== Ordenar datos por Nombre (descendente) ===")
print(df2.sort_values(by="Nombre", ascending=False))

print("\n=== Agrupar por Ciudad y contar personas ===")
print(df2.groupby("Ciudad")["Nombre"].count())

print("\n=== Edad promedio por Ciudad ===")
print(df2.groupby("Ciudad")["Edad"].mean())


# ✔️ Ordenar información
# ✔️ Agrupar datos
# ✔️ Calcular promedios con groupby
# ✔️ Contar elementos por categoría
