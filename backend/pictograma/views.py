from django.http import HttpResponse
from json import dumps


def get_random_pictogram(request):
    data = {
        'pictogramas': [{
            'imagem': 'images/pic001.png',
            'dica': 'Quem descobriu brasil?',
            'resposta': 'KENT BECK',
            'letras': [
                'K',
                'E',
                'N',
                'T',
                'B',
                'E',
                'C',
                'K',
                'J',
                'I',
                'N',
                'C',
                'A'
            ],
            'tempo': 30,
            'topicos': [
                {'nome': 'uml'},
                {'nome': 'figuras excentricas'},
                {'nome': 'Impeachment Dilma Roussef'}
            ]
        }]
    }

    return HttpResponse(dumps(data), content_type='application/json')
