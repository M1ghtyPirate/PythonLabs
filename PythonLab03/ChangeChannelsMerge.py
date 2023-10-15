from PIL import Image

img = Image.open("Image01.jpg")
R, G, B = img.split()
img2 = Image.merge('RGB', (R, G, R))
img2.show()