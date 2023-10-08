from PIL import Image

img = Image.open("Image01.jpg").convert("P", None, Image.FLOYDSTEINBERG, Image.ADAPTIVE, 2)

img.show()