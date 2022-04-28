from fastapi import FastAPI
import requests

app= FastAPI()

@app.get('/converter/{real}')
def main(real:float):
    moeda= requests.get("https://economia.awesomeapi.com.br/last/USD-BRL")
    dolar=moeda.json()["USDBRL"]["ask"]
    converter=float(dolar)*real
    return {"real":real,"dolar":dolar,"converter":round(converter, 2)}


