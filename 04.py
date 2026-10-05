# Ejercicio 4 — Contar vocales
# Escribe contar_vocales(texto) que devuelva cuántas vocales tiene el texto, sin distinguir mayúsculas y minúsculas y contando las acentuadas (áéíóúü).

def contar_vocales(texto):
    vocales = "aeiouáéíóúü" # todas las opciones
    contador = 0 #contador de vocales en la frase

    for caracteres in texto.lower():
        if caracteres in vocales:
            contador += 1
    return contador