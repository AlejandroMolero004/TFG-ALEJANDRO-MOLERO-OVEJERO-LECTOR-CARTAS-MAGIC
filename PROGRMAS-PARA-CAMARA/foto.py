import cv2
from recorte import recortar_imagen
from elegir_parte_cuadricula import elegir_parte_cuadricula
from leer_recortes import leer_recortes
import time

def foto():
    #------- HACER LA FOTO -----------------------------------------
    t_inicial_capturar_imagen = time.perf_counter()

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

    t_capturar_imagen = time.perf_counter() - t_inicial_capturar_imagen
    print(f"-----------------------------------------------------------")
    print(f"TIEMPO REALIZAR FOTO : {t_capturar_imagen*1000:1f} ms") 
    print(f"-----------------------------------------------------------")

    t_inicial_recortar_imagen = time.perf_counter()
    recortar_imagen()
    t_recortar_imagen = time.perf_counter() - t_inicial_recortar_imagen
    print(f"-----------------------------------------------------------")
    print(f"TIEMPO RECORTAR FOTO : {t_recortar_imagen*1000:1f} ms") 
    print(f"-----------------------------------------------------------")

    t_inicial_elegir_parte_cuadricula = time.perf_counter()
    elegir_parte_cuadricula()
    t_elegir_parte_cuadricula = time.perf_counter() - t_inicial_elegir_parte_cuadricula
    print(f"-----------------------------------------------------------")
    print(f"TIEMPO ELEGIR PARTE DE LA FOTO : {t_elegir_parte_cuadricula*1000:1f} ms") 
    print(f"-----------------------------------------------------------")

    
    data = leer_recortes() 
    
    return data
    

