from flask import Flask, escape, request
from flask import jsonify

listaClientes = {
        "1": { "nome": "Luciano Senger",    "bitcoins": "27"},
        "2": { "nome": "Eduardo Lima",      "bitcoins": "7"},
        "3": { "nome": "Selma Antunes",     "bitcoins": "9"},
        "4": { "nome": "Fabio Rafina",     "bitcoins": "10"},
        "5": { "nome": "Lucas Neto",       "bitcoins": "15"}
        }
        
listadenoticias = {"policial": "Compra de lancha de R$ 6 milhões ajudou a polícia a prender traficante ",
            "economia": "Concursos: veja 12 órgãos que abrem as inscrições nesta segunda-feira ",
            "ciencia":   "A pior hora do dia para ficar doente: Pesquisas mostram que a eficácia de vacinas é influenciada pelo relógio biológico"}


app = Flask("app")
@app.route("/")
def hello():
    return "Ola Mundo,  <strong> Estou aprendendo o framework flask", 200


@app.route("/noticias")
@app.route("/noticias/esportes")
def noticias():
    return u"" "Notícias !",200

@app.route("/noticias/<classe>")
def noticiasPorClasse(classe=None):
    cl = classe.lower()

    if cl == "ciencia":
        return listadenoticias[cl],200
    if cl == "policial":
        return listadenoticias[cl], 200
    if cl == "economia":
        return listadenoticias[cl], 200    
    return "notícia não encontrada !"


@app.route("/<name>")
def nome(name):
    if name.lower()=="luciano":
        return "Olá <strong>"+name+"</strong>",200
    else:
        return u"" "não encontrado", 404

@app.route("/principal")
def principal():
    return u"" " <html> <body> <h1> Página principal </h1> </body> </html> "

@app.route("/application")
def application():
    pessoas = [{"nome": "Bruno Rocha"},
               {"nome": "Arjen Lucassen"},
               {"nome": "Anneke van Giersbergen"},
               {"nome": "Steven Wilson"}]
    return jsonify(pessoas=pessoas, total=len(pessoas))     


@app.route('/blog/<int:postID>')
def show_blog(postID):
   return 'Blog Number %d' % postID

@app.route('/rev/<float:revNo>')
def revision(revNo):
   return 'Revision Number %f' % revNo      

@app.route('/hw')
def hw():
    name = request.args.get("name", "World")
    surname= request.args.get("surname", "Fantastic")
    return f'Hello, {escape(name)}  {escape(surname)}! '

@app.route('/clientes')
def clientes():
    for cl in listaClientes:
        if int(listaClientes[cl]['bitcoins']) > 9:
            print (listaClientes[cl]['nome'])
                
    print(request.environ['REMOTE_ADDR'])
    
    if 'chrome' in request.user_agent.browser:
        print("Usuario Chrome detectado")
    
    print(request.user_agent.browser)  
    
    return jsonify(cli=listaClientes, total=len(listaClientes)) 

@app.route('/check', methods=['POST', 'GET'])
def check():
    #print (request.headers)
    if(request.method == 'POST'):
        print("Tratamento dos valores recebidos...")
        email = request.form['email']
        passwd  = request.form['passwd']
        endereco = request.form['endereco']
        cidade = request.form['cidade']
        estado = request.form['estado']
      #  cep = request.form['cep']
      
        print (f"email..........................: {email}") 
        
        return '''
            <html>
            <head>
           
            <body>
            <h1> Dados digitados </h1>
            <table style="border: 3px solid black; ">
                    <th> <tr> <td> Campo </td> <td> Valor </td>
                    </th>
                    <tbody>
                    <tr> <td> Email </td> <td> {} </td>
                    <tr> <td> Passwd </td> <td> {} </td>
                    <tr> <td> Endereco </td> <td> {} </td>
                    <tr> <td> Cidade </td> <td> {} </td>
                    <tbody> </table> </body> </html>'''.format(email, passwd, endereco, cidade)

       # return  '''     <h1>The email is: {}</h1>
       #            <h1>The  passwd is: {}</h1>'''.format(email, passwd)

    else:
        return u"" " <html> <body> <h1> Página principal </h1> </body> </html> "
if __name__ == "__main__":
    app.run(debug=True)


