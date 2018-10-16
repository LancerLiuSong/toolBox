import json
# from __future__ import division
from statistics import mean, median

# jsonFileName = "D:\\solaris_trial\\bhp_out\\HOMESTEAD CREEK\\HOMESTEAD_CREEK_vegGT.GeoJSON"
# csvFileName = "D:\\solaris_trial\\bhp_out\\HOMESTEAD CREEK\\HOMESTEAD_CREEK_vegGT_LF_features.csv"
jsonFileName = "D:\\solaris_trial\\bhp_out\\HOMESTEAD CREEK\\0_0_vegGndGT.GeoJSON"
csvFileName = "D:\\solaris_trial\\bhp_out\\HOMESTEAD CREEK\\0_0_vegGndGT_LF_features.csv"

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

    scvFile.write("\n")




scvFile.close()


