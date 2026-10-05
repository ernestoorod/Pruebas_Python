# Escribe sumar_matrices(a, b), que sume dos matrices del mismo tamaño (listas de listas) 
# elemento a elemento. Hazlo con una comprensión anidada.

# [[1, 2], [3, 4]] + [[10, 20], [30, 40]] → [[11, 22], [33, 44]]

def sumar_matrices(a,b):

    resultado = []

    for fila_a, fila_b in zip(a, b):
        fila_nueva = []

        for num_a, num_b in zip(fila_a, fila_b):
            fila_nueva.append(num_a + num_b)
        resultado.append(fila_nueva)

    return resultado
