from typing import final

from flask import Flask, render_template, redirect
from dataclasses import asdict
from random import randint

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
        id = randint(100, 1000)
        car = Car(i, "Corvette C7", "Chevrolet", 2019, "USA")
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
    if len(cars) == 0:
        final_id = 100
    else:
        final_id = max(cars, key=lambda x: x.id).id +1

        car = Car(final_id, model, company_name, year_of_production, country_of_production)
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
        return redirect("/cars")

    return render_template("formTemplate.html", form=form, btn_name="Зарегистрировать авто")


@app.route("/cars", methods=['GET', 'POST'])
def getCars():
    return cars


@app.route("/cars/<int:car_id>")
def getCar(car_id: int):
    for car in cars:
        if car.id == car_id:
            return asdict(car)

    return str(None)


@app.route("/delCar/<int:car_id>")
def delCar(car_id: int):
    for car in cars:
        if car.id == car_id:
            cars.remove(car)
            return asdict(car)

    return str(None)


if __name__ == '__main__':
    generate_cars(2)
    app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'
    app.run(debug=True, port=8888)
