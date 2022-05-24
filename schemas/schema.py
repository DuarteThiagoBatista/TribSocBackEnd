import email
from pydantic import BaseModel,EmailStr
from typing import Optional

class Empresa(BaseModel):
    id: Optional[int] = None
    nome:str
    localizacao:str
    email:EmailStr
    password:str
    
    class Config:
        orm_mode = True

class EmpresaResponse(BaseModel):
    id: Optional[int] = None
    nome:str
    localizacao:str
    email:EmailStr
    
    class Config:
        orm_mode = True
    
class LoginSucessEmpresa(BaseModel):
    empresa:EmpresaResponse
    acess_token:str

    class Config:
        orm_mode = True

class LoginData(BaseModel):
    email:str
    password:str

    class Config:
        orm_mode = True