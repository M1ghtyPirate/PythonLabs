from PIL import Image

img = Image.open("Image01.jpg")
img = img.convert("RGBA")
print(img.mode)

img.show()