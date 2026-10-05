# Ejercicio 3 — Precio de la entrada de cine
# Escribe precio_entrada(edad, es_estudiante=False) que devuelva el precio según estas reglas, en este orden de prioridad:

# Condición	Precio
# menor de 4 años	0
# menor de 18	5
# 65 o más	4
# estudiante (adulto)	6
# resto	9

def precio_entrada(edad, es_estudiante=False):
    if edad < 5 : 
        precio = 0
    elif edad >= 5 and edad <= 18 :
        precio = 5
    elif edad >= 65 :
        precio = 4
    elif es_estudiante:
        precio = 6
    else:
        precio = 9
    return precio