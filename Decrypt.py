import cv
import sys

file1 = str(sys.argv[1])
file2 = str(sys.argv[2])
image1 = cv.LoadImage(file1)
image2 = cv.LoadImage(file2)

message = ''
i = 0
while True:
    x1,y1,z1 = image1[i,12]
    x2,y2,z2 = image2[i,12]
    if (y2 - y1) == 14:
        message += ' '
    elif chr(int(y2-y1) + 77) == '!':
        break
    else:
        message += chr(int(y2-y1) + 77)
    i += 1
print message
