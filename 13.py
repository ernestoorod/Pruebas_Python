# Ejercicio 13 — Estadísticas con *args
# Escribe estadisticas(*numeros), que devuelva una tupla (minimo, maximo, media) 
# con la media redondeada a 2 decimales. Si no recibe ningún número, 
# debe lanzar un ValueError.

def estadisticas(*numeros):

    if len(numeros) >= 1: 
        num_min = min(numeros)
        num_max = max(numeros)
        suma_num = sum(numeros)
        len_num = len(numeros)
        media = round(suma_num / len_num, 2)

        return num_min, num_max, media
    else:
        raise ValueError("Hay que pasar al menos un número")


print(estadisticas(1, 2, 2))       # (3, 9, 5.67)
