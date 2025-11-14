# gestion_registros.py
# Actividad M12: Lectura de registros y conversión de datos

import csv
import json

# PARTE 1: Lector de Registros (Texto Plano)

# 1. Crear el archivo mi_registro.txt con 4 líneas iniciales
with open("mi_registro.txt", "w", encoding="utf-8") as archivo:
    archivo.write("Usuario: Ana - Ciudad: Madrid\n")
    archivo.write("Usuario: Marleny - Ciudad: Barcelona\n")
    archivo.write("Usuario: Sandra - Ciudad: Sevilla\n")
    archivo.write("Usuario: Enrique - Ciudad: Valencia\n")

# 2. Leer y filtrar líneas que contienen "Madrid" o "Sevilla"
with open("mi_registro.txt", "r", encoding="utf-8") as archivo:
    lineas_registro = archivo.readlines()

print("🗂️ Usuarios en Madrid o Sevilla:")
for linea in lineas_registro:
    if "Madrid" in linea or "Sevilla" in linea:
        print(linea.strip())

# 3. Anexar nueva línea al final del archivo
with open("mi_registro.txt", "a", encoding="utf-8") as archivo:
    archivo.write("Usuario: Elena - Ciudad: Bilbao\n")

# 4. Confirmar que Elena fue añadida
print("\n📄 Registro actualizado:")
with open("mi_registro.txt", "r", encoding="utf-8") as archivo:
    for linea in archivo:
        print(linea.strip())

# PARTE 2: Conversor de Datos (CSV y JSON)

# 1. Crear inventario_productos.csv
with open("inventario_productos.csv", "w", newline="", encoding="utf-8") as archivo_csv:
    writer = csv.writer(archivo_csv)
    writer.writerow(["ID", "Nombre", "Precio", "Stock"])
    writer.writerow([101, "Monitor", 150.99, 25])
    writer.writerow([102, "Teclado", 35.50, 150])
    writer.writerow([103, "Raton", 18.00, 300])

# 2. Leer CSV e imprimir productos con Stock < 100
print("\n📦 Productos con stock menor a 100:")
with open("inventario_productos.csv", "r", encoding="utf-8") as archivo_csv:
    reader = csv.reader(archivo_csv)
    next(reader)  # Saltar encabezado
    for fila in reader:
        stock = int(fila[3])
        if stock < 100:
            print(f"Producto: {fila[1]} - Stock: {stock}")

# 3. Crear diccionario y guardar como JSON
nuevo_producto = {
    "ID": 104,
    "Nombre": "Webcam",
    "Precio": 45.99,
    "Stock": 50
}

with open("producto_nuevo.json", "w", encoding="utf-8") as archivo_json:
    json.dump(nuevo_producto, archivo_json, indent=4)

# 4. Leer JSON y mostrar Nombre y Precio
with open("producto_nuevo.json", "r", encoding="utf-8") as archivo_json:
    data_cargada = json.load(archivo_json)

print("\n🧾 Producto cargado desde JSON:")
print(f"Nombre: {data_cargada['Nombre']}")
print(f"Precio: {data_cargada['Precio']}")