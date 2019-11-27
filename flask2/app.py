# -*- coding: utf-8 -*-

from flask import Flask

app = Flask('app')



@app.route('/')
def hello():
	return "ola mundo!", 200

@app.route('/uepg')
def uepg():
	return "ola UEPG", 200	

@app.route('/uepg/<nome>')
def uepg2(nome):
	return "olá {}".format(nome)

app.run()