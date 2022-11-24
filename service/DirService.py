# Python program to explain os.mkdir() method

# importing os module
import os
import uuid

from document_deploy.models import Directory
from service import Constant


class DirService:

    @staticmethod
    def create(dirName):
        # Path
        path = os.path.join(Constant.PARENT_DIR, dirName)

        isExist = os.path.exists(path)
        print("directory '/{}' exist: {}".format(dirName, isExist))

        if not isExist:
            try:
                os.mkdir(path)
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

