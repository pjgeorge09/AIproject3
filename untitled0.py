# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 11:59:23 2019

@author: Peter
"""
import pandas as pd
import math
import random

def initArray(number):
    anArray = []
    for i in range(0,number):
        anArray.append(random.uniform(-0.5,0.5))
        anArray[i] = round(anArray[i],6)
    return anArray

'''A method to normalize sets of data to values [0-1]'''
def normalizeData (aDF):
    maxH = aDF['Hour'].max()
    maxV = aDF['Volts'].max()
    minH = aDF['Hour'].min()
    minV = aDF['Volts'].min()
    aDF['Hour'] = round((aDF['Hour'] - minH) / (maxH - minH),6)
    aDF['Volts'] = round((aDF['Volts'] - minV) / (maxV - minV),6)
    return aDF;

'''Maybe we should do them at random
    PP10, page 9. f = activation function
    The task is to find proper values of weight set
    (w1 w2 … wni), in order to minimize TE!'''
def linearAF (weight, data):
    alpha = 0.001
    weights = weight
    TE = 2000
    count = 1
    while (count < maxIter):
        #Do stuff       Y = AX
        TE = 0
        for i in range(0,len(data)):
            row = data[i]
            pattern = []
            for _ in row:
                pattern.append(row[_])
            x0 = 1
            x1 = pattern[0]
            xArray = []
            xArray.append(x0)
            xArray.append(x1)
            for _ in range(0,len(weights)):
                actual = ((weights[1] * x1) + weights[0])
                weights[_] += 2*alpha*(pattern[1]-actual)*xArray[_]
            
            error = (pattern[1]-((weights[1] * x1) + weights[0]))
            TE += error**2
        count +=1
    #To test, do this same thing on any 1/3rd section of the combined test data.
    TE = 0
    for i in range(0,16):
        row = data[i]
        pattern = []
        for _ in row:
            pattern.append(row[_])
        x0 = 1
        x1 = pattern[0]
        xArray = []
        xArray.append(x0)
        xArray.append(x1)
        error = (pattern[1]-((weights[1] * x1) + weights[0]))
        TE += error**2
    print("TOTAL ERROR RUN ON THE WHOLE IS " + str(TE))
    return weights

def linearAFB (weight, data):
    alpha = 0.075
    weights = weight
    TE = 2000
    count = 1
    while (count < maxIter):
        #print("Iteration " + str(count))
        #Do stuff       Y = AX
        TE = 0
        #print(str(weights) + " weights before")
        for i in range(0,len(data)):
            row = data[i]
            pattern = []
            for _ in row:
                pattern.append(row[_])
            x0 = 1
            x1 = pattern[0]
            x2 = pattern[0] ** 2
            xArray = []
            xArray.append(x0)
            xArray.append(x1)
            xArray.append(x2)
            for _ in range(0,len(weights)):
                actual = ((weights[2] * x2) + (weights[1] * x1) + weights[0])
                weights[_] += 2*alpha*(pattern[1]-actual)*xArray[_]
            
            error = (pattern[1]-((weights[2] * x2) + (weights[1] * x1) + weights[0]))
            TE += error**2
        #print("TE is " + str(TE))
        count +=1
        
    #To test, do this same thing on any 1/3rd section of the combined test data.
    TE = 0
    for i in range(32,48):
        row = data[i]
        pattern = []
        for _ in row:
            pattern.append(row[_])
        x0 = 1
        x1 = pattern[0]
        x2 = pattern[0] ** 2
        xArray = []
        xArray.append(x0)
        xArray.append(x1)
        xArray.append(x2)
        error = (pattern[1]-((weights[2]*x2) + (weights[1] * x1) + weights[0]))
        TE += error**2
    print("TOTAL ERROR RUN ON THE WHOLE IS " + str(TE))
    return weights

def linearAFC (weight, data):
    alpha = 0.08
    weights = weight
    TE = 2000
    count = 1
    while (count < maxIter):
        #print("Iteration " + str(count))
        #Do stuff       Y = AX
        TE = 0
        #print(str(weights) + " weights before")
        for i in range(0,len(data)):
            row = data[i]
            pattern = []
            for _ in row:
                pattern.append(row[_])
            x0 = 1
            x1 = pattern[0]
            x2 = pattern[0] ** 2
            x3 = pattern[0] ** 3
            xArray = []
            xArray.append(x0)
            xArray.append(x1)
            xArray.append(x2)
            xArray.append(x3)
            for _ in range(0,len(weights)):
                actual = ((weights[3] * x3) + (weights[2] * x2) + (weights[1] * x1) + weights[0])
                weights[_] += 2*alpha*(pattern[1]-actual)*xArray[_]
            error = (pattern[1] - (((weights[3] * x3) + (weights[2] * x2) + (weights[1] * x1) + weights[0])))
            TE += error**2
        #print("TE is " + str(TE))
        count +=1

    #To test, do this same thing on any 1/3rd section of the combined test data.
    TE = 0
    for i in range(15,32):
        row = data[i]
        pattern = []
        for _ in row:
            pattern.append(row[_])
        x0 = 1
        x1 = pattern[0]
        x2 = pattern[0] ** 2
        x3 = pattern[0] ** 3
        xArray = []
        xArray.append(x0)
        xArray.append(x1)
        xArray.append(x2)
        xArray.append(x3)
        error = (pattern[1]-((weights[3]*x3) + (weights[2]*x2) + (weights[1] * x1) + weights[0]))
        TE += error**2
    print("TOTAL ERROR RUN ON THE WHOLE IS " + str(TE))
    return weights


'''Create Data Objects'''
dfT1 = pd.read_csv('train_data_1.txt', header=None, names = ['Hour', 'Volts'])
dfT2 = pd.read_csv('train_data_2.txt', header=None, names = ['Hour', 'Volts'])
dfT3 = pd.read_csv('train_data_3.txt', header=None, names = ['Hour', 'Volts'])
dfT4 = pd.read_csv('test_data_4.txt' , header=None, names = ['Hour', 'Volts'])
#Just need one file for train data
dfX = pd.concat([dfT1,dfT2,dfT3], ignore_index=True)

'''Normalize Data'''
#df1_N = normalizeData(dfT1)
#df2_N = normalizeData(dfT2)
#df3_N = normalizeData(dfT3)
df4_N = normalizeData(dfT4)
dfX_N = normalizeData(dfX) #The one file for train data, normalized

'''Turn DF objects to lists for speed'''
#df1_NL = df1_N.to_dict('index')
#df2_NL = df2_N.to_dict('index')
#df3_NL = df3_N.to_dict('index')
df4_NL = df4_N.to_dict('index')
dfX_NL = dfX_N.to_dict('index')

'''Define Variables'''
maxIter = 500
weightsA = initArray(2)
weightsB = initArray(3)
weightsC = initArray(4)

eqA = linearAF(weightsA, dfX_NL)
print("------------------------------------------")
eqB = linearAFB(weightsB, dfX_NL)
print("------------------------------------------")
eqC = linearAFC(weightsC, dfX_NL)
#print(eqC)
'''Three cases to do.
    1) y= (w1)x + w0                        where x1=x
    2) y= (w2)(x2)+(w1)x + w0               where x2=(x^2)
    3) y= (w3)(x3)+(w2)(x2)+(w1)x + w0      where x3=(x^3)'''
