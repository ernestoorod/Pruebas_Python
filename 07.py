# Ejercicio 7 — Palíndromos¶
# Escribe es_palindromo(texto), que devuelva True si el texto se lee igual al derecho y al revés, ignorando espacios y mayúsculas. Usa slicing.

# Ejemplo: "Somos o no somos" → True

def es_palindromo(texto):
    texto = texto.lower().replace("","")
    texto_reves = texto[::-1]
    return texto == texto_reves

