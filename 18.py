import csv

# ── 1. Tu función ──
def medias_alumnos(ruta, notas):
    
    # PASO 1: escribir el CSV
    # - abrir el archivo para escribir (newline y encoding)
    # - escribir la cabecera
    # - escribir todas las filas

    with open(ruta, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["alumno","asignatura","nota"])
            writer.writerows(notas)

    # PASO 2: leer y acumular
    # - preparar lo que vas a rellenar (¿qué necesitas para una media?)
    # - abrir el archivo para leer (newline y encoding) 
    # - recorrer cada fila con DictReader
    #     - sacar el alumno y la nota (¡convertida!)
    #     - acumular lo necesario para ese alumno

    sumas = {}
    cantidades = {}

    with open(ruta, newline="", encoding="utf-8") as f:
        lector = csv.DictReader(f)
        
        for fila in lector:  
            alumno = fila["alumno"]
            nota = float(fila["nota"])

            if alumno in sumas:
                sumas[alumno] += nota
                cantidades[alumno] += 1
            else:
                sumas[alumno] = nota
                cantidades[alumno] = 1

    # PASO 3: calcular las medias y devolver
    # - por cada alumno: media redondeada a 2 decimales
    # - devolver el diccionario

    return {alumno: round(sumas[alumno] / cantidades[alumno] , 2) for alumno in sumas}


# ── 2. Datos y prueba ──
notas = [
    ("Ana", "mates", 7),
    ("Luis", "mates", 4),
    ("Ana", "lengua", 9),
    ("Luis", "lengua", 6.5),
    ("Marta", "mates", 10),
]

print(medias_alumnos("notas.csv", notas)) # {'Ana': 8.0, 'Luis': 5.25, 'Marta': 10.0}
