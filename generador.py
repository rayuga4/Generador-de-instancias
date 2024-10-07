import random

nombre_archivo = "instancia2"
num_asignaturas = 40
num_salas = 3

num_bloque_1 = int(num_asignaturas * 0.65)
num_bloque_2 = num_asignaturas - num_bloque_1

bloques = [1] * num_bloque_1 + [2] * num_bloque_2
random.shuffle(bloques)

capacidad = []
prioridad = []
disponibilidad = []
interes = []

for x in range(num_salas):
    capacidad.append(random.randint(45,80))

for x in range(num_asignaturas):    
    if x%5==0:
        prioridad.append(random.randint(6,10))
    else:
        prioridad.append(random.randint(1,5))
    num_disponibles = random.randint(14, 28)
    disponibilidad_bloques = [1] * num_disponibles + [0] * (35 - num_disponibles)
    random.shuffle(disponibilidad_bloques)
    disponibilidad.append(disponibilidad_bloques)
    interes.append(random.randint(40,80))

with open(f"{nombre_archivo}.dzn", "w") as f:
    f.write(f"Cantidad_de_salas = {num_salas};\n")
    f.write(f"Cantidad_de_ramos = {num_asignaturas};\n")
    f.write(f"Bloques = {bloques};\n")
    f.write(f"Capacidad = {capacidad};\n")
    f.write(f"Prioridad = {prioridad};\n")
    f.write(f"Interes = {interes};\n")
    f.write("Disponibilidad = array2d(1..Cantidad_de_ramos, 1..35, [\n")
    for dispo in disponibilidad:
        f.write(f"  {', '.join(map(str, dispo))},\n")
    f.write("]);\n")