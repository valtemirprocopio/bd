from app import app
from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, SubmitField, PasswordField, FileField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo
from flask_wtf.csrf import CSRFProtect
from app.models import User


import os
SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY

class CadastroForm(FlaskForm):
    nome = StringField('nome', validators=[DataRequired()])
    email = EmailField('email', validators=[DataRequired(), Email()])
    senha = PasswordField('senha', validators=[DataRequired()])
    repete_senha = PasswordField('Repita a senha', validators=[DataRequired(), EqualTo('senha')])
    submit = SubmitField('Enviar')
    def validate_username(self, nome):
        user = User.query.filter_by(nome=nome.data).first()
        if user is not None:
            raise ValidationError('Por favor, use um nome diferente!')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('Por favor, use um e-mail diferente!')

