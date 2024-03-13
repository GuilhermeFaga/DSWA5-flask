from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField
from wtforms.validators import DataRequired


class UserForm(FlaskForm):
    nome = StringField("Informe o seu nome", validators=[DataRequired()])
    sobrenome = StringField("Informe o seu sobrenome", validators=[DataRequired()])
    instituicao = StringField(
        "Informe a sua Insituição de ensino", validators=[DataRequired()]
    )
    disciplina = SelectField(
        "Informe a sua disciplina",
        choices=[
            ("DSWA5", "DSWA5"),
            ("DSWA4", "DSWA4"),
            ("Gestão de projetos", "Gestão de projetos"),
        ],
        validators=[DataRequired()],
    )
    submit = SubmitField("Submit")
