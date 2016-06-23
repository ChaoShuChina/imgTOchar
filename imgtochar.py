__author__ = 'chao-shu'
from PIL import Image
import argparse


ascii_char = list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLNMOPQRSTUVWXYZ1234567890-=!@#$%^&*()")
def get_char(r,g,b,alpha = 256):
    if alpha == 0:
        return ' '
    lenght = len(ascii_char)
    gray = int(0.2126*r + 0.7152*g + 0.0722*b)
    unit = (256.0 + 1)/lenght
    return ascii_char[int(gray/unit)]

parser = argparse.ArgumentParser()
parser.add_argument("file")
# parser.add_argument('output')
parser.add_argument('width',type = int,default = 80)
parser.add_argument('height',type = int,default = 80)

args = parser.parse_args()
IMG = args.file
WIDTH = args.width
HEIGHT = args.height
# OUTPUT = args.output


im = Image.open(IMG)
im = im.resize((WIDTH,HEIGHT),Image.NEAREST)
txt = ''
for i in range(HEIGHT):
    for j in range(WIDTH):
        txt += get_char(*im.getpixel((j,i)))
    txt += '\n'
with open("output.txt",'w') as outputfile:
    outputfile.write(txt)
