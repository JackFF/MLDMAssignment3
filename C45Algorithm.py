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
    #need to do some sort of splitting to get ent and info gain
    i = 0
    x = len(list(data.head(0)))
    dataFrameType = data.iloc[:, -1] #species/type
    data = data.iloc[:, 0:x-1] #rest of data, to be split into continous and nominal
    x = len(list(data.head(0)))

    continousOrNominal = {} #set that seperates the classes into continous or nominal
    for row in data.columns:
        continousOrNominal[row] = 1.*data[row].nunique()/data[row].count() < 0.05 #continous or nominal calculator

    dataFrameContinous = pd.DataFrame() #creating the empty continous & nominal dataframes
    dataFrameNominal = pd.DataFrame()
    
    for row in continousOrNominal.values():
        if row == False:
            dataFrameContinous = dataFrameContinous.append(data.iloc[:, i]) #adding to the dataframes
            i += 1
        else:
            dataFrameNominal = dataFrameNominal.append(data.iloc[:, i])
            i += 1

    dataFrameContinous = dataFrameContinous.transpose() #transposing the dataframes so they are "flipped" the right way
    datadataFrameNominal = dataFrameNominal.transpose()

    testFrame = pd.DataFrame()
    testFrame = testFrame.append(dataFrameContinous.iloc[:, 0])
    testFrame = testFrame.append(dataFrameType)
    testFrame = testFrame.transpose()
    testFrame = testFrame.sort_values(testFrame.columns[0], ascending=True)

    countOccurenecesOfValue = {} #set for the global entropy data
    for row in (testFrame.iloc[:, 0]): #itterates through the last column in the data set
        if row not in countOccurenecesOfValue: countOccurenecesOfValue[row] = 0 #adds the data to the set
        countOccurenecesOfValue[row] += 1

    for row in countOccurenecesOfValue.values()
        p = float (row) / len(testFrame.iloc[:, 0])
        #print(p)

def main():
    df = pd.read_csv("owls.csv") #reading in the data
    trainingData, testingData = splitDataIntoTrainingAndTesting(df) #splitting the data into testing and training
    globalEntropy = calculateGlobalEntropy(df)
    #print(globalEntropy)
    entropy = calculateEntropy(df)
    

if __name__ == "__main__":
    main()
