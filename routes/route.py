# routes/route.py
from fastapi import APIRouter,File, UploadFile
from controller import compile, worker

router = APIRouter()

@router.post("/submit")
async def mainRoute(file: UploadFile):
    # recieve the file from Form Data in fastapi
    ext = await worker.getFileExtension(file)  # run the getFileExtension function from controller/worker.py
    worker.saveFile(file, ext)  # run the saveFile function from controller/worker.py
    
    result = []

    # select the correct compiler
    if ext == "py":
        result = compile.compilePython(file.filename)  # run the compilePython function from controller/compile.py
    else:
        result = {"error": "File type not supported"}
    
    # delete the file after the process is done
    worker.deleteFile(file.filename)  # run the deleteFile function from controller/worker.py
    return result
