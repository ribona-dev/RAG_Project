import os
import shutil
from fastapi import FastAPI, UploadFile, File, Form
from fastapi.middleware.cors import CORSMiddleware
from rag_engine import RAGAssistant

app = FastAPI(title="Document Assistant")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

assistant = RAGAssistant()
upload_folder = "./temp_uploads"
os.makedirs(upload_folder, exist_ok=True)

@app.post("/upload")
async def upload_document(file: UploadFile = File(...)):
    file_path = os.path.join(upload_folder, file.filename)
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    
    status_message = assistant.process_file(file_path)
    return {"message": status_message}

@app.post("/ask")
async def ask_question(question: str = Form(...)):
    answer_text = assistant.ask_question(question)
    return {"answer": answer_text}