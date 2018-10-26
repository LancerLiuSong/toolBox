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
# strCSVFile = 'D:/data/TestDataset/imgSF_lidarLPI/result/report/bdAlignRep_' + sys.argv[1] + '.csv'
strCSVFile = 'D:/data/TestDataset/imgSF_lidarLPI/result/report/bdAlignRep_comb1_cad40_img0_25_off35_t10_ccoeffN.csv'
# df = pd.read_csv(sys.argv[1])
df = pd.read_csv(strCSVFile)

# print(df)

# # # Plot figure
# df[['norm2_dis_gt', 'norm2_dis_img0', 'norm2_dis_img5', 'norm2_dis_img10', 'norm2_dis_img15', 'norm2_dis_img20', 'norm2_dis_img25']].plot(figsize=(12,4))
# #strPlotFile1 = 'F1_N.png'
# #plt.savefig(strPlotFile1)
# #plt.savefig('f11.png')
# plt.show()

# df[['norm2_dis_gt', 'norm2_dis_img0', 'norm2_dis_img5', 'norm2_dis_img10', 'norm2_dis_img15', 'norm2_dis_img20', 'norm2_dis_img25']].plot(kind='kde', figsize=(8,4))
# #strPlotFile2 = 'F2_' + sys.argv[1] + '.png'
# # plt.savefig(strPlotFile2)
# # plt.savefig('f22.png')
# plt.show()

#print(df['norm2_dis_gt'].mean())

# print('Mean')
# print(df.mean())
# print('Min')
# print(df.min())
# print('Max')
# print(df.max())
# print('Std Div')
# print(df.std())

df[['norm2_dis_img0', 'norm2_dis_img5', 'norm2_dis_img10', 'norm2_dis_img15', 'norm2_dis_img20', 'norm2_dis_img25']].mean().plot(kind='line')
df[['norm2_dis_img0', 'norm2_dis_img5', 'norm2_dis_img10', 'norm2_dis_img15', 'norm2_dis_img20', 'norm2_dis_img25']].min().plot(kind='line')
df[['norm2_dis_img0', 'norm2_dis_img5', 'norm2_dis_img10', 'norm2_dis_img15', 'norm2_dis_img20', 'norm2_dis_img25']].max().plot(kind='line')
plt.show()

# df[['norm2_dis_img0', 'norm2_dis_img5', 'norm2_dis_img10', 'norm2_dis_img15', 'norm2_dis_img20', 'norm2_dis_img25']].mean().plot(kind='line')
# #df[['norm2_dis_img0', 'norm2_dis_img5', 'norm2_dis_img10', 'norm2_dis_img15', 'norm2_dis_img20', 'norm2_dis_img25']].min().plot(kind='line')
# #df[['norm2_dis_img0', 'norm2_dis_img5', 'norm2_dis_img10', 'norm2_dis_img15', 'norm2_dis_img20', 'norm2_dis_img25']].max().plot(kind='line')
# plt.show()

xList = [0, 5, 10, 15, 20, 25]
yList = df[['norm2_dis_img0', 'norm2_dis_img5', 'norm2_dis_img10', 'norm2_dis_img15', 'norm2_dis_img20', 'norm2_dis_img25']].mean()
print(yList)
plt.plot(xList, yList)
plt.show()

df.std().plot(kind='line')
plt.show()