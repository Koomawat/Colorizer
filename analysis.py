import random
import collections
from operator import itemgetter
from basicColorizer import *
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from PIL import Image
from matplotlib import image


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

def traverseImg(og, col):

    # Get width and height of image
    height = len(og)
    width = len(og[0])

    rDiff = []
    gDiff = []
    bDiff = []

    for h in range (height):
        for w in range (width):
            r,g,b = difference(og[h], col[h])
            rDiff.append(r)
            gDiff.append(g)
            bDiff.append(b)
    
    return rDiff, gDiff, bDiff

def difference(ogPixel, colPixel):
    rdiff = abs(ogPixel[0] - colPixel[0])
    gdiff = abs(ogPixel[1] - colPixel[1])
    bdiff = abs(ogPixel[2] - colPixel[2])
    return rdiff, gdiff, bdiff

def avg(diff):
    diffAvg = sum(diff)/len(diff)
    return diffAvg

def main():
    
    ogPixel = pixelfy('download')
    colPixel = pixelfy('result')

    rDiff, gDiff, bDiff = traverseImg(ogPixel, colPixel)
    rAvg = avg(rDiff)
    gAvg = avg(gDiff)
    bAvg = avg(bDiff)
    print(f'R: {rAvg}; G: {gAvg}, B: {bAvg}')
    finalAvg = avg([rAvg, gAvg, bAvg])
    print(f'Average difference: {finalAvg}')
    print(f'Difference Percentage: {round(finalAvg/255, 3)*100}%')

    return

if __name__ == "__main__":
    main()