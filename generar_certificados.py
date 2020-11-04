# ACLARACION: La generación de certificados sin validación de
# algún ente oficial puede ser ilegal. Usar este código
# considerando esto. No me hago responsable de su uso.

#///---- Imports ----///
import pandas as pd
from PIL import Image, ImageDraw, ImageFont

#///---- Extract data ----///
data = pd.read_excel (r'estudiantes.xlsx') 
name_list = data["Nombre"].tolist() 

#///---- Generate certificates ----///
for i in name_list:
    img = Image.open(r'certificado_base.jpg')
    draw = ImageDraw.Draw(img)

    location = (45, 220)
    text_color = (0, 137, 209)
    font = ImageFont.truetype("arial.ttf", 45)
    draw.text(location, i, fill = text_color, font = font)

    img.save("certificados\\certificate_" + i + ".pdf")