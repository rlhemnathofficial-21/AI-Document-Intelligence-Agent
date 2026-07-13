from fastapi import FastAPI
from api.routes import router

app = FastAPI(
    title="AI Document Intelligence Agent",
    description="Agent-Based OCR + LLM Invoice Extraction",
    version="1.0"
)

app.include_router(router)


@app.get("/")
def home():

    return {
        "message": "AI Document Intelligence Agent Running Successfully"
    }