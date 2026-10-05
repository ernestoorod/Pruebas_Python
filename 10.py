# Escribe aprobados(nombres, notas, minimo=5), que devuelva un 
# diccionario {nombre: nota} solo con los que tienen una nota ≥ minimo. 
# Hazlo con zip y una comprensión de diccionario (una línea).

def aprobados(nombres,notas,minimo=5):

    diccionario = {}

    for nombre, nota in zip(nombres, notas):
        if nota >= minimo:
            diccionario[nombre] = nota

    return diccionario