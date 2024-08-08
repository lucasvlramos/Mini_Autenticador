from flask import Flask, request, abort
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__aut__)

# Configuração do banco de dados SQLite
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cartoes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Configuração das credenciais básicas de autenticação HTTP
app.config['HTTP_AUTH_USERNAME'] = 'username'
app.config['HTTP_AUTH_PASSWORD'] = 'password'

# Inicialização do SQLAlchemy
db = SQLAlchemy(app)

class Cartao(db.Model):
    numero_cartao = db.Column(db.String(16), primary_key=True)
    senha_hash = db.Column(db.String(128), nullable=False)
    saldo = db.Column(db.Float, default=500.0, nullable=False)

    def __init__(self, numero_cartao, senha):
        self.numero_cartao = numero_cartao
        self.senha_hash = generate_password_hash(senha)

    def verificar_senha(self, senha):
        return check_password_hash(self.senha_hash, senha)

def verificar_autenticacao():
    auth = request.authorization
    if not auth or auth.username != app.config['HTTP_AUTH_USERNAME'] or auth.password != app.config['HTTP_AUTH_PASSWORD']:
        abort(401)


with app.app_context():
    db.create_all()


