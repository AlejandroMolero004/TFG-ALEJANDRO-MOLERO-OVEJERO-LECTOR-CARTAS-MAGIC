import cv2
def recortar_imagen():

    img = cv2.imread("foto2.jpg")

    if img is None:
        print("No se pudo cargar la imagen")
        exit()

    h, w = img.shape[:2]

    # Número de divisiones
    filas = 40
    columnas = 40

    # Dibujar líneas verticales
    for i in range(1, columnas):
        x = i * w // columnas
        cv2.line(img, (x, 0), (x, h), (0, 255, 0), 2)

    # Dibujar líneas horizontales
    for i in range(1, filas):
        y = i * h // filas
        cv2.line(img, (0, y), (w, y), (0, 255, 0), 2)

    cv2.imwrite("foto_con_cuadricula.jpg", img)