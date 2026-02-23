def calcular_dorado(azul, rojo):

    score = 0.0
    razones = []

    # Ejemplo base de conexión
    if rojo["riesgo"] < 0.5:
        score += 0.3
        razones.append("Riesgo controlado")

    estado = {
     #   "dorado": score > 0.5,
        "dorado": True,
        "score": score,
        "mensaje": "Evaluación completada",
        "razones": razones
    }

    return estado