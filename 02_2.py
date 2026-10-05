# Escribe es_bisiesto(anio) que devuelva True o False. Un año es bisiesto si:

# es divisible entre 4 y no entre 100, o
# es divisible entre 400.
# Intenta resolverlo en una sola línea con and/or.

def es_bisiesto(anio):

    if anio % 4 == 0 and anio % 100 != 0 or anio % 400 == 0:
        return True
    else:
        return False





print(es_bisiesto(2024))   # True   → divisible entre 4, no entre 100
print(es_bisiesto(2023))   # False  → no divisible entre 4
print(es_bisiesto(1900))   # False  → divisible entre 100, pero no entre 400
print(es_bisiesto(2000))   # True   → divisible entre 400
print(es_bisiesto(2100))   # False
print(es_bisiesto(1600))   # True