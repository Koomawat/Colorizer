import random
import collections
from operator import itemgetter
from basicColorizer import *
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from PIL import Image
from matplotlib import image

# Convert each pixel in image to a list of RGB values
def pixelfy(imgName):
    # Open the image
    img = Image.open(f'{imgName}.jpg')
    pix = img.load()

    # Get width and height of the image
    dimension = img.size 
    width = dimension[0]
    height = dimension[1]

    # Initializing RGB data points list
    rgbDataPoints = [None] * (width * height)

    # Iterating all the pixels in the image and finding the RGB values
    count = 0
    for h in range(height):
        for w in range(width):
            rgbDataPoints[count] = pix[w,h]
            count += 1
    
    return rgbDataPoints

# Stores difference in RGB values for each pixel
def traverseImg(og, col):

    # Get width and height of image
    height = len(og)
    width = len(og[0])

    rDiff = []
    gDiff = []
    bDiff = []

    for h in range (height):
        for w in range (width):
            # Get difference of RGB values for one pixel
            r,g,b = difference(og[h], col[h])
            # Store the difference individually
            rDiff.append(r)
            gDiff.append(g)
            bDiff.append(b)
    
    return rDiff, gDiff, bDiff

# Calculates the difference of RGB values of a pixel
def difference(ogPixel, colPixel):
    # pixel type: (r, g, b)
    rdiff = abs(ogPixel[0] - colPixel[0])
    gdiff = abs(ogPixel[1] - colPixel[1])
    bdiff = abs(ogPixel[2] - colPixel[2])
    return rdiff, gdiff, bdiff

# Takes an average of elements in a list
def avg(diff):
    diffAvg = sum(diff)/len(diff)
    return diffAvg

def main():
    
    # Pixelfy images into an array of RGB values 
    ogPixel = pixelfy('download')
    colPixel = pixelfy('result')

    # Get each pixel's difference in RGB values
    rDiff, gDiff, bDiff = traverseImg(ogPixel, colPixel)

    # Take an average of the differences for each pixel
    rAvg = avg(rDiff)
    gAvg = avg(gDiff)
    bAvg = avg(bDiff)
    print(f'R: {rAvg}; G: {gAvg}, B: {bAvg}')

    # Take an average of the differences overall 
    finalAvg = avg([rAvg, gAvg, bAvg])
    print(f'Average difference: {finalAvg}')

    print(f'Difference Percentage: {round(finalAvg/255, 3)*100}%')

    return

if __name__ == "__main__":
    main()