from dataclasses import dataclass


@dataclass
class User:
    email: str
    name: str
    age: int
    city: str
    mod: str
    password: str
