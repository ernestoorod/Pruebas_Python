# Ejercicio 2 — Año bisiesto
# Escribe es_bisiesto(anio) que devuelva True o False. Un año es bisiesto si:

# es divisible entre 4 y no entre 100, o
# es divisible entre 400.
# Intenta resolverlo en una sola línea con and/or.

def es_bisiesto(anio):
    if anio % 4 == 0 and anio % 100 != 0 or anio % 400 == 0:
        return True
    else:
        return False
