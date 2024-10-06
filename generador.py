import random

nombre_archivo = "instancia_grupo11"
num_asignaturas = 50  # Ajusta el número de asignaturas según sea necesario
num_salas = 10  # Ajusta el número de salas disponibles
min_capacidad = 20  # Capacidad mínima de sillas por sala
max_capacidad = 45  # Capacidad máxima de sillas por sala


num_bloque_1 = int(num_asignaturas * 0.65)
num_bloque_2 = num_asignaturas - num_bloque_1
    
bloques = [1] * num_bloque_1 + [2] * num_bloque_2
random.shuffle(bloques)  # Mezclamos para aleatorizar

capacidad = []
prioridad = []
disponibilidad = []
interes = []

for x in range(num_salas):
    capacidad.append(random.randint(min_capacidad,max_capacidad))

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
    f.write(f"Tamanio_salas = [{', '.join(map(str, capacidad))}];\n")
    f.write(f"Prioridad = [{', '.join(map(str, prioridad))}];\n")
    f.write(f"Interes = [{', '.join(map(str, interes))}];\n")
    f.write("Disponibilidad = array2d(1..Cantidad_de_ramos, 1..35, [\n")
    for dispo in disponibilidad:
        f.write(f"  {', '.join(map(str, dispo))},\n")
    f.write("]);\n")

