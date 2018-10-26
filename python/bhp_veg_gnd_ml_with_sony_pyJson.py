import json
# from __future__ import division
from statistics import mean, median

# jsonFileName = "D:\\solaris_trial\\bhp_out\\HOMESTEAD CREEK\\HOMESTEAD_CREEK_vegGT.GeoJSON"
# csvFileName = "D:\\solaris_trial\\bhp_out\\HOMESTEAD CREEK\\HOMESTEAD_CREEK_vegGT_LF_features.csv"
jsonFileName = "D:\\solaris_trial\\bhp_out\\HOMESTEAD CREEK\\0_0_vegGndGT_withSony_spot_2.GeoJSON"
csvFileName = "D:\\solaris_trial\\bhp_out\\HOMESTEAD CREEK\\vegGndGT_LF_features_with_sony_spot_2.csv"

with open(jsonFileName) as f:
    data = json.load(f)

# lifeforms = ['Herb', 'Hummock Grass', 'Other Grass', 'Shrub', 'Tree']

lifeformRs = {'Ground': [], 'Herb': [], 'Hummock Grass': [], 'Other Grass': [], 'Shrub': [], 'Tree': []}
lifeformGs = {'Ground': [], 'Herb': [], 'Hummock Grass': [], 'Other Grass': [], 'Shrub': [], 'Tree': []}
lifeformBs = {'Ground': [], 'Herb': [], 'Hummock Grass': [], 'Other Grass': [], 'Shrub': [], 'Tree': []}
lifeformREs = {'Ground': [], 'Herb': [], 'Hummock Grass': [], 'Other Grass': [], 'Shrub': [], 'Tree': []}
lifeformNIRs = {'Ground': [], 'Herb': [], 'Hummock Grass': [], 'Other Grass': [], 'Shrub': [], 'Tree': []}
lifeformNDVIs = {'Ground': [], 'Herb': [], 'Hummock Grass': [], 'Other Grass': [], 'Shrub': [], 'Tree': []}
lifeformSAVIs = {'Ground': [], 'Herb': [], 'Hummock Grass': [], 'Other Grass': [], 'Shrub': [], 'Tree': []}
lifeformPNDVIs = {'Ground': [], 'Herb': [], 'Hummock Grass': [], 'Other Grass': [], 'Shrub': [], 'Tree': []}
lifeformRs_SonyRgb = {'Ground': [], 'Herb': [], 'Hummock Grass': [], 'Other Grass': [], 'Shrub': [], 'Tree': []}
lifeformGs_SonyRgb = {'Ground': [], 'Herb': [], 'Hummock Grass': [], 'Other Grass': [], 'Shrub': [], 'Tree': []}
lifeformBs_SonyRgb = {'Ground': [], 'Herb': [], 'Hummock Grass': [], 'Other Grass': [], 'Shrub': [], 'Tree': []}
lifeformBs_SonyNir = {'Ground': [], 'Herb': [], 'Hummock Grass': [], 'Other Grass': [], 'Shrub': [], 'Tree': []}
lifeformGs_SonyNir = {'Ground': [], 'Herb': [], 'Hummock Grass': [], 'Other Grass': [], 'Shrub': [], 'Tree': []}
lifeformNIRs_SonyNir = {'Ground': [], 'Herb': [], 'Hummock Grass': [], 'Other Grass': [], 'Shrub': [], 'Tree': []}
lifeformPNDVIs_SonyRgb = {'Ground': [], 'Herb': [], 'Hummock Grass': [], 'Other Grass': [], 'Shrub': [], 'Tree': []}
lifeformBNDVIs_SonyNir = {'Ground': [], 'Herb': [], 'Hummock Grass': [], 'Other Grass': [], 'Shrub': [], 'Tree': []}

# lifeformRs['Hummock Grass'].append(1)
# lifeformRs.get('Hummock Grass')

# for lf in lifeformRs:
#     if lf == 'Hummock Grass':
#         lifeformRs.get(lf).append(2)

# for lf in lifeformRs:
#     print(lifeformRs.get(lf))

for feature in data['features']:
    lifeformRs.get(feature['properties']['LIFEFORM']).append(feature['properties']['AVG_R'])
    lifeformGs.get(feature['properties']['LIFEFORM']).append(feature['properties']['AVG_G'])
    lifeformBs.get(feature['properties']['LIFEFORM']).append(feature['properties']['AVG_B'])
    lifeformREs.get(feature['properties']['LIFEFORM']).append(feature['properties']['AVG_RE'])
    lifeformNIRs.get(feature['properties']['LIFEFORM']).append(feature['properties']['AVG_NIR'])
    lifeformNDVIs.get(feature['properties']['LIFEFORM']).append(feature['properties']['AVG_NDVI'])
    lifeformSAVIs.get(feature['properties']['LIFEFORM']).append(feature['properties']['AVG_SAVI'])
    lifeformPNDVIs.get(feature['properties']['LIFEFORM']).append(feature['properties']['AVG_PNDVI'])

    lifeformRs_SonyRgb.get(feature['properties']['LIFEFORM']).append(feature['properties']['R_SonyRgb'])
    lifeformGs_SonyRgb.get(feature['properties']['LIFEFORM']).append(feature['properties']['G_SonyRgb'])
    lifeformBs_SonyRgb.get(feature['properties']['LIFEFORM']).append(feature['properties']['B_SonyRgb'])
    lifeformBs_SonyNir.get(feature['properties']['LIFEFORM']).append(feature['properties']['B_SonyNir'])
    lifeformGs_SonyNir.get(feature['properties']['LIFEFORM']).append(feature['properties']['G_SonyNir'])
    lifeformNIRs_SonyNir.get(feature['properties']['LIFEFORM']).append(feature['properties']['NIR_SonyNir'])
    lifeformPNDVIs_SonyRgb.get(feature['properties']['LIFEFORM']).append(feature['properties']['pNDVI_SonyRgb'])
    lifeformBNDVIs_SonyNir.get(feature['properties']['LIFEFORM']).append(feature['properties']['BNDVI_SonyNir'])


scvFile = open(csvFileName, 'w')

scvFile.write("%s," % ' ')

scvFile.write("%s," % 'minR')
scvFile.write("%s," % 'maxR')
scvFile.write("%s," % 'avgR')
scvFile.write("%s," % 'medianR')

scvFile.write("%s," % 'minG')
scvFile.write("%s," % 'maxG')
scvFile.write("%s," % 'avgG')
scvFile.write("%s," % 'medianG')

scvFile.write("%s," % 'minB')
scvFile.write("%s," % 'maxB')
scvFile.write("%s," % 'avgB')
scvFile.write("%s," % 'medianB')

scvFile.write("%s," % 'minRE')
scvFile.write("%s," % 'maxRE')
scvFile.write("%s," % 'avgRE')
scvFile.write("%s," % 'medianRE')

scvFile.write("%s," % 'minNIR')
scvFile.write("%s," % 'maxNIR')
scvFile.write("%s," % 'avgNIR')
scvFile.write("%s," % 'medianNIR')

scvFile.write("%s," % 'minNDVI')
scvFile.write("%s," % 'maxNDVI')
scvFile.write("%s," % 'avgNDVI')
scvFile.write("%s," % 'medianNDVI')

scvFile.write("%s," % 'minSAVI')
scvFile.write("%s," % 'maxSAVI')
scvFile.write("%s," % 'avgSAVI')
scvFile.write("%s," % 'medianSAVI')

scvFile.write("%s," % 'minPNDVI')
scvFile.write("%s," % 'maxPNDVI')
scvFile.write("%s," % 'avgPNDVI')
scvFile.write("%s," % 'medianPNDVI')

## Sony
scvFile.write("%s," % 'minR_SonyRgb')
scvFile.write("%s," % 'maxR_SonyRgb')
scvFile.write("%s," % 'avgR_SonyRgb')
scvFile.write("%s," % 'medianR_SonyRgb')

scvFile.write("%s," % 'minG_SonyRgb')
scvFile.write("%s," % 'maxG_SonyRgb')
scvFile.write("%s," % 'avgG_SonyRgb')
scvFile.write("%s," % 'medianG_SonyRgb')

scvFile.write("%s," % 'minB_SonyRgb')
scvFile.write("%s," % 'maxB_SonyRgb')
scvFile.write("%s," % 'avgB_SonyRgb')
scvFile.write("%s," % 'medianB_SonyRgb')

scvFile.write("%s," % 'minB_SonyNir')
scvFile.write("%s," % 'maxB_SonyNir')
scvFile.write("%s," % 'avgB_SonyNir')
scvFile.write("%s," % 'medianB_SonyNir')

scvFile.write("%s," % 'minG_SonyNir')
scvFile.write("%s," % 'maxG_SonyNir')
scvFile.write("%s," % 'avgG_SonyNir')
scvFile.write("%s," % 'medianG_SonyNir')

scvFile.write("%s," % 'minNIR_SonyNir')
scvFile.write("%s," % 'maxNIR_SonyNir')
scvFile.write("%s," % 'avgNIR_SonyNir')
scvFile.write("%s," % 'medianNIR_SonyNir')

scvFile.write("%s," % 'minPNDVI_SonyRgb')
scvFile.write("%s," % 'maxPNDVI_SonyRgb')
scvFile.write("%s," % 'avgPNDVI_SonyRgb')
scvFile.write("%s," % 'medianPNDVI_SonyRgb')

scvFile.write("%s," % 'minBNDVI_SonyNir')
scvFile.write("%s," % 'maxBNDVI_SonyNir')
scvFile.write("%s," % 'avgBNDVI_SonyNir')
scvFile.write("%s," % 'medianBNDVI_SonyNir')

scvFile.write("\n")

for lf in lifeformRs:
    # maxR = max(lifeformRs.get(lf))
    # minR = min(lifeformRs.get(lf))
    # avgR = sum(lifeformRs.get(lf))/len(lifeformRs.get(lf))
    # print(minR, maxR, avgR)
    minR = min(lifeformRs.get(lf))
    maxR = max(lifeformRs.get(lf))
    avgR = mean(lifeformRs.get(lf))
    medianR = median(lifeformRs.get(lf))

    minG = min(lifeformGs.get(lf))
    maxG = max(lifeformGs.get(lf))
    avgG = mean(lifeformGs.get(lf))
    medianG = median(lifeformGs.get(lf))

    minB = min(lifeformBs.get(lf))
    maxB = max(lifeformBs.get(lf))
    avgB = mean(lifeformBs.get(lf))
    medianB = median(lifeformBs.get(lf))    

    minRE = min(lifeformREs.get(lf))
    maxRE = max(lifeformREs.get(lf))
    avgRE = mean(lifeformREs.get(lf))
    medianRE = median(lifeformREs.get(lf))

    minNIR = min(lifeformNIRs.get(lf))
    maxNIR = max(lifeformNIRs.get(lf))
    avgNIR = mean(lifeformNIRs.get(lf))
    medianNIR = median(lifeformNIRs.get(lf))

    minNDVI = min(lifeformNDVIs.get(lf))
    maxNDVI = max(lifeformNDVIs.get(lf))
    avgNDVI = mean(lifeformNDVIs.get(lf))
    medianNDVI = median(lifeformNDVIs.get(lf))

    minSAVI = min(lifeformSAVIs.get(lf))
    maxSAVI = max(lifeformSAVIs.get(lf))
    avgSAVI = mean(lifeformSAVIs.get(lf))
    medianSAVI = median(lifeformSAVIs.get(lf))

    minPNDVI = min(lifeformPNDVIs.get(lf))
    maxPNDVI = max(lifeformPNDVIs.get(lf))
    avgPNDVI = mean(lifeformPNDVIs.get(lf))
    medianPNDVI = median(lifeformPNDVIs.get(lf))

    ## Sony
    minR_SonyRgb = min(lifeformRs_SonyRgb.get(lf))
    maxR_SonyRgb = max(lifeformRs_SonyRgb.get(lf))
    avgR_SonyRgb = mean(lifeformRs_SonyRgb.get(lf))
    medianR_SonyRgb = median(lifeformRs_SonyRgb.get(lf))

    minG_SonyRgb = min(lifeformGs_SonyRgb.get(lf))
    maxG_SonyRgb = max(lifeformGs_SonyRgb.get(lf))
    avgG_SonyRgb = mean(lifeformGs_SonyRgb.get(lf))
    medianG_SonyRgb = median(lifeformGs_SonyRgb.get(lf))

    minB_SonyRgb = min(lifeformBs_SonyRgb.get(lf))
    maxB_SonyRgb = max(lifeformBs_SonyRgb.get(lf))
    avgB_SonyRgb = mean(lifeformBs_SonyRgb.get(lf))
    medianB_SonyRgb = median(lifeformBs_SonyRgb.get(lf))

    minB_SonyNir = min(lifeformBs_SonyNir.get(lf))
    maxB_SonyNir = max(lifeformBs_SonyNir.get(lf))
    avgB_SonyNir = mean(lifeformBs_SonyNir.get(lf))
    medianB_SonyNir = median(lifeformBs_SonyNir.get(lf))

    minG_SonyNir = min(lifeformGs_SonyNir.get(lf))
    maxG_SonyNir = max(lifeformGs_SonyNir.get(lf))
    avgG_SonyNir = mean(lifeformGs_SonyNir.get(lf))
    medianG_SonyNir = median(lifeformGs_SonyNir.get(lf))

    minNIR_SonyNir = min(lifeformNIRs_SonyNir.get(lf))
    maxNIR_SonyNir = max(lifeformNIRs_SonyNir.get(lf))
    avgNIR_SonyNir = mean(lifeformNIRs_SonyNir.get(lf))
    medianNIR_SonyNir = median(lifeformNIRs_SonyNir.get(lf))

    minPNDVI_SonyRgb = min(lifeformPNDVIs_SonyRgb.get(lf))
    maxPNDVI_SonyRgb = max(lifeformPNDVIs_SonyRgb.get(lf))
    avgPNDVI_SonyRgb = mean(lifeformPNDVIs_SonyRgb.get(lf))
    medianPNDVI_SonyRgb = median(lifeformPNDVIs_SonyRgb.get(lf))

    minBNDVI_SonyNir = min(lifeformBNDVIs_SonyNir.get(lf))
    maxBNDVI_SonyNir = max(lifeformBNDVIs_SonyNir.get(lf))
    avgBNDVI_SonyNir = mean(lifeformBNDVIs_SonyNir.get(lf))
    medianBNDVI_SonyNir = median(lifeformBNDVIs_SonyNir.get(lf))

    # print(minR, maxR, avgR, medianR)
    scvFile.write("%s," % lf)

    scvFile.write("%f," % minR)
    scvFile.write("%f," % maxR)
    scvFile.write("%f," % avgR)
    scvFile.write("%f," % medianR)    
    
    scvFile.write("%f," % minG)
    scvFile.write("%f," % maxG)
    scvFile.write("%f," % avgG)
    scvFile.write("%f," % medianG)

    scvFile.write("%f," % minB)
    scvFile.write("%f," % maxB)
    scvFile.write("%f," % avgB)
    scvFile.write("%f," % medianB)

    scvFile.write("%f," % minRE)
    scvFile.write("%f," % maxRE)
    scvFile.write("%f," % avgRE)
    scvFile.write("%f," % medianRE)

    scvFile.write("%f," % minNIR)
    scvFile.write("%f," % maxNIR)
    scvFile.write("%f," % avgNIR)
    scvFile.write("%f," % medianNIR)

    scvFile.write("%f," % minNDVI)
    scvFile.write("%f," % maxNDVI)
    scvFile.write("%f," % avgNDVI)
    scvFile.write("%f," % medianNDVI)

    scvFile.write("%f," % minSAVI)
    scvFile.write("%f," % maxSAVI)
    scvFile.write("%f," % avgSAVI)
    scvFile.write("%f," % medianSAVI)

    scvFile.write("%f," % minPNDVI)
    scvFile.write("%f," % maxPNDVI)
    scvFile.write("%f," % avgPNDVI)
    scvFile.write("%f," % medianPNDVI)

    scvFile.write("%f," % minR_SonyRgb)
    scvFile.write("%f," % maxR_SonyRgb)
    scvFile.write("%f," % avgR_SonyRgb)
    scvFile.write("%f," % medianR_SonyRgb)

    scvFile.write("%f," % minG_SonyRgb)
    scvFile.write("%f," % maxG_SonyRgb)
    scvFile.write("%f," % avgG_SonyRgb)
    scvFile.write("%f," % medianG_SonyRgb)

    scvFile.write("%f," % minB_SonyRgb)
    scvFile.write("%f," % maxB_SonyRgb)
    scvFile.write("%f," % avgB_SonyRgb)
    scvFile.write("%f," % medianB_SonyRgb)

    scvFile.write("%f," % minB_SonyNir)
    scvFile.write("%f," % maxB_SonyNir)
    scvFile.write("%f," % avgB_SonyNir)
    scvFile.write("%f," % medianB_SonyNir)

    scvFile.write("%f," % minG_SonyNir)
    scvFile.write("%f," % maxG_SonyNir)
    scvFile.write("%f," % avgG_SonyNir)
    scvFile.write("%f," % medianG_SonyNir)

    scvFile.write("%f," % minNIR_SonyNir)
    scvFile.write("%f," % maxNIR_SonyNir)
    scvFile.write("%f," % avgNIR_SonyNir)
    scvFile.write("%f," % medianNIR_SonyNir)

    scvFile.write("%f," % minPNDVI_SonyRgb)
    scvFile.write("%f," % maxPNDVI_SonyRgb)
    scvFile.write("%f," % avgPNDVI_SonyRgb)
    scvFile.write("%f," % medianPNDVI_SonyRgb)

    scvFile.write("%f," % minBNDVI_SonyNir)
    scvFile.write("%f," % maxBNDVI_SonyNir)
    scvFile.write("%f," % avgBNDVI_SonyNir)
    scvFile.write("%f," % medianBNDVI_SonyNir)

    scvFile.write("\n")




scvFile.close()


