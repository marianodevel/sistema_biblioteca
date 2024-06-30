def validar_entero(valor):
    try:
        return int(valor)
    except ValueError:
        raise ValueError(f"El valor '{valor}' no es un entero válido.")

def validar_cadena(valor):
    if not isinstance(valor, str):
        raise ValueError(f"El valor '{valor}' no es una cadena válida.")
    return valor

def validar_fecha(valor):
    from datetime import datetime
    try:
        datetime.strptime(valor, '%Y-%m-%d')
        return valor
    except ValueError:
        raise ValueError(f"El valor '{valor}' no es una fecha válida. Use el formato 'AAAA-MM-DD'.")

def validar_estado_prestamo(valor):
    estados_validos = ["En Curso", "Devuelto"]
    if valor not in estados_validos:
        raise ValueError(f"El estado '{valor}' no es válido. Los estados válidos son: {estados_validos}.")
    return valor

def validar_flotante(valor):
    try:
        return float(valor)
    except ValueError:
        raise ValueError(f"El valor '{valor}' no es un número flotante válido.")

