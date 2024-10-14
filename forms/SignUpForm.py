from flask_wtf import FlaskForm
from wtforms.fields.choices import SelectField
from wtforms.fields.numeric import IntegerField
from wtforms.fields.simple import StringField, PasswordField, EmailField
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
    model = StringField('Модель авто', validators=[DataRequired()])
    company_name = StringField('Название компании!', validators=[DataRequired()])
    year_of_production = IntegerField('Год издания', default=2024, validators=[DataRequired()])
    country_of_production = StringField('Страна производства', validators=[DataRequired()])