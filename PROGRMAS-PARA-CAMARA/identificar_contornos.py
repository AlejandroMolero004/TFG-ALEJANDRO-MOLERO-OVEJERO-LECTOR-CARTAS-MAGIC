import numpy as np
import cv2

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
# Cargamos la imagen
original = cv2.imread("foto2.jpg")


# Convertimos a escala de grises
gris = cv2.cvtColor(original, cv2.COLOR_BGR2GRAY)
 
# Aplicar suavizado Gaussiano
gauss = cv2.GaussianBlur(gris, (19,19), 0)
 


# Detectamos los bordes con Canny
canny = cv2.Canny(gauss, 80, 80)
 


# Buscamos los contornos
(contornos,_) = cv2.findContours(canny.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Mostramos el número de monedas por consola
print("He encontrado {} objetos".format(len(contornos)))
contornos_ordenados = sorted(contornos, key=cv2.contourArea, reverse=True)
print (len(contornos_ordenados))
area_max = 0
contorno_maximo =  contornos_ordenados[0]


cv2.drawContours(original, [contorno_maximo], -1, (0, 255, 0), 2)     
cv2.imwrite("foto_con_contornos_maximo.jpg", original)
cv2.drawContours(original, contornos_ordenados, -1, (0, 255, 0), 2)
cv2.imwrite("foto_con_contornos.jpg", original)

