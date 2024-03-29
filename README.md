## Introducao

Este e o projeto a ser desenvolvido pelo grupo #1 de engenharia de software da UFMG. A equipe foi dividida em tres
setores do desenvolvimento. Pontas frontais e traseiras (backend e frontend do ingles), e equipe de burocracia
avaliacional.

## PicToSoft
**PicToSoft** e um software inspirado no jogo disponivel para a plataforma mobile PicToWord, em que sao apresentadas
imagens ao usuario, e ele deve descobrir a logica por tras das imagens e descobrir qual e a palavra secreta.
O projeto no entanto diverge nas fundacoes basicas, onde nosso principal objetivo e ensinar os usuarios alguns conceitos
de engenharia de software. O metodo escolhido para tal e o de repeticao espacada. O usuario nao tem a necessidade de ter
um conhecimento previo em engenharia de software, e esperamos que ao final de uma partida ele possa estar mais
familiarizado com conceitos basicos de engenharia de software.

## Dependencias

Sao necessarios para o funcionamento da aplicacao as seguintes ferramentas e estacoes de trabalho:
* [Python 2.7](http://www.python.org)
* [MongoDB 3+](http://www.mongodb.org)
* [Django 1.8+](https://www.djangoproject.com/)
* PyMongo
* [Node.js](https://nodejs.org/)

## Instalando todas as dependencias

###### Linux
* Python

⋅⋅⋅ Com o linux, o python 2.7 geralmente ja vem disponivel com o sistema.

* MongoDB

⋅⋅⋅ Um modo facil de instalar o MongoDB, utilizar os seguintes comandos:
```
cd ~
wget https://fastdl.mongodb.org/linux/mongodb-linux-x86_64-ubuntu1404-3.2.5.tgz
tar -xf mongodb-linux-x86_64-ubuntu1404-3.2.5.tgz -C mongoDB
sudo mkdir /data/db
cd ~/mongoDB/bin
sudo ./mongod
```
Sempre que for necessario iniciar o servico do mongoDB novamente, basta apenas rodar os dois ultimos comandos.
O mongoDB inicia automatica e escuta por requisicoes na porta 27017 por padrao. Logo, um jeito facil de testar se tudo
funcionou, e acessar a pagina [http://localhost:27017/](http://localhost:27017/), se aparecer a seguinte mensagem:

``` It looks like you are trying to access MongoDB over HTTP on the native driver port. ```
Pode ter certeza que ate entao tudo esta OK!

* Django
Existem dois jeitos MUITO faceis de se instalar o Django.
O primeiro, e utilizar a IDE PyCharm, e criar um novo projeto Django. A primeira parte da criacao desse projeto, a IDE
baixa automaticamente e instala o Django para voce!

O segundo jeito e o mais recomendado e utilizando o pip. Para obter o pip no linux com aptitude, basta digitar no
terminal `sudo apt-get install -y python-pip` e depois `sudo -H pip install pip --upgrade`
Apos instalado o pip, para instalar o Django, use o comando `sudo -H pip install django`

* PyMongo
Este e o motivo de eu ter recomendado instalar o pip no passo anterior, o PyMongo o jeito mais facil de ser instalado e
pelo pip, com o comando `sudo -H pip install pymongo

* Node.js
Node esta disponivel nos gerenciadores de pacotes da maioria das distribuições. O site do Node.js mostra os comandos necessários para a instalação para varias distribuições https://nodejs.org/en/download/package-manager/. Encontre sua distribuição e digite os comandos no terminal. `


###### Windows
```TO-DO: Quem resolver instalar tudo em windows, por favor, completar esta parte :)```

## Rodando a aplicacao

Para rodar o backend, uma vez instalada todas as dependencias, no diretorio principal da nossa aplicacao existe o
diretorio backend, ao entrar neste diretorio, voce pode iniciar a aplicacao rodando o seguinte comando:
`python manage.py runserver`
Nao feche esta janela do terminal, o servidor esta rodando! provavelmente voce deve ter recebido uma mensagem assim:

```
Performing system checks...

System check identified no issues (0 silenced).
April 15, 2016 - 01:18:54
Django version 1.9.5, using settings 'micro_servicos.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
```

Ao acessar a pagina [http://127.0.0.1:8000/](http://127.0.0.1:8000/) voce deveria ver uma mensagem de HelloWorld.
Ao acessar a pagina [http://127.0.0.1:8000/mongodb/](http://127.0.0.1:8000/mongodb/) voce deve ver uma mensagem da sua
versao do PyMongo, a versao do seu mongoDB e os dizeres de que a conexao foi bem sucedida. Se isto tudo acontecer
otimo! tudo esta funcionando. `woo-hoo`

Para rodar frontend primeiro é necessário instalar as dependecias do projetos. As dependencias devem ser baixadas apenas uma vez para o frontend funcionar sempre. Nossa dependencias são gerenciadas com o pacote `npm` instalado com o Node.js. Basta navegar para a raiz do diretório do frontend e digitar o comando `npm install`. O npm irá instalar as ferramentas bower e gulp. Bower é usado para gerencias as bibliotecas javascript e gulp para compilar os arquivos less para css. Use o comando `bower install` para instalar as bibliotecas javascript e o comando `gulp`para compilar os arquivos less. Como o frontend esta separado do backend, basta abrir os arquivos html diretamente, não é necessário um servidor.

## Entidades da aplicacao

Ainda nao definimos quais serao as entidades da aplicacao, mas apos uma boa discussao e gracas a sugestao fantastica do
matheus, acredito que nossa entidade principal deva se chamar pictograma! O usuario sera mostrado pictogramas e devera
responder qual a entidade de engenharia de software correspondente.

Espero que esse mock mude com o tempo, mas poderiamos usar algo no seguinte formato:

```javascript
var jsonMock = {
    'pictogramas': [
        {
            'imagem': 'images/pic001.png',
            'dica': 'Um dos 17 do Manifesto Agil',
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
                {'nome': 'projeto'},
                {'nome': 'processo'},
                {'nome': 'teste'}
            ]
        },
        {...} //mais pictogramas
    ]
}
```

## Tests

`TODO: definir testes existentes, por que eles existem, e como roda-los`

## Equipe

Equipe top do Grupo#1

* Sergio H B Marques
* Lucas C Souza
* Inácio Cerqueira
* Renato Oliveira
* Eric Torres
* Guilherme Ferreira
* Ivan Fernandes
* Lucas Pereira
* Mateus Aroeira
* Tadeu R S R Barbosa


