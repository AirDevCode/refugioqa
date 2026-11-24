import pytest
from refugio import evaluar_adopcion

@pytest.mark.parametrize('datos, esperado', [
    ((25, 'perro', True, True, True), 'Adopcion aprobada'),
    ((30, 'gato', True, True, True), 'Adopcion aprobada'),
    ((18, 'gato', True, True, True), 'Adopcion aprobada'),
    ((120, 'perro', True, True, True), 'Adopcion aprobada'),
    ((17, 'perro', True, True, True), 'Rechazada: edad insuficiente'),
    ((0, 'gato', True, True, True), 'Rechazada: edad insuficiente'),
    ((25, 'perro', False, True, True), 'Rechazada: animal no disponible'),
    ((25, 'perro', True, False, True), 'Rechazada: falta autorizacion veterinaria'),
    ((25, 'gato', True, True, False), 'Rechazada: evaluacion no aprobada'),
    ((25, ' GATO ', True, True, True), 'Adopcion aprobada'),
])
def test_resultados(datos, esperado):
    assert evaluar_adopcion(*datos) == esperado

@pytest.mark.parametrize('datos, error, mensaje', [
    ((-1, 'perro', True, True, True), ValueError, 'Edad fuera'),
    ((121, 'perro', True, True, True), ValueError, 'Edad fuera'),
    (('25', 'perro', True, True, True), TypeError, 'edad debe'),
    ((None, 'perro', True, True, True), TypeError, 'edad debe'),
    ((True, 'perro', True, True, True), TypeError, 'edad debe'),
    ((18.5, 'perro', True, True, True), TypeError, 'edad debe'),
    ((25, 'conejo', True, True, True), ValueError, 'Especie no admitida'),
    ((25, '', True, True, True), ValueError, 'Especie no admitida'),
    ((25, None, True, True, True), TypeError, 'especie debe'),
    ((25, 'gato', 1, True, True), TypeError, 'estados deben'),
    ((25, 'gato', True, None, True), TypeError, 'estados deben'),
    ((25, 'gato', True, True, 'si'), TypeError, 'estados deben'),
])
def test_excepciones(datos, error, mensaje):
    with pytest.raises(error, match=mensaje):
        evaluar_adopcion(*datos)
