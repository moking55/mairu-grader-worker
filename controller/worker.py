# save uploaded file to submission folder
import os

async def getFileExtension(file):
    # get the file extension from the file name
    fileExtension = file.filename.split(".")[1]
    return fileExtension

def saveFile(file, extension):
    # generate a random 8 character string
    newFileName = os.urandom(8).hex()
    # change file name to random 8 character string
    file.filename = f"{newFileName}.{extension}"

    # save the file to the submissions folder
    with open(f"{os.getcwd()}/submission/{file.filename}", "wb") as buffer:
        buffer.write(file.file.read())
    return file.filename

def deleteFile(filename):
    # delete the file from the submissions folder
    os.remove(f"{os.getcwd()}/submission/{filename}")
    return True