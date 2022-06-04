from sqlalchemy import select,delete
from sqlalchemy.orm import Session

from models.models import VagasModels
from schemas.schema import Vaga

class VagaRepository():
    def __init__(self,database:Session):
        self.database=database

    def create(self,vaga:Vaga):
        db_vaga=VagasModels(tipo=vaga.tipo,modelo=vaga.modelo,descricao=vaga.descricao,periodo=vaga.periodo,
        requisito=vaga.requisito,tipo_contratacao=vaga.tipo_contratacao,beneficios=vaga.beneficios,id_empresa=vaga.id_empresa_token)
        self.database.add(db_vaga)
        self.database.commit()
        self.database.refresh(db_vaga)
        return db_vaga
    
    def delete_by_id(self,id):
        delete_vaga=delete(VagasModels).where(VagasModels.id==id)
        
        self.database.execute(delete_vaga)
        self.database.commit()
    
    def get_by_id(self,id):
        query=select(VagasModels).where(VagasModels.id_empresa == id)
        return self.database.execute(query).all()
    
    def getVagas(self):
        query=select(VagasModels)
        return self.database.execute(query).all()