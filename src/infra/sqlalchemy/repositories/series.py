from sqlalchemy.orm import Session
from src.infra.sqlalchemy.models import models
from src.schemas import schemas


class RepositorioSerie():
    def __init__(self, db: Session):
        self.db = db

    def criar(self, serie: schemas.Serie):
        db_serie = models.Serie(
            titulo=serie.titulo,
            ano=serie.ano,
            genero=serie.genero,
            qtd_temporadas=serie.qtd_temporadas,
            observacoes=serie.observacoes,
        )
        self.db.add(db_serie)
        self.db.commit()
        self.db.refresh(db_serie)
        return db_serie

    def listar(self):
        series = self.db.query(models.Serie).all()
        return series

    def obter(self):
        pass

    def remover(self, id_serie: str):
        serie = acharSeriePorId(id_serie,self.db.query(models.Serie).all())
        self.db.delete(serie)
        self.db.commit()
        return None


def acharSeriePorId(id: str, series: list):
    for serie in series:
        if serie.id == id:
            return serie
    return None
