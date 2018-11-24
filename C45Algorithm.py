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
    i = 0
    x = len(list(data.head(0)))
    #print(x)

    while i < x:
        print("hello")
        i += 1

def main():
    df = pd.read_csv("owls.csv") #reading in the data
    trainingData, testingData = splitDataIntoTrainingAndTesting(df) #splitting the data into testing and training
    globalEntropy = calculateGlobalEntropy(df)
    #print(globalEntropy)
    entropy = calculateEntropy(df)
    

if __name__ == "__main__":
    main()
