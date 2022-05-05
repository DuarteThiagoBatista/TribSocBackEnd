from fastapi import FastAPI
import requests

app= FastAPI()

@app.get('/converter/{real}')
def main(dolar:float):
    moeda= requests.get("https://economia.awesomeapi.com.br/last/USD-BRL")
    cotacao_dolar=moeda.json()["USDBRL"]["ask"]
    converter=float(cotacao_dolar)*dolar
    return {"Cotação Dólar":cotacao_dolar,"converter":round(converter, 2)}


