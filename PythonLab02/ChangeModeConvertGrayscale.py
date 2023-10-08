from PIL import Image

img = Image.open("Image02.jpg").convert("L")

img.show()