from PIL import Image
from binascii import hexlify, unhexlify
import binascii
import os
import sys

sys.set_int_max_str_digits(0)


def file2hex(input_file, output_file):
    with open(input_file, "rb") as fd_in, open(output_file, "wb") as fd_out:
        while chunk := fd_in.read(20):
            fd_out.write(hexlify(chunk))
            fd_out.write(b"\n")

#----------------------Put file name-----------------------------------
inputFile = "input2.png"

file2hex(inputFile, "hex_data.txt")

# delete all previous data from the file
open('binary_data.txt', 'w').close()
open('hex_data_opt.txt', 'w').close()
try:
    os.remove("crypted.png")
    print("Encrypting...")
except:
    print("Encrypting...")

# ---------------converts hex data to binary data and store in the bin file-------------------------

with open('hex_data.txt', 'r') as file:
    data = file.read().replace('\n', '')

# --print("Initial string", data)

# Code to convert hex to binary
n = int(data, 16)
bStr = ''
while n > 0:
    bStr = str(n % 2) + bStr
    n = n >> 1
res = bStr

# with open("binary_data.txt", "r+") as binary_data:
#   binary_data.write(res)


# Print the resultant string
# --print("Resultant string", str(res))

binaryList = [*res]
# --print(binaryList)

img = Image.open(inputFile)
l, b = img.size
l = l*2
b = b*2
img.close()

stringInt = 0

img = Image.new("RGB", (l, b), (255, 0, 0))
img.save("crypted.png", "PNG")

img = Image.open("crypted.png")
pixels = img.load()

for i in range(img.size[0]):  # for every pixel:
    for j in range(img.size[1]):
        if len(binaryList) == stringInt:
            break
        elif binaryList[stringInt] == "1":
            pixels[i, j] = (0, 0, 0)
        else:
            pixels[i, j] = (255, 255, 255)
        stringInt += 1

img.save("crypted.png")
print("Image encrypted successfully")
