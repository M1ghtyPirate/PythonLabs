from PIL import Image

img = Image.open("Image01.jpg");
img = img.convert("L")
img.show()