import json
import re
from random import randint

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

        self.pict_json = {
            '_id': self._id,
            'imagem': self.imagem,
            'dica': self.dica,
            'resposta': self.resposta,
            'topicos': self.topicos

        }


    def __str__(self):
        return "Pictograma [ \'imagem\': " + self.imagem + ", \'dica\': " + self.dica + ", \'resposta\': " + \
               self.resposta + ", \'topicos_len\': " + str(len(self.topicos)) + "]"


    def get_as_json(self):
        return json.dumps(self.pict_json)


def criar_objeto_de_json(pict_json):
    return Pictograma(imagem=pict_json['imagem'], dica=pict_json['dica'], resposta=pict_json['resposta'],
                      topicos=pict_json['topicos'], _id=str(pict_json['_id']))


def pictograma_aleatorio():
    skip = randint(0, mongo.db.pictogramas.find().count() - 1)
    return criar_objeto_de_json(mongo.db.pictogramas.find().skip(skip).next())


def pictograma_resposta(resposta):
    return criar_objeto_de_json(
        mongo.db.pictogramas.find_one({"resposta": re.compile('^' + re.escape(resposta) + '$', re.IGNORECASE)}))


def pictograma_id(_id):
    return criar_objeto_de_json(mongo.db.pictogramas.find_one({"_id": ObjectId(_id)}))


def inserir_pictograma(pict_json):
    if type(pict_json) == dict:
        mongo.db.pictogramas.insert_one(pict_json)

    elif type(pict_json) == list:
        for obj in pict_json:
            mongo.db.pictogramas.insert_one(obj)

    else:
        raise TypeError("The json informed is not valid!")
