import cv2

def elegir_parte_cuadricula():
    img = cv2.imread("foto2.jpg")

    if img is None:
        print("No se pudo cargar la imagen")
        return

    h, w = img.shape[:2]

    filas = 40
    columnas = 40

    alto_celda = h // filas
    ancho_celda = w // columnas

    # Desde fila 1 hasta fila 3
    fila_inicio = 6
    fila_fin = 7

    # Desde columna 1 hasta columna 5
    columna_inicio = 12
    columna_fin = 22

    x1 = columna_inicio * ancho_celda
    x2 = (columna_fin + 1) * ancho_celda

    y1 = fila_inicio * alto_celda
    y2 = (fila_fin + 1) * alto_celda

    recorte = img[y1:y2, x1:x2]

    if recorte.size == 0:
        print("Recorte vacío")
        return

    cv2.imwrite("nombre.jpg", recorte)
    print("Guardado correctamente")
#------------------------------------------------------------------
#                       TIPO DE LA CARTA                        - 
#------------------------------------------------------------------
    fila_inicio = 22
    fila_fin = 23

    
    columna_inicio = 12
    columna_fin = 24

    x1 = columna_inicio * ancho_celda
    x2 = (columna_fin + 1) * ancho_celda

    y1 = fila_inicio * alto_celda
    y2 = (fila_fin + 1) * alto_celda

    recorte = img[y1:y2, x1:x2]

    if recorte.size == 0:
        print("Recorte vacío")
        return

    cv2.imwrite("tipo.jpg", recorte)

    