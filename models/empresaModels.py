from sqlalchemy import Column, Integer,String,Float
from database import Base

class EmpresaModels(Base):
    __tablename__='Empresas'
    id=Column(Integer,primary_key=True,index=True)
    nome=Column(String)
    localizacao=Column(String)
    modelo=Column(String)
    vagaTipo=Column(String)
    salario=Column(Float)
    detalhamento_vaga=Column(String)
    vagas_restante=Column(Integer)
    email=Column(String)
    password=Column(String)