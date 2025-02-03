#USE PYTHON 3.9.13 FOR THIS FILE TO WORK
from PIL import Image
lines = open("asciibrightnessvalues.txt").readlines()

#open image to be able to get info from it
image = Image.open(input("Which image would you like to convert to ascii? "))
dimensions = image.size


#read the image's pixels in RGB tuples
allpixels = list(image.getdata())

#create 2-dimensional matrix from RGB tuples
pixelmatrix = [allpixels[row*dimensions[0]:(row+1)*dimensions[0]] for row in range(dimensions[1])]


#convert RGB to brightness
brightnessmatrix = pixelmatrix.copy()

for x in range(len(brightnessmatrix)):
    for y in range(len(brightnessmatrix[x])):
        #convert pixel to average brightness value
        brightnessmatrix[x][y] = (brightnessmatrix[x][y][0]+brightnessmatrix[x][y][1]+brightnessmatrix[x][y][2]) // 3
        if brightnessmatrix[x][y] > 1:
            brightnessmatrix[x][y] -= 1


#set brightness values to ascii characters
asciivalues = {i:(lines[i].rstrip("\n")) for i in range(len(lines))}

#convert brightness to ascii
asciimatrix = brightnessmatrix.copy()
for x in range(len(asciimatrix)):
    for y in range(len(asciimatrix[x])):
        #convert pixel to average brightness value
        asciimatrix[x][y] = asciivalues[asciimatrix[x][y]]


#print out the image
for x in range(len(asciimatrix)):
    print(*asciimatrix[x])

print(f"Image Size: {dimensions[0]} x {dimensions[1]}")