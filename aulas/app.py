from flask import Flask, render_template, request, json
from flask import jsonify

app = Flask("app")

# view / rota
#@app.route("/")
#def hello():
#    #return "<h1> Ola Mundo, <strong> estou aprendendo o framework Flask </strong> </h1> ", 200
#    return render_template("form.html")

@app.route("/uepg")
@app.route("/deinfo")
def uepg():
    return render_template("index.html")
    #return "<h3> Ola UEPG </h3"

@app.route("/uepg/<nome>")
def hello_nome(nome):
    return "Ola {}".format(nome)

@app.route("/deinfo/<nome>")
def deinfo_nome(nome):
    if nome.lower() == "luciano":
        return  "Ola {}".format(nome), 200
    else:
        return "Nao encontrado", 404 

@app.route("/", methods=['POST', 'GET'])
@app.route("/login", methods=['POST', 'GET'])
def login():
    if request.method == "POST":
        print(request.form['nome'])
        print(request.form['passwd'])
        print(request.user_agent.browser)
        endereco = request.environ['REMOTE_ADDR']
        nome = request.form['nome']
        passwd = request.form['passwd']
        if 'chrome' in request.user_agent.browser:
            return "Ola {0} , sua senha é {1} e seu IP e {2}".format(nome, passwd, endereco), 200
        else:
            return "Sem informações.", 404
    else:
        return render_template("form.html")
    

if __name__ == "__main__":
    app.run()
