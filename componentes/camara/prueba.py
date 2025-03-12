import cv2 as cv
import os

ruta_imagen = os.path.abspath("figures/foto.jpeg")

# Verificar si el archivo existe
if not os.path.exists(ruta_imagen):
    print(f"❌ ERROR: La imagen no se encuentra en: {ruta_imagen}")
else:
    print(f"✅ La imagen existe en: {ruta_imagen}")

    img = cv.imread(ruta_imagen)

    if img is None:
        print("❌ ERROR: OpenCV no pudo cargar la imagen. Verifica el formato y permisos.")
    else:
        cv.imshow("Display window", img)
        cv.waitKey(0)
        cv.destroyAllWindows()
