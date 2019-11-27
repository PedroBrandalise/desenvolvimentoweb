from flask import Flask,render_template, request, json
from flask import jsonify

app = Flask("app")

@app.route('/')
def hello():
    return  render_template("index.html")

@app.route("/pessoas", methods=['POST'])
def application():
    pessoas = [{"nome": "Anselmo Rocha"},
               {"nome": "Arjen Lucassen"},
               {"nome": "Anneke van Giersbergen"},
               {"nome": "Steven Wilson"}]
    return jsonify(pessoas=pessoas, total=len(pessoas)) 

if __name__=="__main__":
    app.run()


