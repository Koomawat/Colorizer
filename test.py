import random
import collections

def main():
    

    val = [(1,2,3), (4,5,6), (7,8,9), (7,8,9), (3,5,9)]

    #val = list(set(val))

    print(random.sample(val, 3))

    temp = [(0,0,0),(1,2,3)]

    print(temp[1][1])

    clustersList = [[] for _ in range(5)] 

    clustersList[0].append(val[1])

    print(clustersList[0][0])
    print(clustersList)
    
    a_list = [(1,2), (1,2), (1,2), (4,3), (4,3)]

    count = collections.Counter(a_list)

    print(count)

    com = count.most_common()
    print(com)

    print(com[0][0])

    if com[0][1] > com[1][1]:
        print("pog")

    test = [] 
    test.append(1.12312312)
    test.append(2.12312345)
    lowestIndex = test.index(min(test))
    test.pop(lowestIndex)
    print(lowestIndex)

    print(test)

    return
    
if __name__ == "__main__":
    main()