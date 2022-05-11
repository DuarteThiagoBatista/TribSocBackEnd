from pydantic import BaseModel
from typing import Optional

class EmpresaEntity(BaseModel):
    id:Optional[int]=None
    nome:str
    localizacao:str
    modelo:str
    vagaTipo:str
    salario:float
    detalhamento_vaga:str
    vagas_restante:int
    email:str
    password:str

    class Config:
        orm_mode=True

