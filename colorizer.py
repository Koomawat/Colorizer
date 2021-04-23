from basicColorizer import *
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from PIL import Image
import random
import math

def convertToGrayscale(rgb):
    return np.dot(rgb[...,:3], [0.21, 0.72, 0.07])


def kCluster(k, vals, width, height):

    lenVals = len(vals)

    randomCenters = []

    valsCopy = vals
    valsCopy = list(set(valsCopy))

    randomCenters = random.sample(valsCopy, k)

    clustersList = [[] for _ in range(k)] 

    distCompare = []

    for i in range(lenVals):

        r = vals[i][0]
        g = vals[i][1]
        b = vals[i][2]

        for j in range(k):

            tempR = randomCenters[k][0]
            tempG = randomCenters[k][1]
            tempB = randomCenters[k][2]

            rDiff = 2 * ((r - tempR) ** 2)
            gDiff = 4 * ((g - tempG) ** 2)
            bDiff = 3 * ((b - tempB) ** 2)

            dist = math.sqrt(rDiff + gDiff + bDiff)
            distCompare.append(dist)
        

        lowestIndex = distCompare.index(min(distCompare))    
        clustersList[lowestIndex].append(vals[i])


    resultCenters = []

    return resultCenters


def main():
    
    img = Image.open('beach.jpg')
    pix = img.load()
    dimension = img.size 
    width = dimension[0]
    height = dimension[1]

    print(width)

    rgbDataPoints = [None] * (width * height)
    
    k = 5

    count = 0

    for h in range(height):
        for w in range(width):
            rgbDataPoints[count] = pix[w,h]
            count += 1

    # dont print rgbDataPoints unless u want 10,000+ lines of RGB values

    beach = mpimg.imread('beach.jpg')

    plt.imshow(beach, cmap='gray')
    plt.show()

    r, g, b = beach[:,:,0], beach[:,:,1], beach[:,:,2]
    beachGray = 0.21 * r + 0.72 * g + 0.07 * b

    plt.imshow(beachGray, cmap='gray')
    plt.show()

    
if __name__ == "__main__":
    main()