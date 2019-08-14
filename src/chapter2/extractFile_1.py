import os
import tarfile
from six.moves import urllib

def unzip_files(fileDirectory, fileleName):
    if not os.path.isdir(fileDirectory):
        return "directory doesnt exist"
    targetFile = os.path.join(fileDirectory,fileleName)
    fileDirToBeExtracted = os.path.join(fileDirectory, "newFile")
    fileOpen = tarfile.open(targetFile)
    fileOpen.extractall(path=fileDirToBeExtracted)
    fileOpen.close()
    return "success"


print(unzip_files("C:\workspace\HandsOnBook\dataset\housing","housing.tgz"))