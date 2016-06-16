import json
from datetime import datetime

import bson
from bson.objectid import ObjectId

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
    partida_objid = metricas_partida.insert_one(json_obj).inserted_id

    # {"projeto": {}, "processo": {}, "praticas": {}, "entidades": {}}

    metricas_topico = {"projeto": mongo.db.metricas_topico_projeto, "processo": mongo.db.metricas_topico_processo,
                       "praticas": mongo.db.metricas_topico_praticas, "entidades": mongo.db.metricas_topico_entidades}
    metricas = {
        "projeto": {
            "id": 0,
            "acertos": 0,
            "erros": 0
        },
        "processo": {
            "id": 0,
            "acertos": 0,
            "erros": 0
        },
        "praticas": {
            "id": 0,
            "acertos": 0,
            "erros": 0
        },
        "entidades": {
            "id": 0,
            "acertos": 0,
            "erros": 0
        }
    }

    new_metrics = []

    for topico in metricas:
        count = metricas_topico[topico].find().count()
        if count != 0:
            metricas[topico] = metricas_topico[topico].find_one({"id": count})
            del (metricas[topico]["_id"])

    for resposta in json_obj["respostas"]:
        picto = mongo.db.pictogramas.find_one({"_id": ObjectId(resposta["id"])})
        for topico in picto["topicos"]:
            if topico not in new_metrics:
                new_metrics.append(topico)

            assert topico in metricas_topico  # se nao, temos um pictograma invalido
            if resposta["acertou"]:
                metricas[topico]["acertos"] += 1
            else:
                metricas[topico]["erros"] += 1

    for topico in new_metrics:
        metricas[topico]["id"] += 1
        metricas_topico[topico].insert_one(metricas[topico])


def pegar_metricas_ultimas_partidas():
    metricas = mongo.db.metricas_partida
    return metricas.find({}).sort("date", -1).limit(10)


def pegar_metricas_ultimos_topicos():
    metricas_topico = {"projeto": mongo.db.metricas_topico_projeto, "processo": mongo.db.metricas_topico_processo,
                       "praticas": mongo.db.metricas_topico_praticas, "entidades": mongo.db.metricas_topico_entidades}

    return_dic = {}

    for topico in metricas_topico:
        return_dic[topico] = []
        for metricas_de_topico in metricas_topico[topico].find({}).sort("id", -1).limit(10):
            acertos = metricas_de_topico["acertos"]
            erros = metricas_de_topico["erros"]
            total = acertos + erros
            avg = float(acertos) / total

            return_dic[topico].append({"x": metricas_de_topico["id"], "y": avg})

    return return_dic
