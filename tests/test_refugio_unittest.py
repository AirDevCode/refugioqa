import unittest
from refugio import evaluar_adopcion

class TestRefugio(unittest.TestCase):
    def test_aprobada(self):
        self.assertEqual(evaluar_adopcion(25, 'perro', True, True, True), 'Adopcion aprobada')
    def test_limite_edad(self):
        self.assertEqual(evaluar_adopcion(18, 'gato', True, True, True), 'Adopcion aprobada')
    def test_menor(self):
        self.assertEqual(evaluar_adopcion(17, 'gato', True, True, True), 'Rechazada: edad insuficiente')
    def test_no_disponible(self):
        self.assertEqual(evaluar_adopcion(25, 'gato', False, True, True), 'Rechazada: animal no disponible')
    def test_sin_autorizacion(self):
        self.assertEqual(evaluar_adopcion(25, 'gato', True, False, True), 'Rechazada: falta autorizacion veterinaria')
    def test_evaluacion(self):
        self.assertEqual(evaluar_adopcion(25, 'gato', True, True, False), 'Rechazada: evaluacion no aprobada')
    def test_edad_negativa(self):
        with self.assertRaisesRegex(ValueError, 'Edad fuera'):
            evaluar_adopcion(-1, 'gato', True, True, True)
    def test_especie(self):
        with self.assertRaisesRegex(ValueError, 'Especie no admitida'):
            evaluar_adopcion(25, 'conejo', True, True, True)
    def test_tipo(self):
        with self.assertRaisesRegex(TypeError, 'edad debe'):
            evaluar_adopcion('25', 'gato', True, True, True)

if __name__ == '__main__':
    unittest.main()
