import math
from PIL import Image

def kColorLeft(img, rgbDataPoints, k, colors, height, width):

    imgCopy = img.copy()
    pix = imgCopy.load()

    count = 0

    # Replacing left half of the colored image with the nearest representative color from clustering
    for h in range(height):
        for w in range(width//2):

            currRGB = rgbDataPoints[count]

            distCompare = []

            r = currRGB[0]
            g = currRGB[1]
            b = currRGB[2]

            # Iterating a distance check to every cluster center
            for j in range(k):

                tempR = colors[j][0]
                tempG = colors[j][1]
                tempB = colors[j][2]

                rDiff = 2 * ((r - tempR) ** 2)
                gDiff = 4 * ((g - tempG) ** 2)
                bDiff = 3 * ((b - tempB) ** 2)

                dist = math.sqrt(rDiff + gDiff + bDiff)
                distCompare.append(dist)

            # Finding the closest cluster and replacing the color to the nearest representative color
            lowestIndex = distCompare.index(min(distCompare))    
            pix[w,h] = colors[lowestIndex]
            count += 1

        count += (width//2)

    #imgCopy.show()

    return imgCopy

