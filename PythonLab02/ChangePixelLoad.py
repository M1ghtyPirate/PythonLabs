from PIL import Image

img = Image.open("Image02.jpg")

obj = img.load()
print(obj[25, 45])
obj[25, 45] = (255, 0, 0)

img.show()