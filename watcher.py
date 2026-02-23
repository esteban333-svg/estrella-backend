import time
import requests

URL = "https://estrella-backend-l4y7.onrender.com/estado"

while True:
    try:
        response = requests.get(URL)
        data = response.json()
        print("DEBUG keys:", data.keys())
        print("DEBUG dorado_data:", data.get("dorado"))
        print("Respuesta API:", data)

        dorado_data = data.get("dorado", {})

        if dorado_data.get("dorado") is True:
            print("🔥 DORADO ACTIVO 🔥")
            print("Score:", dorado_data.get("score"))
            print("Razones:", dorado_data.get("razones"))
        else:
            print("Sin señal Dorado...")

    except Exception as e:
        print("Error real:", e)

    time.sleep(60)
