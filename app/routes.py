from app import app
from flask import render_template, flash, redirect, url_for
from app.forms_contato import ContatoForm
from app.forms_login import LoginForm

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/contato', methods=['GET','POST'])
def contato():
    forms_contato = ContatoForm()
    if forms_contato.validate_on_submit():
        mensagem = flash('A mensagem foi enviada com sucesso.')
        return redirect('/index')
    return render_template('contato.html', forms_contato=forms_contato)
        

@app.route('/features')
def features():
    return render_template('features.html')

@app.route('/login', methods=['GET','POST'])
def login():
    forms_login = LoginForm()
    return render_template('/login.html', forms_login=forms_login)
