import csv

# ── 1. Crear el CSV de prueba (esto no lo toques) ──
with open("gastos.csv", "w", encoding="utf-8") as f:
    f.write("fecha,categoria,importe\n")
    f.write("2026-10-01,comida,12.50\n")
    f.write("2026-10-01,ocio,20\n")
    f.write("2026-10-02,comida,8.25\n")
    f.write("2026-10-03,transporte,abc\n")
    f.write("2026-10-03,ocio,\n")
    f.write("2026-10-04,transporte,3.40\n")


# ── 2. Tu función ──
def gastos_por_categoria(ruta):
    # - preparar lo que vas a ir rellenando (¿qué necesitas antes del bucle?)
    # - abrir el archivo para leer (acuérdate del encoding)
    # - recorrer cada fila con DictReader
    #     - intentar convertir el importe
    #     - si va bien: acumular en su categoría
    #     - si falla: contar un error
    # - devolver la tupla con los totales redondeados y los errores
    pass


# ── 3. Prueba ──
print(gastos_por_categoria("gastos.csv"))
# ({'comida': 20.75, 'ocio': 20.0, 'transporte': 3.4}, 2)
