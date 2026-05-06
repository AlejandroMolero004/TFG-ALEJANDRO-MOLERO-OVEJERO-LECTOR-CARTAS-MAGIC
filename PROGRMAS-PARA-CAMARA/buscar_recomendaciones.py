import requests


def autocompletar_recomendaciones(nombre_ocr):
    recomendaciones = []
    cartas_recomendadas = []
    #url = "https://api.scryfall.com/cards/autocomplete?q="+nombre_ocr
    url = "https://api.scryfall.com/cards/autocomplete?q="+nombre_ocr
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        recomendaciones = data.get("data", [])
          
    else:
        print("Error al obtener recomendaciones de cartas.")

    

    url = "https://api.scryfall.com/cards/collection"
    response = requests.post(url, json={"identifiers": [{"name": rec} for rec in recomendaciones]})
    if response.status_code == 200:
        data = response.json()
        cartas_recomendadas = data.get("data", [])
       
   #     print (cartas_recomendadas)
        

    return cartas_recomendadas

