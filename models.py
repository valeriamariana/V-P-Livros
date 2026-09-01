from db import db
from datetime import datetime


class Livro(db.Model):
    __tablename__ = "livro"

    id_livro = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(50), nullable=False)
    sinopse = db.Column(db.Text)
    capa = db.Column(db.String(255))
    num_paginas = db.Column(db.Integer)
    data_public = db.Column(db.Date)
    arquivo = db.Column(db.String(255))
    editora = db.Column(db.String(100))
    data_cadastro = db.Column(db.DateTime, default=datetime.now)