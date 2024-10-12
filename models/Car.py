from dataclasses import dataclass


@dataclass
class Car:
    id: int
    model: str
    company_name: str
    year_of_production: int
    country_of_production: str
