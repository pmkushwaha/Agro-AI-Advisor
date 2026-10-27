from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="Agri AI Advisor",
    description="AI-powered agricultural advisory API",
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {
        "message": "Agri AI Advisor API is running",
        "status": "success",
    }

@app.get("/health")
def health():
    return {"status": "healthy"}

