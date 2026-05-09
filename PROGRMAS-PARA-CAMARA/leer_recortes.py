import re
import cv2
import pytesseract
import requests
from buscar_recomendaciones import autocompletar_recomendaciones 

def leer_recortes():
    nombre_carta = ""
    img = cv2.imread("nombre.jpg")

    # Pasar a gris
    gris = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Identificar foil

    # Mejorar imagen
    gris = cv2.resize(gris, None, fx=2, fy=2)
    _, binaria = cv2.threshold(gris, 150, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    # OCR
    # psm = Page Segmentation Mode cómo está organizado el texto en la imagen  6 = una sola línea de texto
    whitelist = "abcdefghijklmnñopqrstuvwxyzABCDEFGHIJKLMNÑOPQRSTUVWXYZ'., "
    config = f'--psm 6 -c tessedit_char_whitelist="{whitelist}"'

    nombre = pytesseract.image_to_string(binaria, lang="spa+eng",                                        
    config = config
    ) 

    data = pytesseract.image_to_data(binaria, output_type=pytesseract.Output.DICT)
    print (data)

    print("--------------------------------------------------")
    for i in range(len(data['text'])):
        print(f"Texto: {data['text'][i]})")
        if data['text'][i] != "" and data['conf'][i] > 60:  
            nombre_carta += data['text'][i] + " "
    print ("--------------------------------------------------")
    print("Nombre OCR: " + nombre_carta)
    print("--------------------------------------------------")
    cv2.imwrite("nombre_binaria.jpg", binaria)
    
    

    img = cv2.imread("tipo.jpg")

    # Pasar a gris
    gris = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Mejorar imagen
    gris = cv2.resize(gris, None, fx=2, fy=2)
    _, binaria = cv2.threshold(gris, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    # OCR
    tipo = pytesseract.image_to_string(binaria, lang="eng")  # o "spa"

   
    ## print(tipo)
    
    print("Nombre: " + nombre)
    print("--------------------------------------------------")
    print("Tipo: " + tipo)
    print("--------------------------------------------------")
    nombre_limpio = re.sub(r"[\[\]/\*`´^{}()]", " ", nombre).replace("-", " ").replace("\n", " ")
    tipo_limpio = re.sub(r"[\[\]/\*`´^{}()]", " ", tipo).replace("\n", " ")
   
    print("Nombre limpio: " + nombre_carta)
    print("--------------------------------------------------")
    print("Tipo limpio: " + tipo_limpio)
    if not nombre or not tipo:
        print("No se pudo leer el nombre o tipo de la carta.")
        return
    
 # cards = Card.where(types=tipo_limpio,name=nombre_limpio).all()
 # for carta in cards:
 #     print("Carta encontrada:")
 #     print(carta.name, carta.type, carta.mana_cost, carta.text)
    
    url = "https://api.scryfall.com/cards/named"
    response = requests.get(url, params={"fuzzy": nombre_carta})
    if response.status_code == 200:
        print(response.status_code)
        data =  response.json()
        print(data)
        print("RECOMENDACIONES DE CARTAS:")
    
        #print(data.get("name"), data.get("type_line"), data.get("mana_cost"), data.get("oracle_text") ,data.get("prices") , data.get("purchase_uris",{}).get("cardmarket"))
        #return data
        #response = requests.get(data.get("purchase_uris",{}).get("cardmarket"))
        #if response.status_code == 200:
        #    data = response
        #    print("Precio en Cardmarket:")
        #    print(data)
    #else:
        
        recomendaciones = autocompletar_recomendaciones(nombre_carta)
        print(recomendaciones)
        
        return {"carta": data, "recomendaciones": recomendaciones}
        #print ("****************DATA*****************")
        #print(data)
        #print ("***************FIN DATA*****************")
        #print("*******RECOMENDACIONES DE CARTAS*********")
        #print(recomendaciones)
        #print("******************************************")
       
       

       
