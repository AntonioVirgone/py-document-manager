import json

from django.http import HttpResponse
from rest_framework.decorators import api_view

from service.DirService import DirService
from service.DocumentService import DocumentService


def index(request):
    documentCode = request.GET.get("documentCode")
    document = DocumentService.findInRoot(documentCode)

    print("document type is " + str(type(document)))

    return HttpResponse(document)


@api_view(['POST'])
def createDirectory(request):
    dirName = request.GET.get("dirName")

    if DirService.create(dirName):
        return HttpResponse("Creazione cartella %s completata" % dirName)
    else:
        return HttpResponse("Creazione cartella %s fallita" % dirName)


@api_view(['POST'])
def createDocument(request):
    data = request.data
    if request.method == "POST":
        DocumentService.create(data['dataDocument'])
        return HttpResponse("Creazione documento completato")
    else:
        return HttpResponse("Errore durante la creazione del documento")



# def downloadDocument(filename, directory):
#     return send_file(path_or_file=directory + "/" + filename,
#                      mimetype="application/octet-stream",
#                      as_attachment=True,
#                      download_name=filename)