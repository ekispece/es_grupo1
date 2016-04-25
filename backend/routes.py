from flask.globals import request
from flask.helpers import make_response
from flask.wrappers import Response

from pictograma.Pictograma import pictograma_aleatorio, pictograma_id, pictograma_resposta
from pictograma.Pictograma import inserir_pictograma
from app import app


#  Define as rotas para o endpoint pictograma
@app.route("/pictograma", methods=["GET", "POST"])
def pictograma():
    if request.method == "POST":
        inserir_pictograma(request.get_json(force=True))
        return make_response("Ok", 200)
    elif request.method == "GET":
        picto = pictograma_aleatorio()
        response = Response(response=picto.get_as_json(), status=200, mimetype="application/json")
        return response


@app.route("/pictograma/<string:_id>")
def pictograma_por_id(_id):
    picto = pictograma_id(_id)
    response = Response(response=picto.get_as_json(), status=200, mimetype="application/json")
    return response


@app.route("/pictograma/a/<string:resposta>")
def pictograma_por_resposta(resposta):
    picto = pictograma_resposta(resposta)
    response = Response(response=picto.get_as_json(), status=200, mimetype="application/json")
    return response


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9999, debug=True)
