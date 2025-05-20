from modelos.servicio import Servicio

class AtencionMedica(Servicio):
    def __init__(self, descripcion, precio):
        super().__init__(descripcion=descripcion, precio=precio)

class ExamenLab(Servicio):
    def __init__(self, descripcion, precio):
        super().__init__(descripcion=descripcion, precio=precio)

class ImagenRayosX(Servicio):
    def __init__(self, descripcion, precio):
        super().__init__(descripcion=descripcion, precio=precio)

class SuministroMedicamento(Servicio):
    def __init__(self, descripcion, precio):
        super().__init__(descripcion=descripcion, precio=precio)

class ProcedimientoMedico(Servicio):
    def __init__(self, descripcion, precio):
        super().__init__(descripcion=descripcion, precio=precio)
