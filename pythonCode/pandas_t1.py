import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sys

# print(len(sys.argv))
# # print(sys.argv)
# print(sys.argv[0])
# print(sys.argv[1])

# Load CSV to data frame
# df = pd.read_csv('D:/data/TestDataset/imgSF_lidarLPI/result/report/bdAlignRep_cad50_img25_off4.csv')
strCSVFile = 'D:/data/TestDataset/imgSF_lidarLPI/result/report/bdAlignRep_' + sys.argv[1] + '.csv'
# df = pd.read_csv(sys.argv[1])
df = pd.read_csv(strCSVFile)

# # Plot figure
df[['norm2_dis_gt', 'norm2_dis']].plot(figsize=(12,4))
strPlotFile1 = 'F1_' + sys.argv[1] + '.png'
plt.savefig(strPlotFile1)
# plt.savefig('f11.png')

df[['norm2_dis_gt', 'norm2_dis']].plot(kind='kde', figsize=(8,4))
strPlotFile2 = 'F2_' + sys.argv[1] + '.png'
plt.savefig(strPlotFile2)
# plt.savefig('f22.png')

#print(df['norm2_dis_gt'].mean())
print('Mean')
print(df.mean())
print('Min')
print(df.min())
print('Max')
print(df.max())
print('Std Div')
print(df.std())

