
from sqlalchemy.sql import func
from sqlalchemy import Column,Integer,Float,String,ForeignKey,Table,DateTime
from sqlalchemy.orm import relationship
from config.database import Base


class EmpresasModels(Base):
    __tablename__ = 'empresas'
    
    id=Column(Integer,primary_key=True, index=True)
    nome=Column(String)
    localizacao=Column(String)
    email=Column(String,unique=True,index=True)
    password = Column(String)

class VagasModels(Base):
    __tablename__ = "vagas"

    tipo=Column(String)
    modelo=Column(String)
    descricao=Column(String)
    periodo=Column(String)
    requisito=Column(String)
    tipo_contratacao=Column(String)
    beneficios=Column(String)
    id=Column(Integer, primary_key=True,index=True)
    id_empresa=Column(Integer, ForeignKey("empresas.id"))




class ConversoesColaboradores(Base):
    __tablename__ ="ConversoesColaboradores"
    idColaborador=Column(ForeignKey("Colaboradores.id"), primary_key=True)
    idDadosConversao=Column(ForeignKey("DadosConversao.id"), primary_key=True)
    dadosConversao=relationship("DadosConversaoModels", back_populates="colaborador")
    colaborado=relationship("ColaboradoresModels",back_populates="dadosConversao")


class ColaboradoresModels(Base):
    __tablename__ = "Colaboradores"
    
    id=Column(Integer, primary_key=True,index=True)
    nome=Column(String,nullable=False)
    email=Column(String,unique=True,index=True)
    password = Column(String,nullable=False)
    dadosConversao=relationship("ConversoesColaboradores",back_populates="colaborado")

class DadosConversaoModels(Base):
    __tablename__ = "DadosConversao"

    id=Column(Integer, primary_key=True,index=True)
    salarioInserido=Column(Float)
    salarioConvertido=Column(Float)
    salarioDescontado=Column(Float)
    salarioRetornado=Column(Float)
    imposto=Column(Float)
    moeda=Column(Float)
    time_created = Column(DateTime(timezone=True), server_default=func.now())
    colaborador=relationship("ConversoesColaboradores",back_populates="dadosConversao")