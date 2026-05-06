import cv2
from recorte import recortar_imagen
from elegir_parte_cuadricula import elegir_parte_cuadricula
from leer_recortes import leer_recortes

def foto():
    cap = cv2.VideoCapture(0)
    cap.set(cv2.CAP_PROP_BRIGHTNESS, 200)   # brillo
    cap.set(cv2.CAP_PROP_CONTRAST, 50)      # contraste
    cap.set(cv2.CAP_PROP_SATURATION, 50)    # color
    cap.set(cv2.CAP_PROP_EXPOSURE, -4)      # exposición (clave)
    if not cap.isOpened():
        print("No se pudo abrir la cámara")
        exit()

    ret, frame = cap.read()

    if ret:
        cv2.imwrite("foto2.jpg", frame)
        print("Foto guardada")
    else:
        print("Error al capturar")

    cap.release()

    recortar_imagen()
    elegir_parte_cuadricula()
    data = leer_recortes() 
    print("************************FUNCION FOTO****************")
    print (data)
    print("****************************************************")
    return data
    

