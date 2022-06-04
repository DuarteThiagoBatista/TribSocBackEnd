from fastapi import FastAPI,Depends,HTTPException,status
from fastapi.middleware.cors import CORSMiddleware
from router.converterDolar import converterDolarToReal
from router.empresaRouter import empresa_router
from router.colaboradorRouter import colaboradorRouter
from schemas.schema import *
from sqlalchemy.orm import Session
from config.database import get_db
from repository.empresaRepository import EmpresaRepository
from repository.colaboradorRepository import  *
from providers.hash_provider import verify_hash
from providers.token_provider import create_access_token
app= FastAPI()
app.include_router(empresa_router,prefix='/empresa')

app.include_router(colaboradorRouter,prefix='/colaborador')

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post('/login/',status_code=status.HTTP_202_ACCEPTED)
def login(login_data:LoginData,database:Session=Depends(get_db)):
    empresa=EmpresaRepository(database).get_by_email(login_data.email) 
    if empresa:
        password_checked=verify_hash(login_data.password,empresa.password)
        if not password_checked:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Credentials are incorrect")
        token=create_access_token({'id':str(empresa.id),'nome':empresa.nome,'localizacao':empresa.localizacao,'email':empresa.email})
        return LoginSucessEmpresa(empresa=empresa,acess_token=token)

    colaborado=ColaboradorRepositpory(database).get_by_email(login_data.email)
    if colaborado:
        password_checked=verify_hash(login_data.password,colaborado.password)
        if not password_checked:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Credentials are incorrect")
        token=create_access_token({'id':str(colaborado.id)})
        return LoginSucessColaborador(colaborador=colaborado,acess_token=token)
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    
@app.get('/converter/{dolar}')
def main(dolar:float):
    return converterDolarToReal(dolar)
    '''moeda= requests.get("https://economia.awesomeapi.com.br/last/USD-BRL")
    cotacao_dolar=round(float(moeda.json()["USDBRL"]["ask"]),2)
    converter=cotacao_dolar*dolar
    valor_IRRF=round(calculo_irrf(converter),2)
    return {'valor_inserido':dolar,"dolar":cotacao_dolar,"convertido":"%.2f" % converter,"IRRF":valor_IRRF,"salario_liquido":"%.2f" %(converter-valor_IRRF)}
'''
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