from PIL import Image

img = Image.open("Image01.jpg").convert("L")

img.show()