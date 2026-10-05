# Ejercicio 16 — Conversión segura
# Escribe convertir_lista(valores), que intente convertir cada elemento a float 
# y devuelva una tupla (convertidos, errores):

# convertidos: lista de floats que se han podido convertir,
# errores: lista de los valores originales que no se han podido convertir.
# Ojo: float("hola") lanza ValueError, pero float(None) lanza TypeError.

def convertir_lista(valores):

    convertidos = []
    errores = []

    for elemento in valores:

        try:
            conversor = float(elemento)
            convertidos.append(conversor)
        except ValueError:
            errores.append(elemento)
        except TypeError:
            errores.append(elemento)

    return convertidos, errores