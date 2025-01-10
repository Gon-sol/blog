from flask_wtf import FlaskForm
from wtforms.fields import StringField, TextAreaField, SubmitField, PasswordField
from wtforms.validators import data_required, length, DataRequired, equal_to


class PostForm(FlaskForm):

    title = StringField("სათაური", validators=[DataRequired(), length(min=8, max=32)])
    description = TextAreaField("აღწერა", validators=[DataRequired(), length(min=8, max=1000)])

    submit = SubmitField("დადება")

class RegisterForm(FlaskForm):
    username = StringField('მომხმარებლის სახელი')
    password = PasswordField('პაროლი', validators=[DataRequired(), length(min=8)])
    repeat_password = PasswordField('გაიმეორეთ პაროლი', validators=[equal_to("password")])
    role = StringField('რა არის თქვენი როლი?')

    register = SubmitField('რეგისტრაცია')

class LoginForm(FlaskForm):
    username = StringField('მომხმარებლის სახელი')
    password = PasswordField('პაროლი', validators=[DataRequired(), length(min=8)])

    login = SubmitField('ავტორიზაცია')