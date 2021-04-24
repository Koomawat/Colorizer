import math

def kCluster(k, vals, randomCenters):

    lenVals = len(vals)

    # Inititalizing a 2D array of size K
    clustersList = [[] for _ in range(k)] 

    # Initializing a distance compare list to hold the distance values to each cluster
    distCompare = []

    # Iterating all the RGB data points
    for i in range(lenVals):

        r = vals[i][0]
        g = vals[i][1]
        b = vals[i][2]

        # Iterating a distance check to every cluster center
        for j in range(k):

            tempR = randomCenters[j][0]
            tempG = randomCenters[j][1]
            tempB = randomCenters[j][2]

            rDiff = 2 * ((r - tempR) ** 2)
            gDiff = 4 * ((g - tempG) ** 2)
            bDiff = 3 * ((b - tempB) ** 2)

            dist = math.sqrt(rDiff + gDiff + bDiff)
            distCompare.append(dist)
        
        # Setting the current data point to the closest cluster
        lowestIndex = distCompare.index(min(distCompare))    
        clustersList[lowestIndex].append(vals[i])

        # Emptying the distance compare array for the next data point iteration
        distCompare = []

    # Initializing a new list to hold the average RGB value of each cluster
    newCenters = [(0,0,0)]*k

    # Iterating each cluster to find the average
    for i in range(len(clustersList)):

        (x,y,z) = [sum(x) // len(x) for x in zip(*clustersList[i])]
        
        avg = (x,y,z)

        # Appending the average cluster RGB to the data points sequence
        vals.append(avg)
        newCenters[i] = avg

        # Removing the old center from the cluster since the average was appended as the new center
        vals.remove(randomCenters[i])
         
    # Returning the new center values of each cluster
    return newCenters