from PIL import Image

img = Image.open('github.png', 'r')

pix_val = list(img.getdata())

print(pix_val)