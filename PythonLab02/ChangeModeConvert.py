from PIL import Image

img = Image.open("Image02.jpg")
img = img.convert("RGBA")
print(img.mode)

img.show()