from PIL import Image
from matplotlib import pyplot

img = Image.open("Image01.jpg")
R, G, B = img.split()
img2 = Image.merge('RGB', (R, G, R))
img2.show()

pixelBrightness = []
for x in range(img2.size[0]):
    for y in range(img2.size[1]):
        r, g, b = img2.getpixel((x,y))
        pixelBrightness.append(r * 0.299 + 0.587 * g + 0.144 * b)
binsCount = 256
pyplot.hist(pixelBrightness, binsCount)
pyplot.show()