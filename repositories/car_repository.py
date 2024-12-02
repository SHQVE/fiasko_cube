import models
import database


def create_table():
    db = database.get_db()
    db.execute("""
        CREATE TABLE IF NOT EXISTS Cars (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            model TEXT NOT NULL,
            company_name TEXT NOT NULL,
            year_of_production TEXT NOT NULL,
            country_of_production TEXT NOT NULL,
            power TEXT NOT NULL,
            mileage TEXT NOT NULL,
            transmission TEXT NOT NULL,
            actuator TEXT NOT NULL,
            color INTEGER NOT NULL,
            body TEXT NOT NULL,
            engine_displacement TEXT NOT NULL,
            status TEXT NOT NULL,
            price TEXT NOT NULL
        )
    """)


def add_car(car: models.Car):
    db = database.get_db()
    db.execute(
        "insert into Cars (email, name, age, city, password) values (?, ?, ?, ?, ?)",
        (car.model, car.company_name, car.year_of_production, car.country_of_production, car.color, car.price)
    )
    db.commit()


def get_cars():
    db = database.get_db()
    rows = db.execute("SELECT * FROM Cars").fetchall()
    return list(map(lambda row: models.Car(*row), rows))


def delete_car(car: models.Car):
    db = database.get_db()
    db.execute("DELETE FROM Cars WHERE id = ?", (car.id,))
    db.commit()
