from PIL import Image
from binascii import hexlify, unhexlify
import binascii
import os
import sys

sys.set_int_max_str_digits(0)

print("Decrypting...")

def hex2file(input_file, output_file):
    with open(input_file, "rb") as fd_in, open(output_file, "wb") as fd_out:
        for line in fd_in:
            fd_out.write(unhexlify(line.rstrip()))


# delete all previous data from the file
open('binary_data.txt', 'w').close()
open('hex_data_opt.txt', 'w').close()

# -----------------------------convert binary data to hex data and store in the hex_opt file-----------------------
img = Image.open("crypted.png")
outputImg = img.load()
outputList = []

for i in range(img.size[0]):  # for every pixel:
    for j in range(img.size[1]):
        if outputImg[i, j] == (0, 0, 0):
            outputList.append("1")
        elif outputImg[i, j] == (255, 255, 255):
            outputList.append("0")

#--print(outputList)

file = open('binary_data.txt', 'w')
file.writelines(outputList)
file.close()

with open("binary_data.txt", "r") as file:
    bnum = file.read()

b = int(bnum, 2)
hdnum = hex(b)[2:]

with open("hex_data_opt.txt", "w") as file:
    file.write(hdnum)

#--print("\nEquivalent Hexadecimal Value = ", hdnum)

# ------------------------------------------------hex2file------------------------------------------------------------
hex2file("hex_data_opt.txt", "output.png")

try:
    print("Decrypted Successfully")
    img = Image.open("output.png")
    img.show()
except:
    print("Decrypted Successfully \n Can't open this file")



'''
img = Image.open('github.png', 'r')

# pix_val = list(img.getdata())

l, b = img.size

# print(pix_val)
print(l, b)'''
