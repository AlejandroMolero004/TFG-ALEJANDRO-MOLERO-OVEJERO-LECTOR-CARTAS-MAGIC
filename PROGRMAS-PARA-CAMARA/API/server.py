from fastapi import FastAPI, Request
from foto import foto
#  python -m uvicorn API.server:app --reload --port 8001
app = FastAPI()
@app.get("/")
def home():
    return {"message": "¡Hola, mundo!"}

@app.get("/escanear_carta")
def escanear_carta():
   resultado = foto()
   print("Resultado:", resultado)
   return {"message": "Carta escaneada", "resultado": resultado}