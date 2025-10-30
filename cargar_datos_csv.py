import pandas as pd
df = pd.read_csv("ventas.csv", sep=";")
print(df.head())

# # Ver información general
# print("\nInfo:")
# df.info()
# # Ver estadísticas básicas
# print("\ndescribe:")
# print(df.describe())
# # Saber filas y columnas
# print("\nShape:")
# print(df.shape)


# 💾 MÓDULO 2 — Guardar DataFrames (CSV / Excel)

# 🧠 PASO 1 — Crear un nuevo DataFrame filtrado

# Filtrar por condicion
# df_filtrado = df[df["Ventas"] > 600]

# print("\nVentas mayores a 600:")
# print(df_filtrado)

# 💾 PASO 2 — Guardar como archivo CSV

# df_filtrado.to_csv("ventas_filtradas.csv", index=False)

# 📊 PASO 3 — Guardar como archivo Excel
# Necesitas tener instalado openpyxl
# df_filtrado.to_excel("ventas_filtradas.xlsx",
#                      index=False, sheet_name="Resumen")


# 🔍 MÓDULO 3 — Filtrado avanzado con loc e iloc
# Aprender a seleccionar filas y columnas de un DataFrame de manera precisa.

# 🧩 Conceptos clave
# loc → filtra por nombre de columna o condición lógica.
# iloc → filtra por posición numérica(como en una lista de Python).

# 📘 PASO 1 — Usar loc con condiciones
# Ventas mayores a 700
# print("\nVentas mayores a 700")
# filtro1 = df.loc[df["Ventas"] > 700]
# print(filtro1)
# 📘 PASO 2 — Filtrar varias condiciones
# Ventas mayores a 700 y vendedor "Luis"
# print("\nVentas > 700 y vendedor == 'Luis'")
# filtro2 = df.loc[(df["Ventas"] > 700) & (df["Vendedor"] == "Luis")]
# print(filtro2)

# 📘 PASO 3 — Seleccionar columnas específicas con loc
# Solo columnas Fecha y Ventas, pero de Ana
# print("\nColumnas Fecha y Ventas de Ana:")
# filtro3 = df.loc[df["Vendedor"] == "Ana", ["Fecha", "Ventas"]]
# print(filtro3)

# 📘 PASO 4 — Seleccionar por posición con iloc
# Primeras 3 filas y primeras 2 columnas
# print("\nPrimeras 3 filas y primeras 2 columnas:")
# filtro4 = df.iloc[0:3, 0:2]
# print(filtro4)

# 🧩 RETO 3 — Tu turno 💪
# print("\nVentas de ana > 500, colum fecha y ventas:")
# ana1 = df.loc[(df["Vendedor"] == "Ana") & (
#     df["Ventas"] > 500), ["Fecha", "Ventas"]]
# print(ana1)

# print("\nLas 3 primeras filas y solo las 2 primeras columnas.")
# ana2 = df.iloc[0:3, 0:2]
# print(ana2)

# ⚙️ MÓDULO 4 — Funciones apply() y lambda
# Aprender a transformar columnas sin usar bucles (for), aplicando funciones directamente sobre los datos.
# 🧠 Concepto clave
# apply() permite ejecutar una función (normal o lambda) sobre cada valor de una columna o fila.

# 📘 PASO 1 — Crear una nueva columna
# Vamos a calcular la comisión del 10 % de cada venta:
# df["Comision"] = df["Ventas"].apply(lambda x: x * 0.10)
# print(df)

# # 📘 PASO 2 — Crear una columna derivada
# # Ahora calculamos las ventas netas (ventas menos comisión):
# df["Ventas_netas"] = df["Ventas"] - df["Comision"]
# print(df)

# # 📘 PASO 3 — Calcular totales o resúmenes
# total_neto = df["Ventas_netas"].sum()
# print("Total de ventas netas:", total_neto)

# 🧩 RETO 4 — Tu turno 💪

# 🗓️ MÓDULO 5 — Trabajo con fechas (datetime)
# 🎯 Objetivo
# Aprender a convertir columnas de texto en fechas reales y extraer año, mes, día, etc. para análisis temporal.
# 📘 PASO 1 — Convertir la columna Fecha a tipo datetime

df["Fecha"] = pd.to_datetime(df["Fecha"], dayfirst=True)
print(df.info())

# 📘 PASO 2 — Extraer partes de la fecha
# Una vez que Fecha es datetime, puedes sacar información útil:
df["Año"] = df["Fecha"].dt.year
df["Mes"] = df["Fecha"].dt.month
df["Día"] = df["Fecha"].dt.day

print(df)

# 📘 PASO 3 — Filtrar por mes (ejemplo práctico)
ventas_enero = df[df["Mes"] == 1]
print(ventas_enero)

# 📘 PASO 4 — Calcular promedios o totales por mes
promedio_enero = df.loc[df["Mes"] == 1, "Ventas"].mean()
print("Promedio de ventas en enero:", promedio_enero)
