from django.test import TestCase, Client
from django.conf import settings
from json import loads


class TestUrls(TestCase):
    def test_object_was_set_correctly(self):
        res = loads(Client().get('/pictograms').content)

        self.assertTrue('pictogramas' in res)

        res = res['pictogramas'][0]

        self.assertTrue('imagem' in res)
        self.assertTrue('dica' in res)
        self.assertTrue('resposta' in res)
        self.assertTrue('letras' in res)
        self.assertTrue('tempo' in res)
        self.assertTrue('topicos' in res)

        for topics in res['topicos']:
            self.assertTrue('nome' in topics)

    def test_letras_field_has_all_letters(self):
        res = loads(Client().get('/pictograms').content)['pictogramas'][0]

        word = res['resposta'].replace(' ', '')

        for letter in res['letras']:
            word = word.replace(letter, '', 1)

        self.assertEqual(len(word), 0)

if __name__ == '__main__':
    settings.configure()
