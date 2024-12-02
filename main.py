from typing import final

from flask import Flask, render_template, redirect, request
from grz import generate_grz
from dataclasses import asdict
from random import randint

import grz
from forms.SignUpForm import SignUpForm
from forms.form import GravitationForm
from models.Car import Car
from models.User import User

cars = []


def generate_cars(n: int):
    for i in range(n):
        grz_car = grz.generate_grz()
        car = Car(grz_car, "Corvette C7", "Chevrolet", 2019, "USA", 1000, 500, "Механическая", "Задний", "Черный",
                  "Правый", "Лифтбэк", 3.5, "небитый", 3500000)
        cars.append(car)


def addCar(grz_car, model, company_name, year_of_production, country_of_production, power, mileage, transmission,
           actuator, color, steering_wheel, body, engine_displacement, status, price):
    car = Car(grz_car, model, company_name, year_of_production, country_of_production, power, mileage, transmission,
              actuator, color, steering_wheel, body, engine_displacement, status, price)
    cars.append(car)


app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template("index.html")


@app.route("/signUp", methods=['GET', 'POST'])
def signUp():
    form = SignUpForm()

    if form.validate_on_submit():
        model = form.model.data
        company_name = form.company_name.data
        year_of_production = form.year_of_production.data
        country_of_production = form.country_of_production.data
        power = form.power.data
        mileage = form.mileage.data
        transmission = form.transmission.data
        actuator = form.actuator.data
        color = form.color.data
        steering_wheel = form.steering_wheel.data
        body = form.body.data
        engine_displacement = form.engine_displacement.data
        status = form.status.data
        fileimage = request.files["image"]
        price = form.price.data

        car_grz = generate_grz()
        root = app.root_path
        fileimage.save(f"{root}\static\images/{car_grz}.{fileimage.filename.split('.')[-1]}")

        addCar(car_grz, model, company_name, year_of_production, country_of_production, power, mileage, transmission,
               actuator, color, steering_wheel, body, engine_displacement, status, price)
        return redirect("/garage")

    return render_template("formTemplate.html", form=form, btn_name="Зарегистрировать авто")


@app.route("/garage", methods=['GET', 'POST'])
def getCars():
    return render_template("cars/list.html", cars=cars, count=len(cars))


@app.route("/market", methods=['GET', 'POST'])
def marketplace():
    return render_template("cars/market.html", cars=cars)


@app.route("/cars/<car_id>")
def getCar(car_id: str):
    for car in cars:
        if car.id == car_id:
            return render_template("cars/car.html", car=car)

    return str(None)


@app.route("/delCar/<car_id>")
def delCar(car_id: int):
    for car in cars:
        if car.id == car_id:
            cars.remove(car)
            return asdict(car)

    return str(None)


if __name__ == '__main__':
    generate_cars(1)
    app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'
    app.run(debug=True, port=8888)
