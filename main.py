import os
from logic.data import velas_binance
from logic.data import obtener_precio
import uvicorn
from dotenv import load_dotenv


def ejecutar():
    load_dotenv()

    host = os.getenv("API_HOST", "127.0.0.1")
    port = int(os.getenv("API_PORT", "8000"))
    reload = os.getenv("API_RELOAD", "true").strip().lower() == "true"
    precio = obtener_precio()
    print("Precio actual:", precio)
    uvicorn.run("api:app", host=host, port=port, reload=reload)

if __name__ == "__main__":
    ejecutar()
