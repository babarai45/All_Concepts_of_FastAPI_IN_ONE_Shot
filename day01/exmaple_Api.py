# main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# CORS allow karo taake Svelte frontend se call ho sake
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # production mein sirf apna domain daalna
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/hello")
def hello_world():
    return {"message": "Hello World from FastAPI!"}