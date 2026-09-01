from app import app

with app.test_client() as cliente:

    resposta = cliente.post(
        "/livros",
        data={
            "titulo": "O Senhor dos Anéis",
            "sinopse": "Uma aventura pela Terra-média.",
            "capa": "senhor_dos_aneis.jpg",
            "num_paginas": 500,
            "arquivo": "senhor_dos_aneis.pdf",
            "editora": "J. R. R. Tolkien"
        }
    )

    print("Primeiro livro:")
    print(resposta.data.decode())


    resposta = cliente.post(
        "/livros",
        data={
            "titulo": "Harry Potter e a Pedra Filosofal",
            "sinopse": "Um jovem descobre que é um bruxo.",
            "capa": "harry_potter.jpg",
            "num_paginas": 309,
            "arquivo": "harry_potter.pdf",
            "editora": "J. K. Rowling"
        }
    )

    print("Segundo livro:")
    print(resposta.data.decode())