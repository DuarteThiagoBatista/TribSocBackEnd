
from sqlalchemy import select,delete
from sqlalchemy.orm import Session
from models.models import EmpresasModels
from schemas.schema import Empresa

class EmpresaRepository():
    def __init__(self,database:Session):
        self.database=database
    
    def create(self,empresa:Empresa):
        db_empresa=EmpresasModels(nome=empresa.nome,localizacao=empresa.localizacao,email=empresa.email,password=empresa.password)
        self.database.add(db_empresa)
        self.database.commit()
        self.database.refresh(db_empresa)
        return db_empresa
    
    def get_by_email(self,email):
        query=select(EmpresasModels).where(EmpresasModels.email==email)
        return self.database.execute(query).scalar()

    def get_by_id_delete(self,id):
        delete_empresa=delete(EmpresasModels).where(EmpresasModels.id==id)
        self.database.execute(delete_empresa)
        self.database.commit()