import unittest
import json
from modelos.libro import agregar_libro, editar_libro, eliminar_libro, buscar_libros

class TestLibro(unittest.TestCase):
    def setUp(self):
        # Inicializar libros.json
        with open('datos/libros.json', 'w') as file:
            json.dump([], file)

    def test_agregar_libro(self):
        agregar_libro("El Quijote", "Miguel de Cervantes", "Editorial A", 1605, "Novela", 5)
        libros = buscar_libros("titulo", "El Quijote")
        self.assertEqual(len(libros), 1)

    def test_editar_libro(self):
        agregar_libro("El Quijote", "Miguel de Cervantes", "Editorial A", 1605, "Novela", 5)
        libros = buscar_libros("titulo", "El Quijote")
        libro_id = libros[0]["id_libro"]
        editar_libro(libro_id, "Don Quijote", "Miguel de Cervantes", "Editorial B", 1605, "Novela", 10)
        libros_editado = buscar_libros("titulo", "Don Quijote")
        self.assertEqual(libros_editado[0]["editorial"], "Editorial B")
        self.assertEqual(libros_editado[0]["cantidad_disponible"], 10)

    def test_eliminar_libro(self):
        agregar_libro("Libro a Eliminar", "Autor X", "Editorial C", 2023, "Ciencia Ficción", 3)
        libros = buscar_libros("titulo", "Libro a Eliminar")
        libro_id = libros[0]["id_libro"]
        eliminar_libro(libro_id)
        libros_despues = buscar_libros("titulo", "Libro a Eliminar")
        self.assertEqual(len(libros_despues), 0)

if __name__ == '__main__':
    unittest.main()

