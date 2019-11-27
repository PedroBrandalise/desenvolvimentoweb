from flask import Flask, render_template

app = Flask("app")


@app.route('/<nome>')
def hello(nome):
	return "Ola {}".format(nome)

@app.route('/cadastro', methods =['POST', 'GET'])
def cadastro():
	print ('ola')
	return render_template("form.html")


app.run()