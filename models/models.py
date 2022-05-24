from enum import unique
from operator import ipow
from sqlalchemy import Column,Integer,Float,String,ForeignKey
from sqlalchemy.orm import relationship
from config.database import Base

class EmpresasModels(Base):
    __tablename__ = 'empresas'
    
    id=Column(Integer,primary_key=True, index=True)
    nome=Column(String)
    localizacao=Column(String)
    email=Column(String,unique=True,index=True)
    password = Column(String)
