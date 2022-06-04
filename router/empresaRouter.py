from repository.vagaRepository import VagaRepository

from fastapi import APIRouter, Depends,status,HTTPException
from config.database import get_db
from schemas.schema import *
from sqlalchemy.orm import Session
from providers.hash_provider import generate_hash,verify_hash
from providers.token_provider import create_access_token,verify_access_token
from repository.empresaRepository import EmpresaRepository
from repository.colaboradorRepository import ColaboradorRepositpory

empresa_router=APIRouter()

@empresa_router.post('/signup',status_code=status.HTTP_201_CREATED, response_model=EmpresaResponse)
def signup(empresa:Empresa,database:Session=Depends(get_db)):

    empresa.password=generate_hash(empresa.password)
    try:
        colaboradoEmail=ColaboradorRepositpory(database).get_by_email(empresa.email)
        if not colaboradoEmail:
            create_empresa=EmpresaRepository(database).create(empresa)
            return create_empresa
        raise HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE)
    except:
        raise HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE,detail="Erro")



@empresa_router.delete('/id/{id}',status_code=status.HTTP_200_OK)
def delete_By_id(id:int,database:Session=Depends(get_db)):
    EmpresaRepository(database).get_by_id_delete(id)

@empresa_router.get('/token/{token}',response_model= EmpresaResponse)
def token(token:str,database:Session=Depends(get_db)):
    data_id=verify_access_token(token)
    
    if not data_id:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    return EmpresaRepository(database).get_by_id(int(data_id))

#VAGAS
@empresa_router.post('/createVaga',status_code=status.HTTP_201_CREATED,response_model=VagaResponse)
def createVaga(vaga:Vaga,database:Session=Depends(get_db)):
    try:
        vaga.id_empresa_token=int(verify_access_token(vaga.id_empresa_token))
        create_vaga=VagaRepository(database).create(vaga)
        return create_vaga
    except:
        raise HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE,detail="Erro")
    
@empresa_router.delete('/idVaga/{id}')
def delete_by_id(id:int,database:Session=Depends(get_db)):
    VagaRepository(database).delete_by_id(id)

@empresa_router.get('/Vaga/{token}',status_code=status.HTTP_200_OK)
def get_by_token(token:str,database:Session=Depends(get_db)):
    
    id_empresa=int(verify_access_token(token))
    vaga=VagaRepository(database).get_by_id(id_empresa)
    return vaga

@empresa_router.get('/listaVagas')
def get_vagas(database:Session=Depends(get_db)):
    vagas=VagaRepository(database).getVagas()
    return vagas