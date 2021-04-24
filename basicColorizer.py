from newColoredLeft import *
from kMeansCluster import *
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import random

def basic(img, img2, k, rgbDataPoints, height, width):

    pic = img

    # Converting image to grayscale
    r, g, b = pic[:,:,0], pic[:,:,1], pic[:,:,2]

    # Using formula grayscale = 0.21r + 0.72g + 0.21b
    picGray = 0.21 * r + 0.72 * g + 0.07 * b

    # Getting k random starting cluster centers
    randomCenters = []
    dataCopy = rgbDataPoints
    dataCopy = list(set(dataCopy))
    randomCenters = random.sample(dataCopy, k)
    
    # Calling k means algorithm on the data points
    newClusterCenters, rgbDataPoints = kCluster(k, rgbDataPoints, randomCenters)

    # Repeating the algorithm until no cluster changes are made
    while(newClusterCenters != randomCenters):

        randomCenters = newClusterCenters
        newClusterCenters, rgbDataPoints = kCluster(k, rgbDataPoints, randomCenters)

    # Printing the k clusters center colors
    newClusterCentersNP = np.array(newClusterCenters)
    kColorVals = newClusterCentersNP.reshape(1,k,3)
    plt.imshow(kColorVals, cmap='gray')
    plt.show()

    kColorLeft(img2, rgbDataPoints, k, newClusterCenters, height, width)

    return