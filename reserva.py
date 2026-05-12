from excepciones import ReservaIncorrectaError

class Reserva:
    def __init__(self, cliente, servicio, duracion):
        self.cliente = cliente
        self.servicio = servicio
        self.duracion = duracion
        self.estado = "Pendiente"

    def confirmar_reserva(self):
        try:
            if self.duracion <= 0:
                raise ReservaIncorrectaError("La duración debe ser mayor a cero")
            self.estado = "Confirmada"
            print(f"Reserva confirmada para {self.cliente.nombre}")
        except ReservaIncorrectaError as e:
            # Uso de raise para encadenamiento de excepciones si es necesario
            raise e
