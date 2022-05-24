

from fastapi import APIRouter, Depends,status,HTTPException
from config.database import get_db
from schemas.schema import Empresa,EmpresaResponse, LoginData,LoginSucessEmpresa
from sqlalchemy.orm import Session
from providers.hash_provider import generate_hash,verify_hash
from providers.token_provider import create_access_token,verify_access_token
from repository.empresaRepository import EmpresaRepository

empresa_router=APIRouter()

@empresa_router.post('/signup',status_code=status.HTTP_201_CREATED, response_model=EmpresaResponse)
def signup(empresa:Empresa,database:Session=Depends(get_db)):
    empresa.password=generate_hash(empresa.password)
    create_empresa=EmpresaRepository(database).create(empresa)
    return create_empresa

@empresa_router.post('/login',response_model=LoginSucessEmpresa,status_code=status.HTTP_200_OK)
def login(login_data:LoginData,database:Session=Depends(get_db)):
    password=login_data.password
    email=login_data.email

    empresa=EmpresaRepository(database).get_by_email(email) 

    if not empresa:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    
    password_checked=verify_hash(password,empresa.password)
    if not password_checked:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Credentials are incorrect")
    token=create_access_token({'id':str(empresa.id),'nome':empresa.nome,'localizacao':empresa.localizacao,'email':empresa.email})
    return LoginSucessEmpresa(empresa=empresa,acess_token=token)

@empresa_router.delete('/id/{id}',status_code=status.HTTP_200_OK)
def delete_By_id(id:int,database:Session=Depends(get_db)):
    EmpresaRepository(database).get_by_id_delete(id)

@empresa_router.get('/token{token}')
def token(token:str):
    data_id=verify_access_token(token)
    if not data_id:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    return data_id