import requests
import unittest
from flask.app import Flask

from flask.ext.testing import TestCase

json_mock = '{"imagem": "images/img001.png", "dica": "Comunista", "resposta": ' \
            '"Kent Beck", "topicos": ["projeto", "processo", "teste"]}'


class TestePictograma(TestCase):
    def create_app(self):
        app = Flask("pictosoft")
        app.config['TESTING'] = True
        return app

    # Testa pela criacao, busca e remocao de um pictograma
    # Este eh um teste de integracao! para funcionar, a aplicacao e o mongodb devem estar ligados
    def test_mongodb_mock(self):
        r = requests.post("http://0.0.0.0:8080/pictograma", data=json_mock)
        response_json = r.json()
        assert 'inseridos' in response_json
        assert len(response_json['inseridos']) == 1
        obj_id = response_json['inseridos'][0]
        r = requests.get("http://0.0.0.0:8080/pictograma/" + str(obj_id))
        response_json = r.json()
        assert type(response_json) is dict
        assert 'imagem' in response_json
        assert 'dica' in response_json
        assert 'resposta' in response_json
        assert 'topicos' in response_json
        assert len(response_json['topicos']) == 3
        r = requests.delete("http://0.0.0.0:8080/pictograma/" + str(obj_id))
        assert r.status_code == 200


if __name__ == '__main__':
    unittest.main()
