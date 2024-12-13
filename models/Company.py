from dataclasses import dataclass, asdict

from flask_login import UserMixin


@dataclass
class Company(UserMixin):
    id: int | None
    email: str
    new_name_company: str | None
    age: int | None
    city: str | None
    password: str

    def __dict__(self):
        return asdict(self)

    def get_id(self):
        return self.id