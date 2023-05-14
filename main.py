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


def hex2file(input_file, output_file):
    with open(input_file, "rb") as fd_in, open(output_file, "wb") as fd_out:
        for line in fd_in:
            fd_out.write(unhexlify(line.rstrip()))


file2hex("github.png", "hex_data.txt")


#delete all previous data from the file
open('binary_data.txt', 'w').close()
open('hex_data_opt.txt', 'w').close()
try:
    os.remove("image.png")
except:
    print("no img")
#---------------converts hex data to binary data and store in the bin file-------------------------

with open('hex_data.txt', 'r') as file:
    data = file.read().replace('\n', '')

print("Initial string", data)

# Code to convert hex to binary
n = int(data, 16)
bStr = ''
while n > 0:
    bStr = str(n % 2) + bStr
    n = n >> 1
res = bStr

#with open("binary_data.txt", "r+") as binary_data:
 #   binary_data.write(res)


# Print the resultant string
print("Resultant string", str(res))

binaryList = [*res]
print(binaryList)

stringInt = 0

img = Image.new("RGB",(600, 400),(255,0,0))
img.save("image.png", "PNG")

img = Image.open("image.png")
pixels = img.load()


for i in range(img.size[0]): # for every pixel:
    for j in range(img.size[1]):
        if len(binaryList) == stringInt:
            break
        elif binaryList[stringInt] == "1":
            pixels[i,j] = (0,0,0)
            img.putpixel((i, j), (0, 0, 0))
            print("yes")
        else:
            pixels[i,j] =(255,255,255)
            img.putpixel((i, j), (255, 255, 255))
            print("no")
        stringInt += 1


img.save("image.png")
#-------------------------------convert binary data to hex data and store in the hex_opt file-----------------------
img = Image.open("image.png")
outputImg = img.load()
outputList = []


for i in range(img.size[0]): # for every pixel:
    for j in range(img.size[1]):
        if outputImg[i,j] == (0,0,0):
            outputList.append("1")
        elif outputImg[i,j] == (255,255,255):
            outputList.append("0")

print(outputList)

file = open('binary_data.txt','w')
file.writelines(outputList)
file.close()



with open("binary_data.txt","r") as file:
    bnum = file.read()

b = int(bnum, 2)
hdnum = hex(b)[2:]

with open("hex_data_opt.txt","w") as file:
    file.write(hdnum)
print("\nEquivalent Hexadecimal Value = ", hdnum)


#------------------------------------------------hex2file------------------------------------------------------------
hex2file("hex_data_opt.txt","output.png")





img = Image.open('github.png', 'r')

#pix_val = list(img.getdata())

l, b = img.size

#print(pix_val)
print(l,b)
