import json

def crear_prestamo(id_socio, id_libro, fecha_prestamo, costo, fecha_devolucion, estado_prestamo, contador_id_prestamo):
    prestamo = {
        "id_prestamo": contador_id_prestamo,
        "id_socio": id_socio,
        "id_libro": id_libro,
        "fecha_prestamo": fecha_prestamo,
        "costo": costo,
        "fecha_devolucion": fecha_devolucion,
        "estado_prestamo": estado_prestamo
    }
    return prestamo

# Función para cargar datos de préstamos desde un archivo JSON
def cargar_prestamos():
    try:
        with open('datos/prestamos.json', 'r', encoding='utf-8') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

# Función para guardar datos de préstamos en un archivo JSON
def guardar_prestamos(prestamos):
    with open('datos/prestamos.json', 'w', encoding='utf-8') as file:
        json.dump(prestamos, file, indent=4, ensure_ascii=False)

# Función para registrar un nuevo préstamo
def registrar_prestamo(id_socio, id_libro, fecha_prestamo, costo, fecha_devolucion, estado_prestamo):
    prestamos = cargar_prestamos()
    contador_id_prestamo = max([prestamo.get('id_prestamo', 0) for prestamo in prestamos], default=0) + 1
    nuevo_prestamo = crear_prestamo(id_socio, id_libro, fecha_prestamo, costo, fecha_devolucion, estado_prestamo, contador_id_prestamo)
    prestamos.append(nuevo_prestamo)
    guardar_prestamos(prestamos)

# Función para actualizar el estado de un préstamo (marcar como devuelto)
def actualizar_estado_prestamo(id_prestamo, estado_prestamo):
    prestamos = cargar_prestamos()
    for prestamo in prestamos:
        if prestamo['id_prestamo'] == id_prestamo:
            prestamo['estado_prestamo'] = estado_prestamo
            break
    guardar_prestamos(prestamos)

# Función para buscar préstamos por socio, libro o rango de fechas
def buscar_prestamos(criterio, valor):
    prestamos = cargar_prestamos()
    resultados = []
    for prestamo in prestamos:
        if isinstance(valor, str) and isinstance(prestamo.get(criterio), str):
            if valor.lower() in prestamo.get(criterio, '').lower():
                resultados.append(prestamo)
        elif prestamo.get(criterio) == valor:
            resultados.append(prestamo)
    return resultados

