
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
    #id: Optional[int] = None
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

class Vaga(BaseModel):
    id:Optional[int] = None
    tipo:str
    modelo:str
    descricao:str
    periodo:str
    requisito:str
    tipo_contratacao:str
    beneficios:str
    id_empresa_token:str
    class Config:
        orm_mode = True

class VagaResponse(BaseModel):
    id:Optional[int] = None
    tipo:str
    modelo:str
    descricao:str
    periodo:str
    requisito:str
    tipo_contratacao:str
    beneficios:str

    class Config:
        orm_mode = True
        
class Colaborador(BaseModel):
    id:Optional[int] = None
    nome:str
    email:EmailStr
    password:str

    class Config:
        orm_mode = True

class ColaboradorResponse(BaseModel):
    nome:str
    email:EmailStr

    class Config:
        orm_mode = True

class LoginSucessColaborador(BaseModel):
    colaborador:ColaboradorResponse
    acess_token:str
    class Config:
        orm_mode = True

class DadosConversao(BaseModel):
    id:Optional[int] = None
    salarioInserido:float
    salarioConvertido:float
    salarioDescontado:float
    salarioRetornado:float
    imposto:float
    moeda:float
    idColaborador:int

    class Config:
        orm_mode = True

class DadosConversaoResponse(BaseModel):
    id:Optional[int] = None
    salarioInserido:float
    salarioConvertido:float
    salarioDescontado:float
    salarioRetornado:float
    imposto:float
    moeda:float

    class Config:
        orm_mode = True


