from app import app
from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, SubmitField, FormField
from wtforms.validators import DataRequired
from flask_wtf.csrf import CSRFProtect

import os
SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY

class CadastroForm(FlaskForm):
    nome = StringField('nome', validators=[DataRequired()])
    email = EmailField('email', validators=[DataRequired()])
    telefone = StringField('telefone')
    submit = SubmitField('Enviar')

