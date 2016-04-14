import pymongo as mongo
from django.http.response import HttpResponse


def print_version(request):
    response = 'You seem to be using pyMongo ' + str(mongo.version)
    mongo_client = mongo.MongoClient('127.0.0.1:27017')  # this should be the default install location
    response += '<br /><br />MongoDB connected successfully.<br /><br />MongoDB v' + str(mongo_client.server_info()['version'])
    return HttpResponse(response)
