import json

def crear_socio(nombre, apellido, fecha_nacimiento, direccion, correo_electronico, telefono, contador_id_socio):
    socio = {
        "id_socio": contador_id_socio,
        "nombre": nombre,
        "apellido": apellido,
        "fecha_nacimiento": fecha_nacimiento,
        "direccion": direccion,
        "correo_electronico": correo_electronico,
        "telefono": telefono
    }
    return socio

# Función para cargar datos de socios desde un archivo JSON
def cargar_socios():
    try:
        with open('datos/socios.json', 'r', encoding='utf-8') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

# Función para guardar datos de socios en un archivo JSON
def guardar_socios(socios):
    with open('datos/socios.json', 'w', encoding='utf-8') as file:
        json.dump(socios, file, indent=4, ensure_ascii=False)

# Función para agregar un nuevo socio
def agregar_socio(nombre, apellido, fecha_nacimiento, direccion, correo_electronico, telefono):
    socios = cargar_socios()
    contador_id_socio = max([socio.get('id_socio', 0) for socio in socios], default=0) + 1
    nuevo_socio = crear_socio(nombre, apellido, fecha_nacimiento, direccion, correo_electronico, telefono, contador_id_socio)
    socios.append(nuevo_socio)
    guardar_socios(socios)

# Función para editar un socio existente por su ID
def editar_socio(id_socio, nombre, apellido, fecha_nacimiento, direccion, correo_electronico, telefono):
    socios = cargar_socios()
    for socio in socios:
        if socio['id_socio'] == id_socio:
            socio['nombre'] = nombre
            socio['apellido'] = apellido
            socio['fecha_nacimiento'] = fecha_nacimiento
            socio['direccion'] = direccion
            socio['correo_electronico'] = correo_electronico
            socio['telefono'] = telefono
            break
    guardar_socios(socios)

# Función para eliminar un socio por su ID
def eliminar_socio(id_socio):
    socios = cargar_socios()
    socios = [socio for socio in socios if socio['id_socio'] != id_socio]
    guardar_socios(socios)

# Función para buscar socios por nombre, apellido, dirección o correo electrónico
def buscar_socios(criterio, valor):
    socios = cargar_socios()
    resultados = []
    for socio in socios:
        if valor.lower() in str(socio.get(criterio, '')).lower():
            resultados.append(socio)
    return resultados
