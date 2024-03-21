from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    username = StringField("Usuário ou e-mail", validators=[DataRequired()])
    password = PasswordField("Informe a sua senha", validators=[DataRequired()])
    submit = SubmitField("Entrar")
