# Escribe anadir_ordenado(lista, elemento), que devuelva una lista nueva con el 
# elemento añadido y todo ordenado de menor a mayor, sin modificar la lista que 
# recibe.

# Esto comprueba si has entendido lo de mutable/inmutable. 
# La prueba mira que la original siga igual.

def anadir_ordenado(lista,elemento):

    nueva = lista.copy()
    nueva.append(elemento)
    nueva.sort()

    return nueva
