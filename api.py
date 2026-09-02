import requests

def obtener_tasa_cambio(moneda_destino="USD"):
    url = f"https://open.er-api.com/v6/latest/DOP"
    respuesta = requests.get(url)
    datos = respuesta.json()

    tasa = datos["rates"][moneda_destino]
    return tasa

if __name__ == "__main__":
    tasa = obtener_tasa_cambio("USD")
    print(f"1 DOP = {tasa} USD")