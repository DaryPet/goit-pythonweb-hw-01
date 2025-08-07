import logging
from abc import ABC, abstractmethod

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class Vehicle(ABC):
    def __init__(self, make: str, model: str) -> None:
        self.make = make
        self.model = model

    @abstractmethod
    def start_engine(self) -> None:
        pass


class Car(Vehicle):
    def __init__(self, make: str, model: str) -> None:
        super().__init__(make, model)

    def start_engine(self) -> None:
        logger.info(f"{self.make} {self.model}: Двигун запущено")


class Motorcycle(Vehicle):
    def __init__(self, make: str, model: str) -> None:
        super().__init__(make, model)

    def start_engine(self) -> None:
        logger.info(f"{self.make} {self.model}: Мотор заведено")


class VehicleFactory(ABC):
    @abstractmethod
    def create_car(self, make: str, model: str) -> Vehicle:
        pass

    @abstractmethod
    def create_motorcycle(self, make: str, model: str) -> Vehicle:
        pass


class USVehicleFactory(VehicleFactory):
    def create_car(self, make: str, model: str) -> Vehicle:
        return Car(make, f"{model} (US Spec)")

    def create_motorcycle(self, make: str, model: str) -> Vehicle:
        return Motorcycle(make, f"{model} (US Spec)")


class EUVehicleFactory(VehicleFactory):
    def create_car(self, make: str, model: str) -> Vehicle:
        return Car(make, f"{model} (EU Spec)")

    def create_motorcycle(self, make: str, model: str) -> Vehicle:
        return Motorcycle(make, f"{model} (EU Spec)")


if __name__ == "__main__":
    us_factory = USVehicleFactory()
    eu_factory = EUVehicleFactory()

    vehicle1 = us_factory.create_car("Ford", "Mustang")
    vehicle2 = eu_factory.create_motorcycle("BMW", "R1250")

    vehicle1.start_engine()
    vehicle2.start_engine()
