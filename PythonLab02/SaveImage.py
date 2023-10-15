from PIL import Image

img = Image.open("Image01.jpg")
img.save("tmp.jpg")
img.save("tmp.bmp", "BMP")
f = open("tmp2.bmp", "wb")
img.save(f, "BMP")
f.close()