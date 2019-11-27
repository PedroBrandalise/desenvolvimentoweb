from flask import request, render_template, redirect
from app import app
from app import db
from models import Produto


@app.route("/")
def index():
	# return render_template('index.html')
	return render_template('index.html')


@app.route('/produtos', methods = ['POST', 'GET'])
def mostraProdutos():	
	if(request.method =='GET'):
		produtos =  Produto.query.all()
		print(produtos)
		return render_template ('produtos.html', produtos = produtos)
	else:
		desc =request.form['desc']
		preco_custo = request.form['preco_custo']
		preco_venda = request.form['preco_venda']
		print(desc)
		print(preco_custo)
		print(preco_venda)
		prod = Produto(descricao =desc, preco_custo=preco_custo, preco_venda = preco_venda)
		db.session.add(prod)
		db.session.commit()
		return redirect('/produtos')

@app.route("/update/<id>", methods = ["POST", 'GET'])
def update(id):
	prod = Produto.query.get_or_404(id)
	if request.method == "POST":
		prod.descricao =request.form['desc']
		prod.preco_custo = request.form['preco_custo']
		prod.preco_venda = request.form['preco_venda']
		try:
			db.session.commit()
			return redirect("/produtos")
		except Exception as e:
			raise e
	else:
		return render_template('update.html', prod=prod)


@app.route("/delete/<int:id>")
def delete(id):
	prod = Produto.query.get_or_404(id)

	try:
		db.session.delete(prod)
		db.session.commit()
		return redirect("/produtos")
	except:
		return "error 2"