import json
from flask.globals import request
from flask.wrappers import Response

from pictograma.Pictograma import pictograma_aleatorio, pictograma_id, remove_pictograma, inserir_pictograma
from app import app


#  Rotas do website
@app.route("/")
def root():
    return app.send_static_file("index.html")


#  Define as rotas para o endpoint pictograma
@app.route("/pictograma", methods=["GET", "POST"])
def pictograma():
    if request.method == "POST":
        ids = inserir_pictograma(request.get_json(force=True))
        return Response(response=json.dumps({'inseridos': ids}), status=200, mimetype="application/json")
    elif request.method == "GET":
        picto = pictograma_aleatorio()
        response = Response(response=picto.get_as_json(), status=200, mimetype="application/json")
        return response


@app.route("/pictograma/<string:_id>", methods=["GET", "DELETE"])
def pictograma_por_id(_id):
    if request.method == "GET":
        picto = pictograma_id(_id)
        response = Response(response=picto.get_as_json(), status=200, mimetype="application/json")
        return response
    elif request.method == "DELETE":
        return Response(response=remove_pictograma(_id), status=200, mimetype="application/json")


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
