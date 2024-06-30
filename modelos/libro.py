import json

def crear_libro(titulo, autor, editorial, anio_publicacion, genero, cantidad_disponible, contador_id_libro):
    libro = {
        "id_libro": contador_id_libro,
        "titulo": titulo,
        "autor": autor,
        "editorial": editorial,
        "anio_publicacion": anio_publicacion,
        "genero": genero,
        "cantidad_disponible": cantidad_disponible
    }
    return libro

# Función para cargar datos de libros desde un archivo JSON
def cargar_libros():
    try:
        with open('datos/libros.json', 'r', encoding='utf-8') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

# Función para guardar datos de libros en un archivo JSON
def guardar_libros(libros):
    with open('datos/libros.json', 'w', encoding='utf-8') as file:
        json.dump(libros, file, indent=4, ensure_ascii=False)

# Función para agregar un nuevo libro
def agregar_libro(titulo, autor, editorial, anio_publicacion, genero, cantidad_disponible):
    libros = cargar_libros()
    contador_id_libro = max([libro.get('id_libro', 0) for libro in libros], default=0) + 1
    nuevo_libro = crear_libro(titulo, autor, editorial, anio_publicacion, genero, cantidad_disponible, contador_id_libro)
    libros.append(nuevo_libro)
    guardar_libros(libros)

# Función para editar un libro existente por su ID
def editar_libro(id_libro, titulo, autor, editorial, anio_publicacion, genero, cantidad_disponible):
    libros = cargar_libros()
    for libro in libros:
        if libro['id_libro'] == id_libro:
            libro['titulo'] = titulo
            libro['autor'] = autor
            libro['editorial'] = editorial
            libro['anio_publicacion'] = anio_publicacion
            libro['genero'] = genero
            libro['cantidad_disponible'] = cantidad_disponible
            break
    guardar_libros(libros)

# Función para eliminar un libro por su ID
def eliminar_libro(id_libro):
    libros = cargar_libros()
    libros = [libro for libro in libros if libro['id_libro'] != id_libro]
    guardar_libros(libros)

# Función para buscar libros por título, género, autor o editorial
def buscar_libros(criterio, valor):
    libros = cargar_libros()
    resultados = []
    for libro in libros:
        if valor.lower() in str(libro.get(criterio, '')).lower():
            resultados.append(libro)
    return resultados
