import json

jsonFileName = "../data/0_0_solarRoofsBaseN.GeoJSON"
csvFileName = "../data/solarRoofBaseN_month.csv"
csvHourSummerFileName = "../data/solarRoofBaseN_hour_summer.csv"
csvHourEquinoxFileName = "../data/solarRoofBaseN_hour_equinox.csv"
csvHourWinterFileName = "../data/solarRoofBaseN_hour_winter.csv"

with open(jsonFileName) as f:
    data = json.load(f)

#alt = []
#m1 = []

scvFile = open(csvFileName, 'w')
scvSummerFile = open(csvHourSummerFileName, 'w') 


for feature in data['features']:
    #print(feature['properties']['ALTITUDE'])
    #alt.append(feature['properties']['ALTITUDE'])
    #m1.append(feature['properties']['M1'])
    #scvFile.write("%f," % feature['properties']['ALTITUDE'])
    
    ### Monthly
    scvFile.write("%f," % feature['properties']['M1'])
    scvFile.write("%f," % feature['properties']['M2'])
    scvFile.write("%f," % feature['properties']['M3'])
    scvFile.write("%f," % feature['properties']['M4'])
    scvFile.write("%f," % feature['properties']['M5'])
    scvFile.write("%f," % feature['properties']['M6'])
    scvFile.write("%f," % feature['properties']['M7'])
    scvFile.write("%f," % feature['properties']['M8'])
    scvFile.write("%f," % feature['properties']['M9'])
    scvFile.write("%f," % feature['properties']['M10'])
    scvFile.write("%f," % feature['properties']['M11'])
    scvFile.write("%f," % feature['properties']['M12'])
    scvFile.write("\n")
    
    ### Hourly Summer
    scvSummerFile.write("%f," % feature['properties']['H12_6'])
    scvSummerFile.write("%f," % feature['properties']['H12_7'])
    scvSummerFile.write("%f," % feature['properties']['H12_8'])
    scvSummerFile.write("%f," % feature['properties']['H12_9'])
    scvSummerFile.write("%f," % feature['properties']['H12_10'])
    scvSummerFile.write("%f," % feature['properties']['H12_11'])
    scvSummerFile.write("%f," % feature['properties']['H12_12'])
    scvSummerFile.write("%f," % feature['properties']['H12_13'])
    scvSummerFile.write("%f," % feature['properties']['H12_14'])
    scvSummerFile.write("%f," % feature['properties']['H12_15'])
    scvSummerFile.write("%f," % feature['properties']['H12_16'])
    scvSummerFile.write("%f," % feature['properties']['H12_17'])
    scvSummerFile.write("%f," % feature['properties']['H12_18'])
    scvSummerFile.write("\n")


    
    
    
    
    
scvFile.close()
scvSummerFile.close()
    
    
#for val in alt:
#    print("Alt:", val)
