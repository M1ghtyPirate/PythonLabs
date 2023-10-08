from PIL import Image

img = Image.open("Image02.jpg")

R, G, B = img.split()

mask = Image.new("L", img.size, 128)
img2 = Image.merge("RGBA", (R, G, B, mask))

img2.show()