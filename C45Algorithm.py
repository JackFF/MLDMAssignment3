import pandas as pd
import numpy as np
import random as rnd
import math

def splitDataIntoTrainingAndTesting(data):
    train = data.sample(frac=(2/3), random_state=200) #split the data randomly by 2/3
    test = data.drop(train.index) #let testing data equal to data not used in the training data

    return train, test #returns training and testing data

def calculateGlobalEntropy(data):
    globalEntropyData = {} #set for the global entropy data
    for row in (data.iloc[:, -1]): #itterates through the last column in the data set
        if row not in globalEntropyData: globalEntropyData[row] = 0 #adds the data to the set
        globalEntropyData[row] += 1

    globalEntropy = 0.0 #global entropy variable
    for row in globalEntropyData.values(): #itterates through our global entropy set
        p = float(row) / len(data.iloc[:, 4]) #calculating global entropy
        globalEntropy -= p * np.log2(p) #calculating global entropy

    return globalEntropy

def calculateEntropy(data):
    df = pd.DataFrame()
    df = df.append(data)
    df = df.transpose()
    #print(data)
    #print(df)
    entropy = 0.0

    for row in df.values:
        p = float (row) / len(data)
        entropy -= p * np.log2(p)

    return entropy

def getClasses(data):
    classes = data.iloc[:, -1]
    return classes

def splitDataIntoContinousAndNominal(data, classes):
    x = len(list(data.head(0)))
    data = data.iloc[:, 0:x-1] #rest of data, to be split into continous and nominal
    x = len(list(data.head(0)))

    continousOrNominal = {} #set that seperates the classes into continous or nominal
    for row in data.columns:
        continousOrNominal[row] = 1.*data[row].nunique()/data[row].count() < 0.05 #continous or nominal calculator

    dataFrameContinous = pd.DataFrame() #creating the empty continous & nominal dataframes
    dataFrameNominal = pd.DataFrame()

    i = 0
    
    for row in continousOrNominal.values():
        if row == False:
            dataFrameContinous = dataFrameContinous.append(data.iloc[:, i]) #adding to the dataframes
            i += 1
        else:
            dataFrameNominal = dataFrameNominal.append(data.iloc[:, i])
            i += 1

    dataFrameContinous = dataFrameContinous.transpose() #transposing the dataframes so they are "flipped" the right way
    dataFrameNominal = dataFrameNominal.transpose()

    return dataFrameContinous, dataFrameNominal


def findSplittingPointsAndSplit(data, classes, globalEntropy):
    bodyLength = pd.DataFrame()
    wingLength = pd.DataFrame()
    bodyWidth = pd.DataFrame()
    wingWidth = pd.DataFrame()
    
    bodyLength = bodyLength.append(data.iloc[:, 0])
    bodyLength = bodyLength.append(classes)
    bodyLength = bodyLength.transpose()
    bodyLength = bodyLength.sort_values(bodyLength.columns[0], ascending='True')
    
    wingLength = wingLength.append(data.iloc[:, 1])
    wingLength = wingLength.append(classes)
    wingLength = wingLength.transpose()
    wingLength = wingLength.sort_values(wingLength.columns[0], ascending='True')
    
    bodyWidth = bodyWidth.append(data.iloc[:, 2])
    bodyWidth = bodyWidth.append(classes)
    bodyWidth = bodyWidth.transpose()
    bodyWidth = bodyWidth.sort_values(bodyWidth.columns[0], ascending='True')
    
    wingWidth = wingWidth.append(data.iloc[:, 3])
    wingWidth = wingWidth.append(classes)
    wingWidth = wingWidth.transpose()
    wingWidth = wingWidth.sort_values(wingWidth.columns[0], ascending='True')
    
    #print(bodyLength)
    #print(wingLength)
    #print(bodyWidth)
    #print(wingWidth)

    i = 0

    bodyLengthThresholdPoints = []

    for row in bodyLength.values:
        if bodyLength.values[i][1] != bodyLength.values[i-1][1]:
            bodyLengthThresholdPoints.append(bodyLength.index.values[i])
            #print('fak')
        i += 1

    bodyLengthThresholdPoints.pop(0)
    #print(bodyLengthThresholdPoints)


    i = 0

    wingLengthThresholdPoints = []

    for row in bodyLength.values:
        if wingLength.values[i][1] != wingLength.values[i-1][1]:
            wingLengthThresholdPoints.append(wingLength.index.values[i])
            #print('fak')
        i += 1

    wingLengthThresholdPoints.pop(0)
    #print(wingLengthThresholdPoints)


    i = 0

    bodyWidthThresholdPoints = []

    for row in bodyWidth.values:
        if bodyWidth.values[i][1] != bodyWidth.values[i-1][1]:
            bodyWidthThresholdPoints.append(bodyWidth.index.values[i])
            #print('fak')
        i += 1

    bodyWidthThresholdPoints.pop(0)
    #print(bodyWidthThresholdPoints)


    i = 0

    wingWidthThresholdPoints = []

    for row in wingWidth.values:
        if wingWidth.values[i][1] != wingWidth.values[i-1][1]:
            wingWidthThresholdPoints.append(wingWidth.index.values[i])
            #print('fak')
        i += 1

    wingWidthThresholdPoints.pop(0)
    #print(wingWidthThresholdPoints)


    bodyLengthAbove = []
    bodyLengthBelow = []

    i = 0

    while i < len(bodyLengthThresholdPoints):
        bodyLengthAbove = data[data['body-length'] > data['body-length'][bodyLengthThresholdPoints[i]]]
        bodyLengthBelow = data[data['body-length'] <= data['body-length'][bodyLengthThresholdPoints[i]]]
        i += 1

    bodyLengthAbove = bodyLengthAbove.iloc[:, 0]
    bodyLengthBelow = bodyLengthBelow.iloc[:, 0]
    
    #print(bodyLengthAbove)
    #print(bodyLengthBelow)
    
    
    wingLengthAbove = []
    wingLengthBelow = []

    i = 0

    while i < len(wingLengthThresholdPoints):
        wingLengthAbove = data[data['wing-length'] > data['wing-length'][wingLengthThresholdPoints[i]]]
        wingLengthBelow = data[data['wing-length'] <= data['wing-length'][wingLengthThresholdPoints[i]]]
        i += 1

    wingLengthAbove = wingLengthAbove.iloc[:, 1]
    wingLengthBelow = wingLengthBelow.iloc[:, 1]
    
    #print(wingLengthAbove)
    #print(wingLengthBelow)


    bodyWidthAbove = []
    bodyWidthBelow = []

    i = 0

    while i < len(bodyWidthThresholdPoints):
        bodyWidthAbove = data[data['body-width'] > data['body-width'][bodyWidthThresholdPoints[i]]]
        bodyWidthBelow = data[data['body-width'] <= data['body-width'][bodyWidthThresholdPoints[i]]]
        i += 1

    bodyWidthAbove = bodyWidthAbove.iloc[:, 2]
    bodyWidthBelow = bodyWidthBelow.iloc[:, 2]
    
    #print(bodyWidthAbove)
    #print(bodyWidthBelow)


    wingWidthAbove = []
    wingWidthBelow = []

    i = 0

    while i < len(wingWidthThresholdPoints):
        wingWidthAbove = data[data['wing-width'] > data['wing-width'][wingWidthThresholdPoints[i]]]
        wingWidthBelow = data[data['wing-width'] <= data['wing-width'][wingWidthThresholdPoints[i]]]
        i += 1

    wingWidthAbove = wingWidthAbove.iloc[:, 3]
    wingWidthBelow = wingWidthBelow.iloc[:, 3]
    
    #print(wingWidthAbove)
    #print(wingWidthBelow)

    bodyLengthAboveEnt = calculateEntropy(bodyLengthAbove)
    bodyLengthBelowEnt = calculateEntropy(bodyLengthBelow)
    #print(bodyLengthAboveEnt)
    #print(bodyLengthBelowEnt)

    wingLengthAboveEnt = calculateEntropy(wingLengthAbove)
    wingLengthBelowEnt = calculateEntropy(wingLengthBelow)
    #print(wingLengthAboveEnt)
    #print(wingLengthBelowEnt)

    bodyWidthAboveEnt = calculateEntropy(bodyWidthAbove)
    bodyWidthBelowEnt = calculateEntropy(bodyWidthBelow)
    #print(bodyWidthAboveEnt)
    #print(bodyWidthBelowEnt)

    wingWidthAboveEnt = calculateEntropy(wingWidthAbove)
    wingWidthBelowEnt = calculateEntropy(wingWidthBelow)
    #print(wingWidthAboveEnt)
    #print(wingWidthBelowEnt)
    
    

def main():
    df = pd.read_csv("owls.csv") #reading in the data
    trainingData, testingData = splitDataIntoTrainingAndTesting(df) #splitting the data into testing and training
    globalEntropy = calculateGlobalEntropy(df)
    #print(globalEntropy)
    classes = getClasses(df)
    continous, nominal = splitDataIntoContinousAndNominal(df, classes)
    #print(continous, nominal)
    #print(classes)
    thingCont = findSplittingPointsAndSplit(continous, classes, globalEntropy)
    #thingNom = findSplittingPointsAndSplit(nominal, classes)
    

if __name__ == "__main__":
    main()
