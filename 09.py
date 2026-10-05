# Escribe comparar_listas(a, b), que devuelva una tupla con tres listas ordenadas y sin duplicados:

# los elementos que están en las dos,
# los que solo están en a,
# los que solo están en b.
# Pista: conjuntos y sorted().


def comparar_listas(a, b):
    conjunto_a = set(a)
    conjunto_b = set(b)

    en_ambas = sorted(conjunto_a.intersection(conjunto_b))
    solo_en_a = sorted(conjunto_a - conjunto_b)
    solo_en_b = sorted(conjunto_b - conjunto_a)

    return (en_ambas, solo_en_a, solo_en_b)