import pandas as pd
import requests
import base64
from io import BytesIO
from PIL import Image

# Reading data
df = pd.read_csv("./Export_2024-05-17_082004.csv",
                 encoding='Latin-1', encoding_errors='ignore')


data = df['Image Src']


def resize_image(image_data, new_width, new_height):

    image_bytes = base64.b64decode(image_data)
    img = Image.open(BytesIO(image_bytes))
    resized_img = img.resize((new_width, new_height), Image.Resampling.LANCZOS)
    buffered = BytesIO()
    resized_img.save(buffered, format="JPEG")
    resized_base64 = base64.b64encode(buffered.getvalue()).decode("utf-8")

    return resized_base64


# Fuction Transform
def image_url_to_base64(image_url):
    response = requests.get(image_url)

    if response.status_code == 200:
        image_content = response.content
        image_base64 = base64.b64encode(image_content).decode('utf-8')
        resized_base64 = resize_image(image_base64, 300, 300)
        return resized_base64
    else:
        raise Exception(
            f'Error: {response.status_code}')


# image_base64 = image_url_to_base64(data[55])
# print(image_base64)
array_base64 = []
for image_url in data:
    try:
        image_base64 = image_url_to_base64(image_url)
        array_base64.append(image_base64)
        print(image_base64)
    except Exception as e:
        array_base64.append(f'Error : {e}')
        print()
        print()
df['Image_64'] = array_base64

df.to_csv('outfile.csv', index=False)
