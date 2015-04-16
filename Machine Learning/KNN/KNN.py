from numpy import *
import operator


def demoData():
    '''
    Function: demoData
    Summary: generate the demo dataset for KNN
    Returns: (group): dataSet
             (labels): label for each node
    '''
    group = array([[1.0, 0.9], [1.0, 1.0], [0.1, 0.2], [0.0, 0.1]])

    labels = ['A', 'A', 'B', 'B']
    return group, labels


def classifySet(newInput, dataSet, labels, k):
    '''
    Function: classifySet
    Summary: calculate the k nearest node from newInput node
    Examples: InsertHere
    Attributes: 
        @param (newInput): new node to be classified size: 1 * N
        @param (dataSet): data set that already exists size: N * M
        @param (labels): the label of each node size: 1 * M
        @param (k): the number of neighbors to be searched
    Returns: (maxIndex): the most voted label for newInput
    '''
    # 1. calculate the distance
    row_num = dataSet.shape[0]  # shape[0] is the row num of dataSet
    # tile(A, reps): construct an array by repeating A the number of times
    # given by reps
    diff = tile(newInput, (row_num, 1)) - dataSet
    # hence, tile(newInput, (row_num, 1)) expand the newInput to the size of
    # dataSet
    squaredDiff = diff ** 2  # squared the diff result
    squaredDistance = sum(squaredDiff, axis=1)
    distance = squaredDistance ** 0.5
    # argsort returns the indices that sorts an array(the index in the sorted
    # array)
    sortedDistance = argsort(distance)

    # 2. vote with lowest k distances
    classCount = {}
    for i in range(k):
        voteLabel = labels[sortedDistance[i]]
        classCount[voteLabel] = classCount.get(voteLabel, 0) + 1
    # 3. sort dictionary

    maxCount = 0
    for key, val in classCount.items():
        if val > maxCount:
            maxCount = val
            maxIndex = key
    return maxIndex


def myClassify(newInput, dataSet, labels, k):
    '''
    Function: myClassify
    Summary: my calculation method for KNN, it is easy to understand but it runs slower than matrix substract
    Attributes: 
        @param (newInput): new node to be classified size: 1 * N
        @param (dataSet): data set that already exists size: N * M
        @param (labels): the label of each node size: 1 * M
        @param (k): the number of neighbors to be searched
    Returns: (maxIndex): the most voted label for newInpu
    '''
    
    distance = []
    for vector in dataSet:
        distance.append(sum((vector - newInput) ** 2) ** 0.5)
    sortedDistance = argsort(distance)
    classCount = {}
    for i in range(k):
        voteLabel = labels[sortedDistance[i]]
        classCount[voteLabel] = classCount.get(voteLabel, 0) + 1
    maxCount = 0
    for key, val in classCount.items():
        if val > maxCount:
            maxCount = val
            maxIndex = key
    return maxIndex