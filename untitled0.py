# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 11:59:23 2019
@author: Peter
"""
import pandas as pd
import numpy as np
import math
import random
import matplotlib.pyplot as plt

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
def linearAF (weights, data):
    alpha = 0.001
    TE = 2000
    count = 1
    while (count < maxIter):
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
    return weights

def linearAFB (weights, data):
    alpha = 0.001
    TE = 2000
    count = 1
    while (count < maxIter):
        TE = 0
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
        count +=1
    return weights

def linearAFC (weights, data):
    alpha = 0.05
    TE = 2000
    count = 1
    while (count < maxIter):
        TE = 0
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
        count +=1
    return weights

def report(eq, actual):
    TE = 0
    while(len(eq) < 4):
        eq.append(0)
    hours = []
    for _ in dfHours:
        hours.append(_)
    for i in range(0,len(hours)):
        row = actual[i]
        pattern = []
        for _ in row:
            pattern.append(row[_])
        x = [1, pattern[0], pattern[0] **2, pattern[0] **3]
        error = (pattern[1]-((eq[3]*x[3]) + (eq[2]*x[2]) + (eq[1] * x[1]) + eq[0]))
        TE += error**2
    return round(TE, 4)
    
def plotIt(dayHours, dayVolts, graphTitle, weights):
    plt.plot(dayHours, dayVolts,'+', color = 'black', label = "Given Data")    
    values = []
    for _ in dayHours:
        values.append(_)
    yData = []
    for x in values:
        y = 0
        for i in range(0,len(weights)):
            y += weights[i] * (x**i)
        yData.append(float(y))
    plt.plot(values, yData, 'o', color='blue', markersize=3)
    plt.plot(values, yData, '-', color='blue', linewidth=1, label = "Predicted Line")
    plt.xlabel('Hour, normalized')
    plt.ylabel('Volts, normalized')
    plt.title(graphTitle, loc='center')
    plt.legend();
    plt.show()
    return

def makeplot(norm_DF, weights, title):
    l_dayHours = norm_DF['Hour']
    l_dayVolts = norm_DF['Volts']
    plotIt(l_dayHours, l_dayVolts,title, weights)
    return

'''Create Data Objects'''
dfT1 = pd.read_csv('train_data_1.txt', header=None, names = ['Hour', 'Volts'])
dfT2 = pd.read_csv('train_data_2.txt', header=None, names = ['Hour', 'Volts'])
dfT3 = pd.read_csv('train_data_3.txt', header=None, names = ['Hour', 'Volts'])
dfT4 = pd.read_csv('test_data_4.txt' , header=None, names = ['Hour', 'Volts'])
#Just need one file for train data
dfX = pd.concat([dfT1,dfT2,dfT3], ignore_index=True)

'''Normalize Data'''
df1_N = normalizeData(dfT1)
df2_N = normalizeData(dfT2)
df3_N = normalizeData(dfT3)
df4_N = normalizeData(dfT4)
dfX_N = normalizeData(dfX) #The one file for train data, normalized

dfHours = df1_N['Hour']

'''Turn DF objects to lists for speed'''
df1_NL = df1_N.to_dict('index')
df2_NL = df2_N.to_dict('index')
df3_NL = df3_N.to_dict('index')
df4_NL = df4_N.to_dict('index')
dfX_NL = dfX_N.to_dict('index')

'''Define Variables'''
maxIter = 10000
weightsA = initArray(2)
weightsB = initArray(3)
weightsC = initArray(4)

'''Equations built by training on all 3 days at one time'''
eqA = linearAF(weightsA, dfX_NL)
eqB = linearAFB(weightsB, dfX_NL)
eqC = linearAFC(weightsC, dfX_NL)

'''Plot the data '''
makeplot(df1_N, eqA, "Linear Training (a) on Day 1");
makeplot(df2_N, eqA, "Linear Training (a) on Day 2");
makeplot(df3_N, eqA, "Linear Training (a) on Day 3");
makeplot(df4_N, eqA, "Linear Testing (a) on Day 4");

makeplot(df1_N, eqB, "Quadratic Training (b) on Day 1");
makeplot(df2_N, eqB, "Quadratic Training (b) on Day 2");
makeplot(df3_N, eqB, "Quadratic Training (b) on Day 3");
makeplot(df4_N, eqB, "Quadratic Testing (b) on Day 4");

makeplot(df1_N, eqC, "Cubic Training (c) on Day 1");
makeplot(df2_N, eqC, "Cubic Training (c) on Day 2");
makeplot(df3_N, eqC, "Cubic Training (c) on Day 3");
makeplot(df4_N, eqC, "Cubic Testing (c) on Day 4");

'''Report the errors'''
# DF object to hold all the error percents
reports = [[report(eqA, df1_NL), report(eqB, df1_NL), report(eqC, df1_NL)],
          [report(eqA, df2_NL), report(eqB, df2_NL), report(eqC, df2_NL)],
          [report(eqA, df3_NL), report(eqB, df3_NL), report(eqC, df3_NL)],
          [report(eqA, df4_NL), report(eqB, df4_NL), report(eqC, df4_NL)]]
errorDF = pd.DataFrame(reports, columns = ['Linear TE (a)', 'Quadratic TE (b)', 'Cubic TE (c)'])
errorDF.index = np.arange(1, len(errorDF)+1)
print(errorDF)