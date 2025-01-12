# Título y subtítulo
print("╔══════════════════════════════════╗")
print("║ UNIVERSIDAD ESTATAL AMAZÓNICA ║")
print("╚══════════════════════════════════╝")
print("Fernando Corrales\n")

# 1. Crear una lista para almacenar las asignaturas
asignaturas = []

# 2. Agregar asignaturas a la lista
asignaturas.append("Matemáticas")
asignaturas.append("Física")
asignaturas.append("Química")
asignaturas.append("Historia")
asignaturas.append("Lengua")
asignaturas.append("Programación")
asignaturas.append("Base de Datos")

# Otras formas de agregar elementos (menos comunes en este caso):
# asignaturas.extend(["Biología", "Geografía"])  # Agregar otra lista
# asignaturas.insert(2, "Informática")  # Insertar en un índice específico

# 3. Mostrar las asignaturas por pantalla (diferentes métodos)

# a) Usando un bucle for tradicional (con índice):
print("Asignaturas del curso (con bucle for):")
for i in range(len(asignaturas)):
    print(f"- {asignaturas[i]}")

print()

# b) Usando un bucle for (más conciso y recomendado):
print("Asignaturas del curso (con bucle for):")
for asignatura in asignaturas:
    print(f"- {asignatura}")

print()

# c) Usando join (para mostrar todas las asignaturas en una sola línea):
asignaturas_string = ", ".join(asignaturas)
print(f"Asignaturas del curso (en una sola línea): {asignaturas_string}")

print()

# d) Usando sorted() para ordenarlas alfabéticamente antes de mostrarlas:
print("Asignaturas del curso (ordenadas alfabéticamente):")
for asignatura in sorted(asignaturas):
    print(f"- {asignatura}")

print()

# e) Mostrar las asignaturas con un formato de tabla básico:
print("Asignaturas del curso (formato de tabla básico):")
print("╔════════════════════╗")
print("║ Asignatura       ║")
print("╠════════════════════╣")
for asignatura in asignaturas:
    print(f"║ {asignatura:<16} ║") # Alineación a la izquierda con 16 espacios
print("╚════════════════════╝")