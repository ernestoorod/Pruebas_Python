# Ejercicio 1 — Descomponer segundos
# Escribe segundos_a_hms(segundos) que reciba un número entero de segundos y devuelva una tupla (horas, minutos, segundos).

# Ejemplo: segundos_a_hms(3661) → (1, 1, 1)

# Pista: // y %.



def segundos_a_hms(segundos): 
    horas = segundos// 3600 
    minutos = (segundos % 3600) // 60
    segundos = segundos % 60

    return (horas, minutos, segundos)