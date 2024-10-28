from typing import final

from flask import Flask, render_template, redirect
from grz import generate_grz
from dataclasses import asdict
from random import randint

import grz
from forms.SignUpForm import SignUpForm
from forms.form import GravitationForm
from models.Car import Car
from models.User import User

cars = []


# def generate_users(n: int):
#     for i in range(n):
#         age = randint(1, 100)
#         user = User(i, "test@example.com", "test", age, f"city{i}", "", "12345")
#         users.append(user)


def generate_cars(n: int):
    for i in range(n):
        grz_car = grz.generate_grz()
        car = Car(grz_car, "Corvette C7", "Chevrolet", 2019, "USA")
        cars.append(car)


# def addUser(email, name, age, city, password):
#     if len(users) == 0:
#         last_id = 0
#     else:
#         last_id = max(users, key=lambda x: x.id).id + 1
#
#     user = User(last_id, email, name, age, city, "", password)
#     users.append(user)


def addCar(model, company_name, year_of_production, country_of_production):

    grz_car = grz.generate_grz()
    car = Car(grz_car, model, company_name, year_of_production, country_of_production)
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


        addCar(model, company_name, year_of_production, country_of_production)
        return redirect("/garage")

    return render_template("formTemplate.html", form=form, btn_name="Зарегистрировать авто")


@app.route("/garage", methods=['GET', 'POST'])
def getCars():
    return render_template("cars/list.html", cars=cars, count=len(cars))


@app.route("/cars/<int:car_id>")
def getCar(car_id: str):
    for car in cars:
        if car.id == car_id:
            return asdict(car)

    return str(None)


@app.route("/delCar/<int:car_id>")
def delCar(car_id: str):
    for car in cars:
        if car.id == car_id:
            cars.remove(car)
            return asdict(car)

    return str(None)


if __name__ == '__main__':
    generate_cars(5)
    app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'
    app.run(debug=True, port=8888)
