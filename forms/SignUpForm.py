from flask_wtf import FlaskForm
from wtforms.fields.choices import SelectField
from wtforms.fields.numeric import IntegerField, FloatField
from wtforms.fields.simple import StringField, PasswordField, EmailField, FileField
from wtforms.validators import DataRequired, Email


# pip install email-validator

# class SignUpForm(FlaskForm):
#     email = EmailField('Электронная почта', validators=[DataRequired(), Email()])
#     name = StringField('Имя', validators=[DataRequired()])
#     age = IntegerField('Возраст', default=18)
#     city = StringField('Город', validators=[DataRequired()])
#     gender = SelectField('Пол', choices=[("М", "Мужской"), ("Ж", "Женский")])
#     mod = SelectField('Мод авто', choices=[("Drift", "дрифт"), ("Light", "комфорт")])
#     password = PasswordField('Пароль', validators=[DataRequired()])
#     consfirm_password = PasswordField('Подтвердите пароль', validators=[DataRequired()])


class SignUpForm(FlaskForm):
    company_name = StringField('Марка авто', validators=[DataRequired()])
    model = StringField('Модель авто', validators=[DataRequired()])
    year_of_production = IntegerField('Год', default=2024, validators=[DataRequired()])
    country_of_production = SelectField('Страна', choices=[("Russia", "Россия"), ("USA", "Америка"),
                                              ("Japan", "Япония")])
    power = IntegerField('Мощность', validators=[DataRequired()])
    mileage = IntegerField('Пробег', validators=[DataRequired()])
    transmission = SelectField('КПП', choices=[("Automatic", "Автоматическая"), ("Mechanical", "Механика"),
                                               ("Robotic", "Роботизированная"), ("Variative", "Вариативная")])
    actuator = SelectField('Привод', choices=[("Rear", "Задний (RWD)"), ("Front", "Передний (FWD)"),
                                              ("Full", "Полный (AWD / 4WD)")])
    color = SelectField('Цвет авто',
                        choices=[("Red", "Красный"), ("White", "Белый"), ("Black", "Черный"), ("Blue", "Синий"),
                                 ("Green", "Зеленый"), ("Yellow", "Желтый"),
                                 ("Orange", "Оранжевый"),
                                 ("Purple", "Фиолетовый"),
                                 ("Pink", "Розовый"),
                                 ("Brown", "Коричневый"),
                                 ("Gray", "Серый"),
                                 ("Silver", "Серебряный"),
                                 ("Gold", "Золотой"),
                                 ("Cyan", "Бирюзовый"),
                                 ("Magenta", "Пурпурный")])
    steering_wheel = SelectField('Руль', choices=[("Left", "Левый"), ("Right", "Правый")])
    body = SelectField('Кузов',
                       choices=[("Sedan", "Седан"),
                                ("Coupe", "Купе"),
                                ("Liftback", "Лифтбэк"),
                                ("Hatchback", "Хэтчбек"),
                                ("SUV", "Внедорожник"),
                                ("Minivan", "Минивэн"),
                                ("Pickup", "Пикап"),
                                ("Convertible", "Кабриолет"),
                                ("Wagon", "Универсал"),
                                ("Crossover", "Кроссовер"),
                                ("Roadster", "Родстер"),
                                ("Van", "Фургон"),
                                ("Limousine", "Лимузин"),
                                ("Targa", "Тарга")])
    engine_displacement = FloatField('Объем двигателя  л^3', default=1, validators=[DataRequired()])
    status = SelectField('Состояние',
                         choices=[("Battered", "Битый"),
                                  ("Unscathed", "Небитый")])
    image = FileField("img (Обязательно фото размером 320 x 214! )")
    price = IntegerField('Цена', validators=[DataRequired()])
