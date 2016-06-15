import requests
import unittest
import json
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

    def test_pictogramas_aleatorios(self):
		ids_inseridos = []
		numero_pictogramas = 10
		for i in range(numero_pictogramas):
			r = requests.post("http://0.0.0.0:8080/pictograma", data=json_mock)
			response_json = r.json()
			obj_id = response_json['inseridos'][0]
			ids_inseridos.append(str(obj_id))
		r = requests.get("http://0.0.0.0:8080/pictograma")
		response_json = r.json()
		assert len(response_json) is 10
		for i in range(numero_pictogramas):
			assert type(response_json[i]) is dict
			assert 'imagem' in response_json[i]
			assert 'dica' in response_json[i]
			assert 'resposta' in response_json[i]
			assert 'topicos' in response_json[i]
		for i in range(numero_pictogramas):
			r = requests.delete("http://0.0.0.0:8080/pictograma/" + ids_inseridos[i])
			assert r.status_code == 200

    def test_pictogramas_aleatorios_topicos(self):
		ids_inseridos = []
		numero_pictogramas = 10
		topicos_json = json.loads(json_mock)['topicos']
		topicos = [str(topico) for topico in topicos_json]
		intersecao_topicos = False 
		for i in range(numero_pictogramas):
			r = requests.post("http://0.0.0.0:8080/pictograma", data=json_mock)
			response_json = r.json()
			obj_id = response_json['inseridos'][0]
			ids_inseridos.append(str(obj_id))
		args = "?topicos=" + topicos[0]
		args_resto = ""
		for i in range(1,len(topicos)):
			args_resto += "&topicos=" + topicos[i]
		args += args_resto
		r = requests.get("http://0.0.0.0:8080/pictograma" + args)
		response_json = r.json()
		assert len(response_json) is 10
		for i in range(numero_pictogramas):
			assert type(response_json[i]) is dict
			assert 'imagem' in response_json[i]
			assert 'dica' in response_json[i]
			assert 'resposta' in response_json[i]
			assert 'topicos' in response_json[i]			
			topicos_retornados = [str(topico) for topico in response_json[i]['topicos']]
			for topico in topicos:
				if topico in topicos_retornados:
					intersecao_topicos = True
					break
			assert intersecao_topicos
		for i in range(numero_pictogramas):
			r = requests.delete("http://0.0.0.0:8080/pictograma/" + ids_inseridos[i])
			assert r.status_code == 200	
	

			
if __name__ == '__main__':
    unittest.main()
