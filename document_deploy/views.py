import json

from django.http import HttpResponse
from rest_framework.decorators import api_view

from service.DirectoryService import DirectoryService
from service.DocumentService import DocumentService
from service.model.DirectoryViewModel import DirectoryViewModel, DirectoryViewModelEncoder


def index(request):
    documentCode = request.GET.get("documentCode")
    document = DocumentService.findInRoot(documentCode)

    print("document type is " + str(type(document)))

    return HttpResponse(document)


@api_view(['POST'])
def createDirectory(request):
    dirName = request.GET.get("dirName")
    code = DirectoryService.create(dirName)

    if code:
        json_str = json.dumps(DirectoryViewModel(directoryCode=code, directoryName=dirName), cls=DirectoryViewModelEncoder)

        print(json_str)
        return HttpResponse(
            json_str,
            content_type="application/json")
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


def findAllDirectory(request):
    print("ciao")
    list = DirectoryService.getDirectoryList()
    return HttpResponse(json.dumps(list), content_type="application/json")
