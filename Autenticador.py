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
