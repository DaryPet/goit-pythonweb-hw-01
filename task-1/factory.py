import logging
from abc import ABC, abstractmethod

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class Vehicle(ABC):
    def __init__(self, make: str, model: str) -> None:
        self.make: str = make
        self.model: str = model

    @abstractmethod
    def start_engine(self) -> None:
        pass


class Car(Vehicle):
    def start_engine(self) -> None:
        logger.info(f"{self.make} {self.model}: Двигун запущено")


class Motorcycle(Vehicle):

    def start_engine(self) -> None:
        logger.info(f"{self.make} {self.model}: Мотор заведено")


class VehicleFactory(ABC):
    @abstractmethod
    def create_car(self, make: str, model: str) -> Car:
        pass

    @abstractmethod
    def create_motorcycle(self, make: str, model: str) -> Motorcycle:
        pass


class USVehicleFactory(VehicleFactory):
    SPEC: str = "US Spec"

    def create_car(self, make: str, model: str) -> Car:
        return Car(make, f"{model} ({self.SPEC}")

    def create_motorcycle(self, make: str, model: str) -> Motorcycle:
        return Motorcycle(make, f"{model} ({self.SPEC})")


class EUVehicleFactory(VehicleFactory):
    SPEC: str = "EU Spec"

    def create_car(self, make: str, model: str) -> Car:
        return Car(make, f"{model} ({self.SPEC})")

    def create_motorcycle(self, make: str, model: str) -> Motorcycle:
        return Motorcycle(make, f"{model} ({self.SPEC})")


if __name__ == "__main__":
    us_factory: VehicleFactory = USVehicleFactory()
    eu_factory: VehicleFactory = EUVehicleFactory()

    vehicle1: Vehicle = us_factory.create_car("Ford", "Mustang")
    vehicle2: Vehicle = eu_factory.create_motorcycle("BMW", "R1250")

    vehicle1.start_engine()
    vehicle2.start_engine()
