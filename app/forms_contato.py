from app import app
from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, TextAreaField, FileField, SubmitField
from wtforms.validators import DataRequired
from flask_wtf.csrf import CSRFProtect
import os
SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY

class ContatoForm(FlaskForm):
    nome = StringField('nome', validators=[DataRequired()])
    email = EmailField('email', validators=[DataRequired()])
    assunto = StringField('assunto', validators=[DataRequired()])
    mensagem = TextAreaField('mensagem', validators=[DataRequired()])
    submit = SubmitField('Enviar')
