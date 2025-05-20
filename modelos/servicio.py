from modelos.base import Base
from sqlalchemy import Column, Integer, String, Float

class Servicio(Base):
    __tablename__ = 'servicios'
    id = Column(Integer, primary_key=True)
    descripcion = Column(String)
    precio = Column(Float)
    origen = Column(String, default='base')  # <-- nuevo campo
