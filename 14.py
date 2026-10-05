# Tienes una lista de diccionarios como esta: 
# {"nombre": "teclado", "precio": 25, "stock": 10}.

# Escribe ordenar_productos(productos, clave="precio", descendente=False), 
# que devuelva la lista de nombres ordenada por la clave indicada. 
# Usa sorted con una lambda.

def ordenar_productos(productos, clave="precio", descendente=False):

    ordenados = sorted(productos, key=lambda a: a[clave], reverse=descendente)

    nombres = []
    for p in ordenados:
        nombres.append(p["nombre"])

    return nombres

productos = [
    {"nombre": "teclado", "precio": 25, "stock": 10},
    {"nombre": "raton", "precio": 15, "stock": 30},
    {"nombre": "monitor", "precio": 180, "stock": 5},
    {"nombre": "alfombrilla", "precio": 8, "stock": 50},
]

print(ordenar_productos(productos))
# ['alfombrilla', 'raton', 'teclado', 'monitor']   → por precio, de menor a mayor

print(ordenar_productos(productos, descendente=True))
# ['monitor', 'teclado', 'raton', 'alfombrilla']   → por precio, de mayor a menor

print(ordenar_productos(productos, clave="stock"))
# ['monitor', 'teclado', 'raton', 'alfombrilla']   → por stock, de menor a mayor

print(ordenar_productos(productos, clave="stock", descendente=True))
# ['alfombrilla', 'raton', 'teclado', 'monitor']

print(ordenar_productos(productos, clave="nombre"))
# ['alfombrilla', 'monitor', 'raton', 'teclado']   → alfabético