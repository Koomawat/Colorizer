import random

def main():
    

    val = [(1,2,3), (4,5,6), (7,8,9), (7,8,9), (3,5,9)]

    #val = list(set(val))

    print(random.sample(val, 3))

    temp = [(0,0,0),(1,2,3)]

    print(temp[1][1])

    clustersList = [[] for _ in range(5)] 

    clustersList[0].append(val[1])

    print(clustersList)

    return
    
if __name__ == "__main__":
    main()