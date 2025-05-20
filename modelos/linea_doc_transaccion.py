from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from modelos.base import Base

class LineaDocTransaccion(Base):
    __tablename__ = 'lineas'

    id = Column(Integer, primary_key=True)
    documento_id = Column(Integer, ForeignKey('documentos.id'))
    servicio_id = Column(Integer, ForeignKey('servicios.id'))

    documento = relationship("DocumentoTransaccion", back_populates="lineas")
    servicio = relationship("Servicio")
