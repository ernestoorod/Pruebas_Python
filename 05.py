# Ejercicio 5 — Números primos
# Escribe es_primo(n), que devuelva True si n es primo. Recuerda que 0 y 1 no son primos. Usa un for y sal en cuanto encuentres un divisor.
# Escribe primos_hasta(n), que devuelva la lista de primos entre 2 y n (ambos incluidos) usando una comprensión de listas que llame a es_primo.

def es_primo(n):
    if n < 2:
        return False
    for i in range(2, n):      
        if n % i == 0:
            return False
    return True

def primos_hasta(n):  
    return [i for i in range(2, n + 1) if es_primo(i)]
