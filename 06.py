# Partiendo de un número n > 0, repite hasta llegar a 1:

# si n es par → n = n // 2
# si es impar → n = 3 * n + 1
# Escribe pasos_collatz(n) que devuelva cuántos pasos hacen falta para llegar a 1. Usa while y el operador ternario.

# Ejemplo: 6 → 3 → 10 → 5 → 16 → 8 → 4 → 2 → 1 son 8 pasos.

def pasos_collatz(n):
    pasos = 0
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        pasos += 1
    return pasos
