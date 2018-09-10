import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sys

strCSVFile = './checkT.csv'
df = pd.read_csv(strCSVFile)

#print(df[['Y', 'Y_hat']])

Y = df['Y']
Y_hat = df['Y_hat']

# print(Y.shape)
# print(Y)
# print("=======================")
# print(Y_hat.shape)
# print(Y_hat)

# Ys = df[['Y', 'Y_hat']]
# print(Ys.shape)
# print(Ys)

# for y in Ys:
#     #print(y[0] + "~" + y[1])
#     print(y)

AllP = 0.0
AllSP = 0.0
TP = 0.0

for i in range(len(Y)):
    print(Y[i], '_', Y_hat[i])
    if Y_hat[i] == 1:
        AllP += 1.0
    if Y[i] == 1:
        AllSP += 1.0
    if Y[i] == 1 and Y_hat[i] == 1:
        TP += 1.0

p = TP / AllP
r = TP / AllSP

f1 = 2 * (p * r) / (p + r)

print("AllP:", AllP)
print("AllSP:", AllSP)
print("TP:", TP)

print("p:", p)
print("r:", r)
print("f1:", f1)
