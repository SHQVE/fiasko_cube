import models
import database
from models.Car import Car
from models.Company import Company


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
        );
        CREATE TABLE IF NOT EXISTS Company (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                email TEXT NOT NULL,
                new_name_company TEXT NOT NULL,
                age TEXT NOT NULL,
                city TEXT NOT NULL,
                password TEXT NOT NULL,
                confirm_password TEXT NOT NULL
            );   
         CREATE TABLE IF NOT EXISTS Garage (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            company_id In,
            car_id int
            );   
        
    """)


def add_car(car: Car):
    db = database.get_db()
    db.execute(
        "insert into Cars (model, company_name, year_of_production, country_of_production, power, mileage, transmission, actuator, color, body, engine_displacement, status, price, password) values (?, ?, ?, ?, ?)",
        (car.model, car.company_name, car.year_of_production, car.country_of_production, car.color, car.price)
    )
    db.commit()


def get_cars():
    db = database.get_db()
    rows = db.execute("SELECT * FROM Cars").fetchall()
    return list(map(lambda row: Car(*row), rows))


def delete_car(car: models.Car):
    db = database.get_db()
    db.execute("DELETE FROM Cars WHERE id = ?", (car.id,))
    db.commit()
