from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from workout_api.contrib.models import BaseModel

class CentroTreinamentoModels(BaseModel):
    __tablename__ = "centro_treinamento"

    pk_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    nome: Mapped[str] = mapped_column(String(50), unique=True, nullable=False)
    endereço: Mapped[str] = mapped_column(String(60))
    proprietario: Mapped[str] = mapped_column(String(30))
    atleta: Mapped['AtletaModels'] = relationship(back_populates='centro_treinamento')