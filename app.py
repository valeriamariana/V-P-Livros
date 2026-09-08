from datetime import datetime

from flask import Flask, flash, redirect, render_template, request, url_for

from db import db
from models import Livro


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///biblioteca.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SECRET_KEY"] = "chave-dev-vp-livros"


db.init_app(app)

with app.app_context():
    db.create_all()


def converter_data(valor):
    """Converte uma data do formulario (AAAA-MM-DD) para date ou None."""
    if not valor:
        return None
    return datetime.strptime(valor, "%Y-%m-%d").date()


@app.route("/")
def inicio():
    return redirect(url_for("listar_livros"))


# =========================
# READ - listar livros
# =========================
@app.route("/livros", methods=["GET"])
def listar_livros():
    livros = Livro.query.order_by(Livro.id_livro.desc()).all()
    return render_template("index.html", livros=livros)


# =========================
# CREATE - cadastrar livro
# =========================
@app.route("/livros/novo", methods=["GET", "POST"])
def novo_livro():
    if request.method == "POST":
        titulo = request.form.get("titulo", "").strip()

        if not titulo:
            flash("O título é obrigatório.", "erro")
            return render_template("novo.html")

        livro = Livro(
            titulo=titulo,
            sinopse=request.form.get("sinopse", "").strip() or None,
            capa=request.form.get("capa", "").strip() or None,
            num_paginas=int(request.form["num_paginas"]) if request.form.get("num_paginas") else None,
            data_public=converter_data(request.form.get("data_public")),
            arquivo=request.form.get("arquivo", "").strip() or None,
            editora=request.form.get("editora", "").strip() or None,
        )

        db.session.add(livro)
        db.session.commit()
        flash("Livro cadastrado com sucesso!", "sucesso")
        return redirect(url_for("listar_livros"))

    return render_template("novo.html")


# =========================
# UPDATE - editar livro
# =========================
@app.route("/livros/<int:id_livro>/editar", methods=["GET", "POST"])
def editar_livro(id_livro):
    livro = db.get_or_404(Livro, id_livro)

    if request.method == "POST":
        titulo = request.form.get("titulo", "").strip()

        if not titulo:
            flash("O título é obrigatório.", "erro")
            return render_template("editar.html", livro=livro)

        livro.titulo = titulo
        livro.sinopse = request.form.get("sinopse", "").strip() or None
        livro.capa = request.form.get("capa", "").strip() or None
        livro.num_paginas = int(request.form["num_paginas"]) if request.form.get("num_paginas") else None
        livro.data_public = converter_data(request.form.get("data_public"))
        livro.arquivo = request.form.get("arquivo", "").strip() or None
        livro.editora = request.form.get("editora", "").strip() or None

        db.session.commit()
        flash("Livro atualizado com sucesso!", "sucesso")
        return redirect(url_for("listar_livros"))

    return render_template("editar.html", livro=livro)


# =========================
# DELETE - excluir livro
# =========================
@app.route("/livros/<int:id_livro>/excluir", methods=["POST"])
def excluir_livro(id_livro):
    livro = db.get_or_404(Livro, id_livro)
    db.session.delete(livro)
    db.session.commit()
    flash("Livro excluído com sucesso!", "sucesso")
    return redirect(url_for("listar_livros"))


if __name__ == "__main__":
    app.run(debug=True)
