from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from app import login
from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    def set_password(self, senha):
        self.password_hash = generate_password_hash(senha)

    def check_password(self, senha):
        return check_password_hash(self.password_hash, senha)
    def __repr__(self):
        return '<User {}>'.format(self.nome)


    def __repr__(self):
        return '<Post {}>'.format(self.body)

class User(UserMixin, db.Model):
    @login.user_loader
    def load_user(id):
        return User.query.get(int(id))
