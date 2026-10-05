from PIL import Image
import os
from pathlib import Path

def recortar_fotogramas():
    # Imagen que contiene los 16 fotogramas
    imagen = Image.open("saludo.png")

    # Tenemos 4 cuadros por fila y 4 por columna
    columnas = 4
    filas = 4

    # Tamaño total de la imagen
    ancho, alto = imagen.size

    # Calculamos el tamaño de cada fotograma
    ancho_frame = ancho // columnas
    alto_frame = alto // filas

    # Carpeta donde guardaremos los frames
    os.makedirs("frames", exist_ok=True)

    numero = 1

    for fila in range(filas):
        for columna in range(columnas):
            izquierda = columna * ancho_frame +1
            arriba = fila * alto_frame
            derecha = (columna + 1) * ancho_frame - 1
            abajo = arriba + alto_frame

            frame = imagen.crop((
                izquierda,
                arriba,
                derecha,
                abajo
            ))

            frame.save(f"frames/frame_{numero:02d}.png")

            numero += 1


def main():
    recortar_fotogramas()
    # Buscamos todos los frames dentro de la carpeta "frames"
    archivos = sorted(Path("frames").glob("frame_*.png"))

    # Verificamos que haya frames
    if not archivos:
        print("No se encontraron frames.")
        return

    # Abrimos todos los frames
    frames = [Image.open(archivo) for archivo in archivos]

    # Creamos el GIF
    frames[0].save(
        "saludo.gif",
        save_all=True,
        append_images=frames[1:],
        duration=250,
        loop=0
    )

    print("GIF creado correctamente.")


if __name__ == "__main__":
    main()