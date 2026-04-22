from fastapi import FastAPI
from app.models.request_model import QueryRequest
from app.agent import process_query

app = FastAPI()

@app.get("/")
def home():
    return {"message": "AI Cognitive Agent Running 🚀"}

@app.post("/ask")
async def ask(req: QueryRequest):
    response = await process_query(req.query)
    return {"response": response}