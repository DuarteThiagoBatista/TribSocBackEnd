from sqlalchemy import select, delete
from sqlalchemy.orm import Session
from schemas.schema import Colaborador,DadosConversao
from models.models import ColaboradoresModels,ConversoesColaboradores,DadosConversaoModels
from datetime import datetime

class ColaboradorRepositpory():
    def __init__(self,database:Session):
        self.database=database 
    
    def create(self,colaborador:Colaborador):
        db_colaborador=ColaboradoresModels(nome=colaborador.nome,email=colaborador.email,password=colaborador.password)
        self.database.add(db_colaborador)
        self.database.commit()
        self.database.refresh(db_colaborador)
        return db_colaborador
    
    def get_by_email(self,email):
        query=select(ColaboradoresModels).where(ColaboradoresModels.email==email)
        return self.database.execute(query).scalar()
    
    def createDadosCoversao(self,dados:DadosConversao):
        db_dados_conversao=DadosConversaoModels(salarioInserido=dados.salarioInserido,
        salarioConvertido=dados.salarioConvertido,
        salarioDescontado=dados.salarioDescontado,salarioRetornado=dados.salarioRetornado,
        imposto=dados.imposto,moeda=dados.moeda)
        self.database.add(db_dados_conversao)
        self.database.commit()
        self.database.refresh(db_dados_conversao)

        print(db_dados_conversao.id)
        db_Conversoes_Colaboradore=ConversoesColaboradores(idColaborador=dados.idColaborador,
        idDadosConversao=db_dados_conversao.id)
        self.database.add(db_Conversoes_Colaboradore)
        self.database.commit()
        self.database.refresh(db_Conversoes_Colaboradore)
        return db_dados_conversao
    
    def delete_by_id(self,id):
        delete2=delete(ConversoesColaboradores).where(ConversoesColaboradores.idDadosConversao==id)
        deletee= delete(DadosConversaoModels).where(DadosConversaoModels.id == id)
        self.database.execute(delete2)
        self.database.execute(deletee)
        self.database.commit()



