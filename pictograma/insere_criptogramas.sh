#!/usr/bin/env bash
curl -X POST http://0.0.0.0:8080/pictograma -d '[
{"imagem": "images/img001.png", "dica": "Comunista", "resposta": "Kent Beck", "topicos": ["projeto", "processo", "praticas"]},
{"imagem": "images/img002.png", "dica": "Usado para representar as coisas", "resposta": "UML", "topicos": ["processo", "entidades"]},
{"imagem": "images/img003.png", "dica": "Livro nao utilizado", "resposta": "CMM People", "topicos": ["projeto"]}
]'