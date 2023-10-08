from PIL import Image

img = Image.open("Image01.jpg")

print(img.size)
print(img.mode)
print(img.format)
print(img.info)
print(img.getbbox())