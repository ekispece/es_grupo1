import json
from datetime import datetime

import bson

from app import mongo


def json_valido(json_obj):
    assert "respostas" in json_obj
    for resposta in json_obj["respostas"]:
        assert "id" in resposta
        assert "acertou" in resposta
    return True


def salvar_jogo(json_obj):
    metricas_partida = mongo.db.metricas_partida
    json_obj["date"] = datetime.now()
    metricas_partida.insert_one(json_obj)

    metricas_topico = mongo.db.metricas_topico





def pegar_metricas_ultimas_partidas():
    metricas = mongo.db.metricas_partida
    return metricas.find({}).sort("date", -1).limit(10)
