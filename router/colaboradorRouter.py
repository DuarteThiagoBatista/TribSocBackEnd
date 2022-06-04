

from repository.empresaRepository import EmpresaRepository
from fastapi import APIRouter,Depends,status,HTTPException
from sqlalchemy.orm import Session
from providers.hash_provider import generate_hash,verify_hash
from schemas.schema import *
from config.database import get_db
from repository.colaboradorRepository import ColaboradorRepositpory
from providers.token_provider import create_access_token, verify_access_token


colaboradorRouter=APIRouter()

@colaboradorRouter.post('/signup',status_code=status.HTTP_201_CREATED,response_model=ColaboradorResponse)
def signup(colaborador:Colaborador,database:Session=Depends(get_db)):
    try:
        empresa=EmpresaRepository(database).get_by_email(colaborador.email)
        
        if not empresa:
            colaborador.password=generate_hash(colaborador.password)
            create_colaborador=ColaboradorRepositpory(database).create(colaborador)
            return create_colaborador
        raise HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE)
    except:
        raise HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE,detail="Erro")
       

@colaboradorRouter.get('/token/')
def token(token:str):
    data_id=verify_access_token(token)
    if not data_id:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    return data_id

@colaboradorRouter.post('/createDadosConversao',response_model=DadosConversaoResponse)
def createDadosConversao(dados:DadosConversao,database:Session=Depends(get_db)):
    
    dadosConversao=ColaboradorRepositpory(database).createDadosCoversao(dados)
    return dadosConversao

@colaboradorRouter.delete('/delete/')
def deleteTudoDados(id:int,database:Session=Depends(get_db)):
    ColaboradorRepositpory(database).delete_by_id(id)
