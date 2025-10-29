import pandas as pd
import matplotlib.pyplot as plt

ventas = {
    "Producto": ["Laptop", "Mouse", "Teclado", "Monitor", "Laptop", "Mouse", "Parlantes", "Monitor"],
    "Precio": [3500, 80, 120, 900, 3500, 80, 200, 900],
    "Cantidad": [1, 3, 2, 1, 2, 1, 1, 2],
    "Ciudad": ["Bogotá", "Medellín", "Cali", "Bogotá", "Bogotá", "Medellín", "Cali", "Cali"]
}

df = pd.DataFrame(ventas)
print("=== DATASET ORIGINAL ===")
print(df)

# PASO 2: Agregar una columna nueva (Valor Total)

df["Valor_total"] = df["Precio"] * df["Cantidad"]
print("\n=== Valor total por venta ===")
print(df)

# ✅ PASO 3: Ventas totales por producto
# === Ventas totales por producto ===
ventas_por_producto = df.groupby("Producto")["Valor_total"].sum()
print("\n=== Ventas totales por producto ===")
print(ventas_por_producto)

# ✅ PASO 4: Ventas totales por ciudad
ventas_por_ciudad = df.groupby("Ciudad")["Valor_total"].sum()
print("\n=== Ventas totales por Ciudad ===")
print(ventas_por_ciudad)

# === Gráfico ventas por producto ===
ventas_por_producto.plot(kind="bar", title="Ventas Totales por Producto")
plt.xlabel("Producto")
plt.ylabel("Ventas ($)")
plt.show()
