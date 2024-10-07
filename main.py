from flask import Flask, render_template, redirect

from forms.SignUpForm import SignUpForm
from forms.form import GravitationForm
from models import *

users = []

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template("index.html")



@app.route("/signUp", methods=['GET', 'POST'])
def signUp():
    form = SignUpForm()

    if form.validate_on_submit():
        email = form.email.data
        name = form.name.data
        age = form.age.data
        city = form.city.data
        mod = form.mod.data
        password = form.password.data
        confirm_password = form.consfirm_password.data

        if password != confirm_password:
            return render_template(
                "formTemplate.html",
                form=form,
                btn_name="Регистрация!",
                error="Пароли не совпадают!"
            )

        user = User(email, name, age, city, mod, password)
        users.append(user)

        return redirect("/users")

    return render_template("formTemplate.html", form=form, btn_name="Регистрация!")


@app.route("/users", methods=['GET', 'POST'])
def getUsers():
    return users


if __name__ == '__main__':
    app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'
    app.run(debug=True, port=8888)
