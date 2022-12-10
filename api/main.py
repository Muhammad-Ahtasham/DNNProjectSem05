from fastapi import FastAPI, UploadFile, File
import uvicorn
import numpy as np
from io import BytesIO

app = FastAPI()
@app.get("/ping")
async def ping():
    return "hello i am alive"

@app.post("/predict")

def read_file_as_image(data)-> np.ndarray:

async def predict(
    file: UploadFile = File(...)
):
    bytes = await file.read()

if __name__ == "__main__":
    uvicorn.run(app, host='localhost', port=8000)