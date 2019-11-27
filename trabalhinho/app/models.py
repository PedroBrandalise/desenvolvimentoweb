from app import db


class Produto(db.Model):
	__tablename__ = 'produto'
	id = db.Column(db.Integer, primary_key= True)
	descricao = db.Column(db.String(120))
	preco_custo = db.Column(db.Float)
	preco_venda = db.Column(db.Float)

	def __repr__(self):
		return '<Produto: {}\nPreço: {}>'.format(self.descricao, self.preco_venda)  