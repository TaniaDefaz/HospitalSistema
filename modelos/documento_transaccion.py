from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from modelos.base import Base

class DocumentoTransaccion(Base):
    __tablename__ = 'documentos'

    id = Column(Integer, primary_key=True)
    nro = Column(String)
    fecha = Column(DateTime, default=datetime.utcnow)
    valor = Column(Float, default=0.0)
    paciente_id = Column(Integer, ForeignKey('pacientes.id'))

    lineas = relationship("LineaDocTransaccion", back_populates="documento")
