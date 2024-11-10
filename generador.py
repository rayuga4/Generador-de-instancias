import random

nombre_archivo = "instanciaPequeña6"
# Se especifica la cantidad de salas y asignaturas para la instancia deseada
num_asignaturas = 30
num_salas = 1

#se obtiene la cantidad de asignaturas con 1 bloque y la cantidad con 2 bloques
num_bloque_1 = int(num_asignaturas * 0.65)
num_bloque_2 = num_asignaturas - num_bloque_1

#se realiza shuffle de manera que sea aleatoria la cantidad de bloques de cada sala y no sea "secuencial"
bloques = [1] * num_bloque_1 + [2] * num_bloque_2
random.shuffle(bloques)

capacidad = []
prioridad = []
disponibilidad = []
interes = []

#se asigna una cantidad aleatoria de capacidad de sala a cada sala segun los rangos dados por enunciado
for x in range(num_salas):
    capacidad.append(random.randint(45,80))
#    capacidad.append(80)

for x in range(num_asignaturas):    
    # cada 5 asignaturas se asigna uno indispensable con prioridad mayor o igual a 6
    if x%5==0:
        prioridad.append(random.randint(6,10))
    else:
        prioridad.append(random.randint(1,5))
    # se genera una cantidad aleatoria de bloques disponibles segun el rango del enunciado y se realiza shuffle similar a los bloques de cada ramo
    num_disponibles = random.randint(14, 28)
    disponibilidad_bloques = ["true"] * num_disponibles + ["false"] * (35 - num_disponibles)
    random.shuffle(disponibilidad_bloques)
    disponibilidad.append(disponibilidad_bloques)
    # se genera un interes aleatorio a cada asignatura segun los rangos dados por enunciado
    interes.append(random.randint(40,80))

# se escribe todos los datos generados en el formato necesario para que sea utilizado con el modelo planteado
with open(f"{nombre_archivo}.dzn", "w") as f:
    f.write(f"cantSalas = {num_salas};\n")
    f.write(f"cantRamos = {num_asignaturas};\n")
    f.write(f"bloques = {bloques};\n")
    f.write(f"capacidad = {capacidad};\n")
    f.write(f"prioridad = {prioridad};\n")
    f.write(f"interes = {interes};\n")
    f.write("disponibilidad = array2d(1..cantRamos, 1..35, [\n")
    for dispo in disponibilidad:
        f.write(f"  {', '.join(map(str, dispo))},\n")
    f.write("]);\n")
