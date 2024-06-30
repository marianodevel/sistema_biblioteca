import unittest
import json
from modelos.prestamo import registrar_prestamo, actualizar_estado_prestamo, buscar_prestamos

class TestPrestamo(unittest.TestCase):
    def setUp(self):
        # Inicializar prestamos.json
        with open('datos/prestamos.json', 'w') as file:
            json.dump([], file)

    def test_registrar_prestamo(self):
        registrar_prestamo(1, 1, "2024-06-30", 0, "", "En Curso")
        prestamos = buscar_prestamos("id_socio", 1)
        self.assertEqual(len(prestamos), 1)

    def test_actualizar_estado_prestamo(self):
        registrar_prestamo(1, 1, "2024-06-30", 0, "", "En Curso")
        prestamos = buscar_prestamos("id_socio", 1)
        prestamo_id = prestamos[0]["id_prestamo"]
        actualizar_estado_prestamo(prestamo_id, "Devuelto")
        prestamos_actualizado = buscar_prestamos("id_socio", 1)
        self.assertEqual(prestamos_actualizado[0]["estado_prestamo"], "Devuelto")

if __name__ == '__main__':
    unittest.main()

