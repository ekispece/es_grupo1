import json
import unittest

from flask.testsuite import FlaskTestCase

from app import app
from backend.pictograma import Pictograma

json_mock = '{"_id": "mock", "imagem": "images/img001.png", "dica": "Comunista", "resposta": "Kent Beck", "topicos":' \
            ' ["projeto", "processo", "teste"]}'


class TestePictograma(FlaskTestCase):
    def setUp(self):
        app.config['TESTING'] = True
        self.app = app.test_client()

    def test_deve_criar_objeto_de_json(self):
        picto = Pictograma.criar_objeto_de_json(json.loads(json_mock))

        assert picto is not None
        assert picto.dica == "Comunista"
        assert picto.resposta == "Kent Beck"


if __name__ == '__main__':
    unittest.main()
