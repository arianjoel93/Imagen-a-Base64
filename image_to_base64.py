from PIL import Image
import base64
import io
from io import BytesIO

# Cargar la imagen PNG usando Pillow
image_path = './automatizacion.png'
image = Image.open(image_path)

# Convertir la imagen a un objeto BytesIO
buffered = io.BytesIO()
image.save(buffered, format="PNG")

def resize_image(image_data, new_width, new_height):
    image_bytes = base64.b64decode(image_data)
    img = Image.open(BytesIO(image_bytes))
    
    # Convertir a RGB si la imagen tiene un canal alfa
    if img.mode == 'RGBA':
        img = img.convert('RGB')
    
    # Cambiar el tamaño de la imagen
    resized_img = img.resize((new_width, new_height), Image.Resampling.LANCZOS)
    buffered = BytesIO()
    resized_img.save(buffered, format="JPEG")
    resized_base64 = base64.b64encode(buffered.getvalue()).decode("utf-8")
    return resized_base64

def image_to_base64(image):
    # Obtener los bytes de la imagen y convertir a base64
    image_base64 = base64.b64encode(buffered.getvalue()).decode('utf-8')
    resized_base64 = resize_image(image_base64, 300, 300)
    print(resized_base64)

image_to_base64(image)
