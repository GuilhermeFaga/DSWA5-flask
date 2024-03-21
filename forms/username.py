from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class UsernameForm(FlaskForm):
    username = StringField("Nome de usuário", validators=[DataRequired()])
    submit = SubmitField("Entrar")
