from newColoredLeft import *
from kMeansCluster import *
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import random
from scipy import misc
import math
import collections
from operator import itemgetter
import time


def basic(img, img2, k, rgbDataPoints, height, width):

    start = time.time()

    pic = img

    # Converting image to grayscale
    r, g, b = pic[:,:,0], pic[:,:,1], pic[:,:,2]

    # Using formula grayscale = 0.21r + 0.72g + 0.21b
    picGray = 0.21 * r + 0.72 * g + 0.07 * b
    #plt.imshow(picGray, cmap='gray')
    #plt.show()

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
    #plt.imshow(kColorVals, cmap='gray')
    #plt.show()

    halfKMeans = kColorLeft(img2, rgbDataPoints, k, newClusterCenters, height, width)
    halfKMeansCopy = halfKMeans.copy()
    pixels = halfKMeansCopy.load()

    # BW Euclidean distance of 9x1 vector, find most similar six on left

    widthCut = width // 2
    heightCut = height

    # BW Training (left side)
    bwTraining = picGray[:, :widthCut]
    #plt.imshow(bwTraining, cmap='gray')
    #plt.show()

    # BW Testing (right side)
    bwTesting = picGray[:, widthCut:]
    #plt.imshow(bwTesting, cmap='gray')
    #plt.show()

    euclideanListCompare = []
    indexList = []
    representativeColors = []

    locations = []

    thousandSamples = []

    for i in range(heightCut):
        for j in range(widthCut):

            if i !=0 and i != heightCut-1 and j !=0 and j != widthCut-1:
                locations.append((i,j))

    thousandSamples = random.sample(locations,1000)
    

    for h in range (heightCut):
        print(h)
        for w in range (widthCut):

            if h!=0 and h!= heightCut-1 and w!= widthCut-1:

                g0 = picGray[h-1, w-1+widthCut]
                g1 = picGray[h-1, w+widthCut]
                g2 = picGray[h-1, w+1+widthCut]   
                g3 = picGray[h, w-1+widthCut]
                g4 = picGray[h, w+widthCut]
                g5 = picGray[h, w+1+widthCut]
                g6 = picGray[h+1, w-1+widthCut]
                g7 = picGray[h+1, w+widthCut]
                g8 = picGray[h+1, w+1+widthCut]
            

                for i in range (1000):

                    h2 = thousandSamples[i][0]
                    w2 = thousandSamples[i][1]

                    g_0 = bwTraining[h2-1, w2-1]
                    g_1 = bwTraining[h2-1, w2]
                    g_2 = bwTraining[h2-1, w2+1]   
                    g_3 = bwTraining[h2, w2-1]
                    g_4 = bwTraining[h2, w2]
                    g_5 = bwTraining[h2, w2+1]
                    g_6 = bwTraining[h2+1, w2-1]
                    g_7 = bwTraining[h2+1, w2]
                    g_8 = bwTraining[h2+1, w2+1]

                    eucDistance = 0

                    eucDistance = math.sqrt(
                    ((g0 - g_0) ** 2) + 
                    ((g1 - g_1) ** 2) +
                    ((g2 - g_2) ** 2) +
                    ((g3 - g_3) ** 2) +
                    ((g4 - g_4) ** 2) +
                    ((g5 - g_5) ** 2) +
                    ((g6 - g_6) ** 2) +
                    ((g7 - g_7) ** 2) +
                    ((g8 - g_8) ** 2))
                    #print(eucDistance)
                    euclideanListCompare.append((eucDistance))
                    indexList.append((h2,w2))  

                #print("-------------------")
                #print(euclideanListCompare)

                for i in range(7):
                    
                    #print("------------------")
                    minEuc = min(enumerate(euclideanListCompare), key=itemgetter(1))[0]
                    #print(minEuc, " ",val)
                    location = indexList[minEuc]
                    locationH = location[0]
                    locationW = location[1]
                    currColor = pixels[locationW, locationH]
                    representativeColors.append(currColor)
                    del euclideanListCompare[minEuc]
                    del indexList[minEuc]

                
                colorCount = collections.Counter(representativeColors)
                commonColor = colorCount.most_common()
                #print(commonColor)
                #print("w:", w, " H:", h)

                if len(commonColor) == 1:

                    pixels[w+widthCut, h] = commonColor[0][0]

                elif commonColor[0][1] > commonColor [1][1]:

                    pixels[w+widthCut, h] = commonColor[0][0]

                else:
                    #pixels[w+widthCut, h] = (0,0,0)
                    pixels[w+widthCut, h] = representativeColors[0]


                euclideanListCompare.clear()
                indexList.clear()
                representativeColors.clear()

            else:

                pixels[w+widthCut, h] = (0,0,0)

    #halfKMeansCopy.show()
    #plt.imshow(halfKMeansCopy, cmap='gray')
    #plt.show()
    #print("done")

    end = time.time()
    compTime = end - start

    return halfKMeansCopy, compTime

# For statistical analysis purposes
def original(img, img2, k, rgbDataPoints, height, width):

    start = time.time()

    pic = img

    # Converting image to grayscale
    r, g, b = pic[:,:,0], pic[:,:,1], pic[:,:,2]

    # Using formula grayscale = 0.21r + 0.72g + 0.21b
    picGray = 0.21 * r + 0.72 * g + 0.07 * b
    #plt.imshow(picGray, cmap='gray')
    #plt.show()

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
    #plt.imshow(kColorVals, cmap='gray')
    #plt.show()

    halfKMeans = kColorLeft(img2, rgbDataPoints, k, newClusterCenters, height, width)
    halfKMeansCopy = halfKMeans.copy()
    pixels = halfKMeansCopy.load()

    # BW Euclidean distance of 9x1 vector, find most similar six on left

    widthCut = width // 2
    heightCut = height

    # BW Training (left side)
    bwTraining = picGray[:, :widthCut]
    #plt.imshow(bwTraining, cmap='gray')
    #plt.show()

    # BW Testing (right side)
    bwTesting = picGray[:, widthCut:]
    #plt.imshow(bwTesting, cmap='gray')
    #plt.show()

    euclideanListCompare = []
    indexList = []
    representativeColors = []


    for h in range (heightCut):
        print(h)
        for w in range (widthCut):

            if h!=0 and h!= heightCut-1 and w!= widthCut-1:
                
                # Surrounding pixels + middle pixel
                g0 = picGray[h-1, w-1+widthCut]
                g1 = picGray[h-1, w+widthCut]
                g2 = picGray[h-1, w+1+widthCut]   
                g3 = picGray[h, w-1+widthCut]
                g4 = picGray[h, w+widthCut]
                g5 = picGray[h, w+1+widthCut]
                g6 = picGray[h+1, w-1+widthCut]
                g7 = picGray[h+1, w+widthCut]
                g8 = picGray[h+1, w+1+widthCut]
            
                
                
                for h2 in range (heightCut):
                    for w2 in range (widthCut):
                        
                        if h2!=0 and h2!= heightCut-1 and w2!=0 and w2!= widthCut-1:

                            g_0 = bwTraining[h2-1, w2-1]
                            g_1 = bwTraining[h2-1, w2]
                            g_2 = bwTraining[h2-1, w2+1]   
                            g_3 = bwTraining[h2, w2-1]
                            g_4 = bwTraining[h2, w2]
                            g_5 = bwTraining[h2, w2+1]
                            g_6 = bwTraining[h2+1, w2-1]
                            g_7 = bwTraining[h2+1, w2]
                            g_8 = bwTraining[h2+1, w2+1]

                            # calculate Euclidean distance 
                            eucDistance = math.sqrt(
                            (abs(g0 - g_0) ** 2) + 
                            (abs(g1 - g_1) ** 2) +
                            (abs(g2 - g_2) ** 2) +
                            (abs(g3 - g_3) ** 2) +
                            (abs(g4 - g_4) ** 2) +
                            (abs(g5 - g_5) ** 2) +
                            (abs(g6 - g_6) ** 2) +
                            (abs(g7 - g_7) ** 2) +
                            (abs(g8 - g_8) ** 2))
                            #print(eucDistance)
                            euclideanListCompare.append(eucDistance)
                            indexList.append((h2,w2))  

                #print("-------------------")
                #print(euclideanListCompare)

                # six similar seraches
                for i in range(6):
                    
                    #print("------------------")
                    minEuc = min(enumerate(euclideanListCompare), key=itemgetter(1))[0]
                    val = min(enumerate(euclideanListCompare), key=itemgetter(1))[1]
                    #print(minEuc, " ",val)
                    location = indexList[minEuc]
                    locationH = location[0]
                    locationW = location[1]
                    currColor = pixels[locationW, locationH]
                    representativeColors.append(currColor)
                    del euclideanListCompare[minEuc]
                    del indexList[minEuc]
            
                colorCount = collections.Counter(representativeColors)
                commonColor = colorCount.most_common()
                #print(commonColor)
                #print("w:", w, " H:", h)

                if len(commonColor) == 1:

                    pixels[w+widthCut, h] = commonColor[0][0]

                elif commonColor[0][1] > commonColor [1][1]:

                    pixels[w+widthCut, h] = commonColor[0][0]

                else:
                    #pixels[w+widthCut, h] = (0,0,0)
                    pixels[w+widthCut, h] = representativeColors[0]


                euclideanListCompare.clear()
                indexList.clear()
                representativeColors.clear()

            else:

                pixels[w+widthCut, h] = (0,0,0)

    #halfKMeansCopy.show()
    #plt.imshow(halfKMeansCopy, cmap='gray')
    #plt.show()
    #print("done")

    end = time.time()
    compTime = end - start

    return halfKMeansCopy, compTime