from sqlalchemy import Column, Integer, String
from modelos.base import Base

class Paciente(Base):
    __tablename__ = 'pacientes'

    id = Column(Integer, primary_key=True)
    nombre = Column(String)
