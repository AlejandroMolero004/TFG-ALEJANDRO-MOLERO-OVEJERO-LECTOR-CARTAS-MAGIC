# 🃏 TFG - Lector de Cartas Magic

Sistema de reconocimiento automático de cartas de *Magic: The Gathering* desarrollado como Trabajo de Fin de Grado.

El proyecto utiliza visión por computador y OCR para detectar cartas mediante una cámara, extraer automáticamente su nombre y consultar información relacionada usando la API de Scryfall.

## ✨ Funcionalidades

- Captura de imágenes mediante cámara.
- Procesamiento y mejora de imagen con OpenCV.
- Reconocimiento de texto mediante Tesseract OCR.
- Identificación automática de cartas.
- Consulta de información desde Scryfall.
- Visualización de:
  - Nombre
  - Tipo
  - Coste de maná
  - Rareza
  - Imagen
  - Precio aproximado
  - Recomendaciones
- Interfaz web desarrollada con Fresh y Deno.

## 🛠️ Tecnologías utilizadas

- Python
- OpenCV
- Tesseract OCR
- Raspberry Pi 5
- Fresh
- Deno
- TypeScript
- Scryfall API
- Playwright

## 📋 Instrucciones de uso
En primer lugar, desde una terminal situada en la carpeta principal del proyecto (`PROGRAMAS-PARA-CAMARA`), se activa el entorno virtual de Python mediante el siguiente comando:

```bash
source venv/bin/activate
```

Una vez activado el entorno virtual, se inicia la API utilizando:

```bash
python -m uvicorn API.server:app --reload --port 8001
```

Posteriormente, se abre una segunda terminal en la misma carpeta del proyecto y se vuelve a activar el entorno virtual. Después, se accede a la carpeta del frontend mediante:

```bash
cd FRONT
```

Finalmente, el frontend se inicia utilizando el siguiente comando:

```bash
deno task start
```

Una vez iniciado el servidor web, el sistema proporcionará una URL local desde la que será posible acceder a la aplicación web y utilizar el sistema de reconocimiento automático de cartas.


## 🚀 Objetivo

El objetivo principal del proyecto es demostrar la viabilidad del uso de técnicas de visión por computador y OCR para reconocer automáticamente cartas coleccionables en tiempo real.

## 👨‍💻 Autor

Alejandro Molero Ovejero  
Universidad Nebrija — Ingeniería Informática
