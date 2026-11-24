def evaluar_adopcion(edad, especie, disponible, autorizacion, evaluacion):
    if type(edad) is not int:
        raise TypeError('La edad debe ser un entero')
    if not 0 <= edad <= 120:
        raise ValueError('Edad fuera del rango permitido')
    if not isinstance(especie, str):
        raise TypeError('La especie debe ser texto')
    if especie.strip().lower() not in ('perro', 'gato'):
        raise ValueError('Especie no admitida')
    if any(type(v) is not bool for v in (disponible, autorizacion, evaluacion)):
        raise TypeError('Los estados deben ser booleanos')
    if edad < 18:
        return 'Rechazada: edad insuficiente'
    if not disponible:
        return 'Rechazada: animal no disponible'
    if not autorizacion:
        return 'Rechazada: falta autorizacion veterinaria'
    if not evaluacion:
        return 'Rechazada: evaluacion no aprobada'
    return 'Adopcion aprobada'
