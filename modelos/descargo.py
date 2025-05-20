from modelos.documento_transaccion import DocumentoTransaccion

class Descargo(DocumentoTransaccion):
    __mapper_args__ = {'polymorphic_identity': 'descargo'}

    def agregar_servicio(self, servicio):
        self.lineas.append(servicio)
