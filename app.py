from flask import Flask, request
from models import db, Livro

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///biblioteca.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)

with app.app_context():
    db.create_all()

@app.route("/")
def inicio():
    return "Backend da biblioteca funcionando!"

@app.route("/livros", methods=["POST"])
def inserir_livro():

    titulo = request.form["titulo"]
    sinopse = request.form.get("sinopse")
    capa = request.form.get("capa")
    num_paginas = request.form.get("num_paginas")
    arquivo = request.form.get("arquivo")
    editora = request.form.get("editora")

    livro = Livro(
        titulo=titulo,
        sinopse=sinopse,
        capa=capa,
        num_paginas=num_paginas,
        arquivo=arquivo,
        editora=editora
    )

    db.session.add(livro)
    db.session.commit()

    return "Livro inserido com sucesso!"

@app.route("/livros", methods=["GET"])
def listar_livros():

    livros = Livro.query.all()

    resultado = ""

    for livro in livros:
        resultado += "ID: " + str(livro.id_livro) + "\n"
        resultado += "Título: " + str(livro.titulo) + "\n"
        resultado += "Sinopse: " + str(livro.sinopse) + "\n"
        resultado += "Número de páginas: " + str(livro.num_paginas) + "\n"
        resultado += "Capa: " + str(livro.capa) + "\n"
        resultado += "Arquivo: " + str(livro.arquivo) + "\n"
        resultado += "Editora: " + str(livro.editora) + "\n"
        resultado += "-------------------------\n"

    return resultado

if __name__ == "__main__":
    app.run(debug=True)