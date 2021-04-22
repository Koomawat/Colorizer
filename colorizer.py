from basicColorizer import *
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

def convertToGrayscale(rgb):
    return np.dot(rgb[...,:3], [0.21, 0.72, 0.07])

def main():
    
    beach = mpimg.imread('beach.jpg')

    plt.imshow(beach, cmap='gray')
    plt.show()

    r, g, b = beach[:,:,0], beach[:,:,1], beach[:,:,2]
    beachGray = 0.21 * r + 0.72 * g + 0.07 * b
    
    plt.imshow(beachGray, cmap='gray')
    plt.show()

    
if __name__ == "__main__":
    main()