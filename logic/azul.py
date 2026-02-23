from logic.data import obtener_precio


def calcular_azul():
    precio = obtener_precio("BTC/USDT")

    estado = {
        "fuerza_tecnica": 0.1,   # placeholder por ahora
        "precio": precio,
        "rsi": None,
        "emas": None,
        "bollinger": None
    }

    return estado