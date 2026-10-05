# Ejercicio 17 — Ventas en CSV
# Escribe resumen_ventas(ruta, ventas), que:

# reciba ventas, una lista de tuplas (producto, unidades, precio_unitario),
# escriba un CSV en ruta con la cabecera producto,unidades,precio,
# lo vuelva a leer con csv.DictReader,
# devuelva un diccionario {producto: total_facturado} redondeado a 2 decimales. 
# Si un producto aparece varias veces, se acumula.
# Recuerda: lo que lees del CSV es texto.

import csv

def resumen_ventas(rutas, ventas):

    with open(rutas, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["producto","unidades","precio"])
        writer.writerows(ventas)

    totales = {}

    with open(rutas, newline="", encoding="utf-8") as f:
        lector = csv.DictReader(f)
               
        for fila in lector:

            producto = fila["producto"]
            unidades = int(fila["unidades"])
            precio = float(fila["precio"])
            
            total = unidades * precio

            if producto in totales:
                totales[producto] += total
            else:
                totales[producto] = total

        return {producto: round(total, 2) for producto, total in totales.items()}
