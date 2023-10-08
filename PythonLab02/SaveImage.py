from PIL import Image

img = Image.open("Image02.jpg")
img.save("tmp.jpg")
img.save("tmp.bmp", "BMP")
f = open("tmp2.bmp", "wb")
img.save(f, "BMP")
f.close()