from typing import Optional
from pydantic import BaseModel

class Serie(BaseModel):
    id: Optional[str] = None
    titulo: str
    ano: int
    genero: str
    qtd_temporadas: int
    observacoes: Optional[str] = None

    class Config:
        orm_mode = True
