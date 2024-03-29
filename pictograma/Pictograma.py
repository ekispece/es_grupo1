import json
import random
import string
from random import randint, shuffle, sample

from bson.objectid import ObjectId

from app import mongo


class Pictograma:
    def __init__(self, imagem, dica, resposta, topicos, _id=None):

        if imagem is None:
            raise TypeError("Campo imagem nao deve ser nulo")

        if dica is None:
            raise TypeError("Campo dica nao deve ser nulo")

        if resposta is None:
            raise TypeError("Campo resposta nao deve ser nulo")

        if topicos is None:
            raise TypeError("Campo topicos nao deve ser nulo")

        if len(topicos) == 0:
            raise TypeError("Campo topicos deve incluir ao menos um topico")

        self.imagem = imagem
        self.dica = dica
        self.resposta = resposta
        self.topicos = topicos
        self._id = _id

        self.letras = list(resposta.lower())

        assert len(self.letras) <= 13

        while len(self.letras) < 13:
            self.letras.append(random.choice(string.lowercase))

        assert len(self.letras) == 13
        shuffle(self.letras)

        self.pict_json = {
            '_id': self._id,
            'imagem': self.imagem,
            'dica': self.dica,
            'resposta': self.resposta,
            'topicos': self.topicos,
            'letras': self.letras
        }

    def __str__(self):
        return "Pictograma [ \'imagem\': " + self.imagem + ", \'dica\': " + self.dica + ", \'resposta\': " + \
               self.resposta + ", \'topicos_len\': " + str(len(self.topicos)) + "]"

    def get_as_json(self):
        return json.dumps(self.pict_json)


def get_list_as_json(lista_pictogramas):
    return json.dumps([pictograma.pict_json for pictograma in lista_pictogramas])


def criar_objeto_de_json(pict_json):
    return Pictograma(imagem=pict_json['imagem'], dica=pict_json['dica'], resposta=pict_json['resposta'],
                      topicos=pict_json['topicos'], _id=str(pict_json['_id']))


def pictograma_aleatorio():
    skip = randint(0, mongo.db.pictogramas.find().count() - 1)
    return criar_objeto_de_json(mongo.db.pictogramas.find().skip(skip).next())


def buscar_pictogramas(topicos):
    tamanho = 5  # numero desejado de pictogramas a ser retornado pelo banco de dados
    tamanho_lista_retornada = 0  # real tamanho da lista retornada, que serve para lidar com o caso de nao termos pictogramas suficientes para retornar 10 filtrados por topicos
    lista_pictogramas = []  # lista retornada pelo banco de dados
    lista_randomica = []  # lista que guardara a amostragem feita em lista_pictogramas

    if topicos is None:
        for pictograma in mongo.db.pictogramas.find():
            lista_pictogramas.append(pictograma)
    elif type(topicos) is list:
        for pictograma in mongo.db.pictogramas.find({"topicos": {"$in": topicos}}):
            lista_pictogramas.append(pictograma)
    else:
        raise ArgumentoInvalido("Topicos nao foram passados em formato de lista!")

    tamanho_lista_retornada = len(lista_pictogramas)
    if (
        tamanho_lista_retornada < tamanho):  # se tamanho_lista_retornada for 0, sera retornado uma lista vazia de pictogramas
        tamanho = tamanho_lista_retornada

    lista_randomica = sample(lista_pictogramas, tamanho)
    for index in range(tamanho):
        lista_randomica[index] = criar_objeto_de_json(lista_randomica[index])

    return lista_randomica


def pictograma_id(_id):
    return criar_objeto_de_json(mongo.db.pictogramas.find_one({"_id": ObjectId(_id)}))


def remove_pictograma(_id):
    return mongo.db.pictogramas.remove({"_id": ObjectId(_id)})


def checar_json_pictograma_valido(picto_json):
    print picto_json
    if 'imagem' not in picto_json:
        raise JSONInvalido("campo imagem nao foi definido no json")
    if 'dica' not in picto_json:
        raise JSONInvalido("campo dica nao foi definido no json")
    if 'resposta' not in picto_json:
        raise JSONInvalido("campo resposta nao foi definido no json")
    if 'topicos' not in picto_json:
        raise JSONInvalido("campo topicos nao foi definido no json")
    if len(picto_json['topicos']) < 1:
        raise JSONInvalido("Campo topicos foi definido, mas nao ha nenhum topico")

    return True


def inserir_pictograma(pict_json):
    id_insertions = []
    if type(pict_json) == dict:
        if checar_json_pictograma_valido(pict_json):
            id_insertions.append(str(mongo.db.pictogramas.insert_one(pict_json).inserted_id))

    elif type(pict_json) == list:
        for obj in pict_json:
            if checar_json_pictograma_valido(obj):
                id_insertions.append(str(mongo.db.pictogramas.insert_one(obj).inserted_id))

    else:
        raise JSONInvalido("The json informed is not valid!")

    return id_insertions


class JSONInvalido(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)


class ArgumentoInvalido(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)
