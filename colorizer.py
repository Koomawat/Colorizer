from basicColorizer import *
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from PIL import Image


def main():
    
    # Open image
    img = Image.open('beach.jpg')
    pix = img.load()
    dimension = img.size 
    #img.show()

    # Get width and height of image
    width = dimension[0]
    height = dimension[1]

    # Initializing RGB data points list
    rgbDataPoints = [None] * (width * height)
    
    # Using a k value of 5
    k = 5

    # Iterating all the pixels in the image and finding the RGB values
    count = 0
    for h in range(height):
        for w in range(width):
            rgbDataPoints[count] = pix[w,h]
            count += 1

    # Matplot image read
    image = mpimg.imread('beach.jpg')
    #plt.imshow(image, cmap='gray')
    #plt.show()

    # Calling basic colorizer
    basic(image, img, k, rgbDataPoints, height, width)

    
if __name__ == "__main__":
    main()