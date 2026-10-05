# Ejercicio 15 — Tubería de funciones
# Escribe aplicar_en_cadena(valor, *funciones), que aplique las funciones una 
# detrás de otra al valor y devuelva el resultado final. Si no recibe funciones, 
# devuelve el valor tal cual.

def aplicar_en_cadena(valor, *funciones):
    
    for f in funciones:
        valor = f(valor)
    return valor

print(aplicar_en_cadena(3, lambda x: x + 1, lambda x: x * 2))   # 8
print(aplicar_en_cadena(3, lambda x: x * 2, lambda x: x + 1))   # 7  → el orden importa
print(aplicar_en_cadena(5))                                      # 5  → sin funciones
print(aplicar_en_cadena(-4, abs))                                # 4
print(aplicar_en_cadena("hola", str.upper))                      # HOLA