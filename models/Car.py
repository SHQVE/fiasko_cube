from dataclasses import dataclass


@dataclass
class Car:
    id: str
    model: str
    company_name: str
    year_of_production: int
    country_of_production: str
    power: int
    mileage: int
    transmission: str
    actuator: str
    color: str
    steering_wheel: str
    body: str
    engine_displacement: int
    status: str
    price: int
