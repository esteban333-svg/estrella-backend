from fastapi import FastAPI
from logic.azul import calcular_azul
from logic.rojo import calcular_rojo
from logic.dorado import calcular_dorado

app = FastAPI()


@app.get("/")
def inicio():
    return {
        "ok": True,
        "mensaje": "API activa",
        "endpoints": {
            "estado": "/estado",
            "docs": "/docs"
        }
    }


@app.get("/estado")
def obtener_estado():
    azul = calcular_azul()
    rojo = calcular_rojo()
    dorado = calcular_dorado(azul, rojo)

    return {
        "azul": azul,
        "rojo": rojo,
        "dorado": dorado
    }
