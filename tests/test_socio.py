import unittest
import json
from modelos.socio import agregar_socio, editar_socio, eliminar_socio, buscar_socios

class TestSocio(unittest.TestCase):
    def setUp(self):
        # Inicializar socios.json
        with open('datos/socios.json', 'w') as file:
            json.dump([], file)

    def test_agregar_socio(self):
        agregar_socio("Juan", "Perez", "1990-01-15", "Calle 123", "juan@example.com", "123456789")
        socios = buscar_socios("nombre", "Juan")
        self.assertEqual(len(socios), 1)

    def test_editar_socio(self):
        agregar_socio("Juan", "Perez", "1990-01-15", "Calle 123", "juan@example.com", "123456789")
        socios = buscar_socios("nombre", "Juan")
        socio_id = socios[0]["id_socio"]
        editar_socio(socio_id, "Juan", "Gonzalez", "1990-01-15", "Calle 123", "juan@example.com", "987654321")
        socios_editado = buscar_socios("apellido", "Gonzalez")
        self.assertEqual(socios_editado[0]["telefono"], "987654321")

    def test_eliminar_socio(self):
        agregar_socio("Maria", "Lopez", "1985-06-20", "Av. Principal", "maria@example.com", "987654321")
        socios = buscar_socios("nombre", "Maria")
        socio_id = socios[0]["id_socio"]
        eliminar_socio(socio_id)
        socios_despues = buscar_socios("nombre", "Maria")
        self.assertEqual(len(socios_despues), 0)

if __name__ == '__main__':
    unittest.main()

