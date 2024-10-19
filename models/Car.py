from dataclasses import dataclass


@dataclass
class Car:
    id: str
    model: str
    company_name: str
    year_of_production: int
    country_of_production: str
