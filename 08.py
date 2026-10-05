# Ejercicio 8 — Agrupar por inicial¶
# Escribe agrupar_por_inicial(palabras), que reciba una lista de palabras y devuelva un diccionario en el que:

# la clave es la inicial en minúscula,
# el valor es la lista de palabras que empiezan por esa letra, en el orden en que aparecen.
# Ejemplo: ["pera", "Plátano", "kiwi"] → {"p": ["pera", "Plátano"], "k": ["kiwi"]}

def agrupar_por_inicial(palabras):
    diccionario = {}

    for palabra in palabras:

        inicial = palabra[0].lower() 

        if inicial not in diccionario:
            diccionario[inicial] = []
        diccionario[inicial].append(palabra)

    return diccionario