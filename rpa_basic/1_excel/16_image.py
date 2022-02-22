from openpyxl import Workbook
from openpyxl.drawing.image import Image

wb = Workbook()
ws = wb.active

img = Image("img.png")

#C3 위치에 img.png 파일의 이미지를 삽입s
ws.add_image(img, "C3")

wb.save("sample_image.xlsx")

# ImportError : you must install pillow to fetch image...
# pip install Pillow