from PIL import Image

img = Image.open("Image02.jpg")

print(img.getpixel((25, 45)))
img.putpixel((25, 45), (0, 0, 255))
print(img.getpixel((25, 45)))

img.show()