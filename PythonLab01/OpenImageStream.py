from PIL import Image

f = open("Image01.jpg", "rb")
img = Image.open(f)
img.show()
f.close()