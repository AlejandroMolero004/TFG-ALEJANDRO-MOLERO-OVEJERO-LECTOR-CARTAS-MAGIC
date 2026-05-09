from fastapi import HTTPException

from fastapi import FastAPI, Request
from foto import foto
#  python -m uvicorn API.server:app --reload --port 8001
app = FastAPI()


@app.post("/escanear_carta")
def escanear_carta():
   resultado = foto()
   print("Resultado:", resultado)
   if resultado is None:
        raise HTTPException(
            status_code=500,
            detail="No se pudo escanear la carta"
        )

   return {"message": "Carta escaneada", "resultado": resultado}