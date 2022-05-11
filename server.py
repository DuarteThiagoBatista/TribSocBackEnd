from fastapi import FastAPI,Depends
from sqlalchemy.orm import Session
from database import criar_db,get_db
from entity.empresaEntity import EmpresaEntity
from repository.empresaRepository import RepositorioEmpresa
import requests

criar_db()
app=FastAPI()


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

@app.get('/converter/{dolar}')
def main(dolar:float):
    moeda= requests.get("https://economia.awesomeapi.com.br/last/USD-BRL")
    cotacao_dolar=round(float(moeda.json()["USDBRL"]["ask"]),2)
    converter=cotacao_dolar*dolar
    valor_IRRF=round(calculo_irrf(converter),2)
    return {'valor_inserido':dolar,"dolar":cotacao_dolar,"convertido":"%.2f" % converter,"IRRF":valor_IRRF,"salario_liquido":"%.2f" %(converter-valor_IRRF)}


@app.post('/empresas')
def criar_empresas(empresa:EmpresaEntity,db:Session=Depends(get_db)):
    produto_criado=RepositorioEmpresa(db).criar(empresa)
    return produto_criado

@app.get('/empresas')
def listar_produtos(db:Session=Depends(get_db)):
    return RepositorioEmpresa(db).listar()