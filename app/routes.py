from app import app
from werkzeug.urls import url_parse
from flask import render_template, flash, redirect, url_for, request
from app import forms_cadastro
from app.forms_contato import ContatoForm
from app.forms_login import LoginForm
from app.forms_cadastro import CadastroForm
from flask_login import current_user, login_user,  logout_user, login_required
from app.models import User
from app import db


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/contato', methods=['GET','POST'])
def contato():
    forms_contato = ContatoForm()
    if forms_contato.validate_on_submit():
        mensagem = flash('A mensagem foi enviada com sucesso.')
    return render_template('contato.html', forms_contato=forms_contato)
        

@app.route('/features')
def features():
    return render_template('features.html')

@app.route('/login', methods=['GET','POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('/'))
    forms_login = LoginForm()
    if forms_login.validate_on_submit():
        user = User.query.filter_by(nome=forms_cadastro.nome.data).first()
        if user is None or not user.check_password(forms_cadastro.senha.data):
            flash('Invalid username or password')
            return redirect(url_for('/login.html'))
        login_user(user, remember=forms_login.lembrar.data)
        return redirect(url_for('index'))
    return render_template('/login.html', forms_login=forms_login)

    
@app.route('/cadastro', methods=['GET','POST'])
def cadastro():
    if current_user.is_authenticated:
        return redirect(url_for('index.html'))
    forms_cadastro = CadastroForm()
    if forms_cadastro.validate_on_submit():
        user = User(nome=forms_cadastro.nome.data, email=forms_cadastro.email.data)
        user.set_password(forms_cadastro.senha.data)
        db.session.add(user)
        db.session.commit()
        flash('Parabens, sua conta foi criada com sucesso!!')
        return redirect(url_for('login'))
    return render_template('cadastro.html', forms_cadastro=forms_cadastro)

@app.route('/sair')
def sair():
    logout_user()
    return redirect(url_for('index'))

