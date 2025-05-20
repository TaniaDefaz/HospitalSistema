from sqlalchemy import create_engine
from modelos.base import Base
from modelos.paciente import Paciente
from modelos.documento_transaccion import DocumentoTransaccion
from modelos.factura import Factura
from modelos.descargo import Descargo
from modelos.linea_doc_transaccion import LineaDocTransaccion
from modelos.servicio import Servicio

engine = create_engine('sqlite:///hospital.db', echo=True)
Base.metadata.create_all(engine)
