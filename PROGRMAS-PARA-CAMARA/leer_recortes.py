import cv2
import pytesseract
from mtgsdk import Card
import requests

def leer_recortes():

    img = cv2.imread("nombre.jpg")

    # Pasar a gris
    gris = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Mejorar imagen
    gris = cv2.resize(gris, None, fx=2, fy=2)
    _, binaria = cv2.threshold(gris, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    # OCR
    nombre = pytesseract.image_to_string(binaria, lang="eng")  # o "spa"

    

    img = cv2.imread("tipo.jpg")

    # Pasar a gris
    gris = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Mejorar imagen
    gris = cv2.resize(gris, None, fx=2, fy=2)
    _, binaria = cv2.threshold(gris, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    # OCR
    tipo = pytesseract.image_to_string(binaria, lang="eng")  # o "spa"

   
    ## print(tipo)
   
    print(nombre)
    print("--------------------------------------------------")
    print(tipo)
    cards = Card.where(types='creature',name="Prismabasher").all()
    for carta in cards:
        print("Carta encontrada:")
        print(carta.name, carta.type, carta.mana_cost, carta.text)

    url = "https://api.scryfall.com/cards/named?fuzzy=" + nombre[2:16]
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        print("Carta encontrada SCRYFALL:")
        print(data.get("name"), data.get("type_line"), data.get("mana_cost"), data.get("oracle_text"))
    else:
        print("Carta no encontrada en Scryfall.")