from modelos.documento_transaccion import DocumentoTransaccion

class Factura(DocumentoTransaccion):
    __mapper_args__ = {'polymorphic_identity': 'factura'}
