from abc import ABC, abstractmethod
from excepciones import ClienteInvalidoError

class EntidadBase(ABC):
    """Clase abstracta para entidades generales [cite: 21]"""
    def __init__(self, id_sistema):
        self._id_sistema = id_sistema # Encapsulación [cite: 11]

class Cliente(EntidadBase):
    """Clase Cliente con validaciones robustas [cite: 22]"""
    def __init__(self, id_sistema, nombre, id_personal):
        super().__init__(id_sistema)
        if not nombre or not id_personal:
            raise ClienteInvalidoError("Nombre e identificación son obligatorios [cite: 19]")
        self.__nombre = nombre
        self.__id_personal = id_personal

    @property
    def nombre(self):
        return self.__nombre

class Servicio(ABC):
    """Clase abstracta para servicios de Software FJ [cite: 23]"""
    def __init__(self, nombre, costo_base):
        self.nombre = nombre
        self.costo_base = costo_base

    @abstractmethod
    def calcular_costo(self, cantidad, impuesto=0.19):
        """Método para polimorfismo [cite: 24]"""
        pass

class ReservaSalas(Servicio):
    def calcular_costo(self, horas, impuesto=0.19):
        # Sobrecarga: cálculo con impuesto opcional [cite: 26]
        return (self.costo_base * horas) * (1 + impuesto)

class AlquilerEquipos(Servicio):
    def calcular_costo(self, dias, impuesto=0.19):
        return (self.costo_base * dias) + 15000 # Cargo fijo adicional

class AsesoriaEspecializada(Servicio):
    def calcular_costo(self, sesiones, descuento=0.10):
        # Sobrecarga: cálculo con descuento en lugar de impuesto [cite: 26]
        return (self.costo_base * sesiones) * (1 - descuento)
