from entity.empresaEntity import EmpresaEntity
from models.empresaModels import *
from sqlalchemy.orm import Session



class RepositorioEmpresa():
    def __init__(self,db:Session):
        self.db=db
    
    def criar(self,empresa:EmpresaEntity):
        db_empresa=EmpresaModels(nome=empresa.nome,localizacao=empresa.localizacao,modelo=empresa.modelo,vagaTipo=empresa.vagaTipo,salario=empresa.salario,detalhamento_vaga=empresa.detalhamento_vaga,vagas_restante=empresa.vagas_restante,email=empresa.email,password=empresa.password )
        self.db.add(db_empresa)
        self.db.commit()
        self.db.refresh(db_empresa)
        return db_empresa
    
    def listar(self):
        empresas= self.db.query(EmpresaModels).all()
        return empresas