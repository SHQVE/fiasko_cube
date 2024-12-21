from typing import final

from flask import Flask, render_template, redirect, request
from grz import generate_grz
from dataclasses import asdict
from random import randint
from flask_login import LoginManager, login_required, login_user, logout_user

import repositories
import grz
from forms.SignUpForm import SignUpForm
from forms.RegisterForm import RegisterForm
from forms.LoginForm import LoginForm
from models.Car import Car
from models.Company import Company
from repositories import create_table
from utilss import Link

cars = []
garage = []


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


def addCompany(email, new_name_company, age, city, password):
    company = Company(None, email, new_name_company, age, city, password)
    repositories.add_user(company)


@app.route('/')
def hello_world():
    return render_template("index.html")


login_manager = LoginManager()


@login_manager.user_loader
def load_company(company_id):
    return repositories.get_user(company_id)


@app.route('/register', methods=['GET', 'POST'])
def register():
    forma = RegisterForm()

    if forma.validate_on_submit():
        email = forma.email.data
        new_name_company = forma.new_name_company.data
        age = forma.age.data
        city = forma.city.data
        password = forma.password.data
        confirm_password = forma.confirm_password.data

        if password != confirm_password:
            return render_template(
                "formTemplate.html",
                form=forma,
                btn_name="Регистрация!",
                error="Пароли не совпадают!"
            )

        addCompany(email, new_name_company, age, city, password)
        return redirect("/company")

    return render_template("formTemplate.html", form=forma, btn_name="Регистрация!")


@app.route('/login', methods=['GET', 'POST'])
def login():
    formo = LoginForm()

    if formo.validate_on_submit():
        email = formo.email.data
        new_name_company = formo.new_name_company.data
        age = formo.age.data
        city = formo.city.data
        password = formo.password.data
        confirm_password = formo.confirm_password.data

        if password != confirm_password:
            return render_template(
                "formTemplate.html",
                form=formo,
                btn_name="Вход!",
                error="Пароли не совпадают!"
            )

        addCompany(email, new_name_company, age, city, password)
        return redirect("/company")

    return render_template("formTemplate.html", form=formo, btn_name="Вход!")


@app.route("/company/<int:company_id>")
@login_required
def getCompany(company_id: int):
    company = repositories.get_user()

    for companya in company:
        if companya.id == company_id:
            return render_template(
                "layout/car-layout.html",
                links=[
                    Link("Home", "/"),
                    Link("Add Company", "/add"),
                    Link("Delete Company", f"/delUser/{companya.id}", class_name="bg-danger"),
                ],
                companya=companya
            )

    return redirect("/")


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
    return render_template("cars/list.html", cars=garage, count=len(cars))


@app.route("/market", methods=['GET', 'POST'])
def marketplace():
    return render_template("cars/market.html", cars=cars)


@app.route("/buy/<car_id>", methods=['GET', 'POST'])
def buy_cars(car_id: str):
    if request.method == "POST":
        for i, car in enumerate(cars):
            if car.id == car_id:
                garage.append(cars.pop(i))
        return redirect("/garage")
    else:
        for car in cars:
            if car.id == car_id:
                return render_template("cars/buycar.html", car=car, garage=garage)
        return redirect("")


@app.route("/cars/<car_id>")
def getCar(car_id: str):
    for car in cars + garage:
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
    # login_manager.init_app(app)
    # app.app_context().push()
    # create_table()
    app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'
    app.run(debug=True, port=8888)
