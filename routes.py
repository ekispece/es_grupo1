import json
import ast
from flask import json
from flask.globals import request
from flask.wrappers import Response

from bson import json_util

from metricas import metricas
from pictograma.Pictograma import buscar_pictogramas, pictograma_id, remove_pictograma, inserir_pictograma, \
    get_list_as_json
from app import app
from crossdomain import crossdomain


#  Rotas do website
@app.route("/")
@crossdomain(origin='*')
def root():
    return app.send_static_file("index.html")


#  Define as rotas para o endpoint pictograma
@app.route("/pictograma", methods=["GET", "POST"])
@crossdomain(origin='*')
def pictograma():
    if request.method == "POST":
        ids = inserir_pictograma(request.get_json(force=True))
        return Response(response=json.dumps({'inseridos': ids}), status=200, mimetype="application/json")
    elif request.method == "GET":
        if len(request.args.getlist('topicos')) is 0:
            picto = buscar_pictogramas(None)
        else:
            lista = ast.literal_eval(str(request.args.getlist('topicos')))
            picto = buscar_pictogramas(lista)
        response = Response(response=get_list_as_json(picto), status=200, mimetype="application/json")
        return response


@app.route("/pictograma/<string:_id>", methods=["GET", "DELETE"])
@crossdomain(origin='*')
def pictograma_por_id(_id):
    if request.method == "GET":
        picto = pictograma_id(_id)
        response = Response(response=picto.get_as_json(), status=200, mimetype="application/json")
        return response
    elif request.method == "DELETE":
        return Response(response=remove_pictograma(_id), status=200, mimetype="application/json")


@app.route("/finaliza", methods=["POST"])
@crossdomain(origin="*")
def finaliza_jogo_e_mostra_metricas():
    json_dic = request.get_json(force=True)
    assert json_dic is not None
    assert metricas.json_valido(json_dic)
    metricas.salvar_jogo(json_dic)
    partidas = metricas.pegar_metricas_ultimas_partidas()
    return_json = {"partidas": []}
    for i, partida in enumerate(partidas):
        respostas_corretas = 0
        for resposta in partida["respostas"]:
            if resposta["acertou"]:
                respostas_corretas += 1
        return_json["partidas"].append({"x": i, "y": respostas_corretas})

    return_json["topicos"] = {"projeto": {}, "processo": {}, "praticas": {}, "entidades": {}}
    for key in return_json["topicos"]:
        print key
    return Response(response=json_util.dumps(return_json))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
