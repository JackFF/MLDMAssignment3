import pandas as pd
import numpy as np
import random as rnd
import math

def splitDataIntoTrainingAndTesting(data):
    train = data.sample(frac=(2/3), random_state=200) #split the data randomly by 2/3
    test = data.drop(train.index) #let testing data equal to data not used in the training data

    return train, test #returns training and testing data

def calculateEntropy(data):
    #get in data, get headings, easy to do list(.head(1)) or something like that
    #count how many columns then seperate them
    #iterate through and count how many answers there are
    #add up and caculate entropy
    classes = list(data.head(0))
    print(classes[0])
    print(len(classes))
    x = len(classes)
    i = 0
    while i < x:
        print("hello")
        print(data.iloc[:, i]) #prints each column out, must make it do something now
        i = i + 1

def main():
    df = pd.read_csv("owls.csv") #reading in the data
    trainingData, testingData = splitDataIntoTrainingAndTesting(df) #splitting the data into testing and training
    entropy = calculateEntropy(df)
    

if __name__ == "__main__":
    main()
