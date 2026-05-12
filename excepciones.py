class SoftwareFJError(Exception):
    """Excepción base para el sistema Software FJ [cite: 10]"""
    pass

class ClienteInvalidoError(SoftwareFJError):
    """Error cuando los datos del cliente no son válidos [cite: 19, 22]"""
    pass

class ServicioNoDisponibleError(SoftwareFJError):
    """Error cuando un servicio no puede procesarse [cite: 19]"""
    pass

class ReservaIncorrectaError(SoftwareFJError):
    """Error para intentos de reserva fallidos [cite: 25]"""
    pass
