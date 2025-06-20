from abc import ABC, abstractmethod


# Implementing abstract classes for better type support
class Vehicle(ABC):
    @abstractmethod
    def __str__(self) -> str:
        pass

    def move(self) -> None:
        print("Moviendo el vehiculo...")


class Engine(ABC):
    @abstractmethod
    def __str__(self) -> str:
        pass

    def start(self) -> None:
        print("Iniciando el motor...")


class Car(Vehicle):
    def __str__(self) -> str:
        return "Carro"


class CombustionEngine(Engine):
    def __str__(self) -> str:
        return "Motor de combustion"


class Boat(Vehicle):
    def __str__(self) -> str:
        return "Lancha"


class NauticalEngine(Engine):
    def __str__(self) -> str:
        return "Motor Nautico"


class VehicleFactory(ABC):
    @abstractmethod
    def create_vehicle(self) -> Vehicle:
        pass

    @abstractmethod
    def create_engine(self) -> Engine:
        pass


class LandVehicleFactory(VehicleFactory):

    def create_vehicle(self) -> Vehicle:
        vehicle = Car()
        print(f"Creando vehiculo terrestre: {vehicle}")
        return vehicle

    def create_engine(self) -> Engine:
        engine = CombustionEngine()
        print(f"Usando Motor: {engine}")
        return engine


class AquaticVehicleFactory(VehicleFactory):

    def create_vehicle(self) -> Vehicle:
        vehicle = Boat()
        print(f"Creando vehiculo acuatico: {vehicle}")
        return vehicle

    def create_engine(self) -> Engine:
        engine = NauticalEngine()
        print(f"Usando motor: {engine}")
        return engine


# Client code
def generate_transport(factory: VehicleFactory):
    vehicle = factory.create_vehicle()
    engine = factory.create_engine()

    engine.start()
    vehicle.move()

generate_transport(LandVehicleFactory())
generate_transport(AquaticVehicleFactory())
