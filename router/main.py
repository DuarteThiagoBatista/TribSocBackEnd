from fastapi import FastAPI
import requests
from fastapi.middleware.cors import CORSMiddleware
from router.empresaRouter import empresa_router


app= FastAPI()
app.include_router(empresa_router,prefix='/empresa')

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get('/converter/{dolar}')
def main(dolar:float):
    moeda= requests.get("https://economia.awesomeapi.com.br/last/USD-BRL")
    cotacao_dolar=round(float(moeda.json()["USDBRL"]["ask"]),2)
    converter=cotacao_dolar*dolar
    valor_IRRF=round(calculo_irrf(converter),2)
    return {'valor_inserido':dolar,"dolar":cotacao_dolar,"convertido":"%.2f" % converter,"IRRF":valor_IRRF,"salario_liquido":"%.2f" %(converter-valor_IRRF)}

def calculo_irrf(real):
    if real<= 1903.98:
        return 0
    elif real<=2826.65:
        return (real*7.5)/100
    elif real<=3751.05:
        return (real*15)/100
    elif real<=4664.68:
        return (real*22.5)/100
    else:
        return(real*27.5)/100