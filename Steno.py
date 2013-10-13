import cv
import sys

file = str(sys.argv[1])
message = str(sys.argv[2])
image = cv.LoadImage(file)
message += '!'
for i in range(len(message)):
    if message[i] != ' ':
        modify = ord(str.upper(message[i])) - 77
        x , y , z = image[i,12]
        image[i,12] = x, y + modify, z
    else:
        modify = 14
        x , y , z = image[i,12]
        image[i,12] = x, y + modify, z
cv.SaveImage(file, image)

