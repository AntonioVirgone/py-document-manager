import uuid

from document_deploy.models import Document
from service import CreateDocumentService
from service.DataDocument import DataDocument

from django.core import serializers


def jsonSerializer(articles):
    return serializers.serialize("json", articles)


class DocumentService:

    @staticmethod
    def create(data):
        dataDocument = DataDocument.fromJson(data)

        document = Document(code=str(uuid.uuid4()), name=dataDocument.fileName, root=dataDocument.directoryName)
        document.save()

        CreateDocumentService.createDocument(dataDocument)

    @staticmethod
    def findByCode(documentCode):
        return Document.objects.get(code=documentCode)

    @staticmethod
    def findInRoot(root):
        articles = Document.objects.all().filter(root=root)
        return jsonSerializer(articles)

