# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 11:59:23 2019

@author: Peter
"""
import pandas as pd

'''A method to normalize sets of data to values [0-1]'''
def normalizeData (aDF):
    maxH = aDF['Hour'].max()
    maxV = aDF['Volts'].max()
    minH = aDF['Hour'].min()
    minV = aDF['Volts'].min()
    aDF['Hour'] = round((aDF['Hour'] - minH) / (maxH - minH),6)
    aDF['Volts'] = round((aDF['Volts'] - minV) / (maxV - minV),6)
    return aDF;

'''Maybe we should do them at random'''
def linearAF (data):
    #weightsMaybe = data[0]
    count = len(data)
    while (count > 0):
        #Do stuff       Y = AX
        print("")
        
    
    return

'''Create Data Objects'''
dfT1 = pd.read_csv('train_data_1.txt', header=None, names = ['Hour', 'Volts'])
dfT2 = pd.read_csv('train_data_2.txt', header=None, names = ['Hour', 'Volts'])
dfT3 = pd.read_csv('train_data_3.txt', header=None, names = ['Hour', 'Volts'])
dfT4 = pd.read_csv('test_data_4.txt' , header=None, names = ['Hour', 'Volts'])

'''Normalize Data'''
df1_N = normalizeData(dfT1)
df2_N = normalizeData(dfT2)
df3_N = normalizeData(dfT3)
df4_N = normalizeData(dfT4)

'''Turn DF objects to lists for speed'''
df1_NL = df1_N.to_dict('index')
df2_NL = df2_N.to_dict('index')
df3_NL = df3_N.to_dict('index')
df4_NL = df4_N.to_dict('index')

'''Three cases to do.
    1) y= (w1)x + w0                        where x1=x
    2) y= (w2)(x2)+(w1)x + w0               where x2=(x^2)
    3) y= (w3)(x3)+(w2)(x2)+(w1)x + w0      where x3=(x^3)'''
