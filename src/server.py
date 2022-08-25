from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session

from src.infra.sqlalchemy.config.database import criar_db, get_db
from src.infra.sqlalchemy.repositories.series import RepositorioSerie
from src.schemas.schemas import Serie

criar_db()
app = FastAPI()


@app.get("/series")
def listar_series(db: Session = Depends(get_db)):
    series = RepositorioSerie(db).listar()
    return series


@app.post("/series")
def criar_serie(serie: Serie, db: Session = Depends(get_db)):
    produto_criado = RepositorioSerie(db).criar(serie)
    return produto_criado


@app.delete("/series")
def deletar_serie(id: str, db: Session = Depends(get_db)):
    RepositorioSerie(db).remover(id)
    return {"Mensagem": "Series deletada"}
