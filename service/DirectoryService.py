# Python program to explain os.mkdir() method

# importing os module
import os
import uuid

from document_deploy.models import Directory
from service import Constant


class DirectoryService:
    @staticmethod
    def getDirectoryList():
        print(os.listdir(path=Constant.PARENT_DIR))
        return os.listdir(path=Constant.PARENT_DIR)

    @staticmethod
    def create(dirName):
        list = DirectoryService.getDirectoryList()

        if not list.__contains__(dirName):
            try:
                os.mkdir(Constant.PARENT_DIR + "/" + dirName)
                print("Directory '%s' created" % dirName)

                directoryCode = str(uuid.uuid4())
                directory = Directory(code=directoryCode, name=dirName)
                directory.save()
                return directoryCode

            except (Exception) as error:
                print("Failed to select record from table", error)
            return False

        else:
            return False
