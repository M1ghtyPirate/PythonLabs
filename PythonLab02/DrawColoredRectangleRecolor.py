from PIL import Image

img = Image.new("RGB", (640, 480), "rgb(205,100,200)")
img.show()

for x in range(640):
    for y in range(480):
        img.putpixel((x, y), (0, 160, 0))
img.save("okno.png", "PNG")
img.show()