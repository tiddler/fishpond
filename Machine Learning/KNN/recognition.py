from numpy import *
import operator
import os

import KNN


def txt2vector(filename, row_num=32, col_num=32):
    '''
    Function: txt2vector
    Summary: convert a txt file of an image to a vector
    Examples: 32 * 32 strings to 1 * 1024 vector
    Attributes: 
        @param (filename):file's path
        @param (row_num) default=32: row number
        @param (col_num) default=32: col number
    Returns: result vector after being processed
    '''
    result = zeros((1, row_num * col_num))
    file = open(filename)
    for row in range(row_num):
        str = file.readline()
        for col in range(col_num):
            result[0, 32 * row + col] = int(str[col])
    return result


def writingRecog(filename):
    hwLabels = []
    trainingFileList = os.listdir('digits/trainingDigits')
    row_num = len(trainingFileList)
    trainingMatrix = zeros((row_num, 1024))
    print("Start trainning.")
    for i in range(row_num):
        nameStr = trainingFileList[i]
        fileStr = nameStr.split('.')[0]
        classNumStr = int(fileStr.split('_')[0])
        hwLabels.append(classNumStr)
        trainingMatrix[i, :] = txt2vector(
            'digits/trainingDigits/{0}'.format(nameStr))
    print("Training finishes. Trainning example : {0}".format(row_num))

    testVector = txt2vector('demo.txt')
    classifyResult = KNN.classifySet(
        testVector, trainingMatrix, hwLabels, 4)
    print('the recognition result is {0}'.format(
        classifyResult))


def demoRecognition(k=4):
    '''
    Function: demoRecognition
    Summary: construct the train set and test the KNN classify error rate with test set
    Attributes: 
        @param (k) default=4: the number of neighbors to search
    '''

    hwLabels = []
    trainingFileList = os.listdir('digits/trainingDigits')
    row_num = len(trainingFileList)
    trainingMatrix = zeros((row_num, 1024))
    print("Start trainning.")
    for i in range(row_num):
        nameStr = trainingFileList[i]
        fileStr = nameStr.split('.')[0]
        classNumStr = int(fileStr.split('_')[0])
        hwLabels.append(classNumStr)
        trainingMatrix[i, :] = txt2vector(
            'digits/trainingDigits/{0}'.format(nameStr))
    print("Training finishes. Trainning example : {0}".format(row_num))

    testFileList = os.listdir('digits/testDigits')
    errorCount = 0
    row_num = len(testFileList)
    for i in range(row_num):
        nameStr = testFileList[i]
        fileStr = nameStr.split('.')[0]
        classNumStr = int(fileStr.split('_')[0])
        testVector = txt2vector('digits/testDigits/{0}'.format(nameStr))
        classifyResult = KNN.classifySet(
            testVector, trainingMatrix, hwLabels, k)
        print('the recognition result is {0}, the real result is {1}'.format(
            classifyResult, classNumStr))
        if classifyResult != classNumStr:
            errorCount += 1
    print("finish")
    print("the error rate is {0: f}".format(errorCount / row_num))

if __name__ == '__main__':
    demoRecognition()
