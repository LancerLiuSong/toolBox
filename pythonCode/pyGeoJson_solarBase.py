import json

jsonFileName = "H:/solarDemo/output/mock/0_0_solarRoofsBaseS.GeoJSON"
csvFileName = "H:/solarDemo/output/mock/csv/solarRoofBaseS_month.csv"
csvHourSummerFileName = "H:/solarDemo/output/mock/csv/solarRoofBaseS_hour_summer.csv"
csvHourEquinoxFileName = "H:/solarDemo/output/mock/csv/solarRoofBaseS_hour_equinox.csv"
csvHourWinterFileName = "H:/solarDemo/output/mock/csv/solarRoofBaseS_hour_winter.csv"

with open(jsonFileName) as f:
    data = json.load(f)

scvFile = open(csvFileName, 'w')
scvSummerFile = open(csvHourSummerFileName, 'w')
scvEquinoxFile = open(csvHourEquinoxFileName, 'w')
scvWinterFile = open(csvHourWinterFileName, 'w')

### Write 1st line
scvFile.write(" ,")
scvFile.write("M1,")
scvFile.write("M2,")
scvFile.write("M3,")
scvFile.write("M4,")
scvFile.write("M5,")
scvFile.write("M6,")
scvFile.write("M7,")
scvFile.write("M8,")
scvFile.write("M9,")
scvFile.write("M10,")
scvFile.write("M11,")
scvFile.write("M12,")
scvFile.write("\n")

scvSummerFile.write(" ,")
scvSummerFile.write("H6,")
scvSummerFile.write("H7,")
scvSummerFile.write("H8,")
scvSummerFile.write("H9,")
scvSummerFile.write("H10,")
scvSummerFile.write("H11,")
scvSummerFile.write("H12,")
scvSummerFile.write("H13,")
scvSummerFile.write("H14,")
scvSummerFile.write("H15,")
scvSummerFile.write("H16,")
scvSummerFile.write("H17,")
scvSummerFile.write("H18,")
scvSummerFile.write("\n")

scvEquinoxFile.write(" ,")
scvEquinoxFile.write("H6,")
scvEquinoxFile.write("H7,")
scvEquinoxFile.write("H8,")
scvEquinoxFile.write("H9,")
scvEquinoxFile.write("H10,")
scvEquinoxFile.write("H11,")
scvEquinoxFile.write("H12,")
scvEquinoxFile.write("H13,")
scvEquinoxFile.write("H14,")
scvEquinoxFile.write("H15,")
scvEquinoxFile.write("H16,")
scvEquinoxFile.write("H17,")
scvEquinoxFile.write("H18,")
scvEquinoxFile.write("\n")

scvWinterFile.write(" ,")
scvWinterFile.write("H6,")
scvWinterFile.write("H7,")
scvWinterFile.write("H8,")
scvWinterFile.write("H9,")
scvWinterFile.write("H10,")
scvWinterFile.write("H11,")
scvWinterFile.write("H12,")
scvWinterFile.write("H13,")
scvWinterFile.write("H14,")
scvWinterFile.write("H15,")
scvWinterFile.write("H16,")
scvWinterFile.write("H17,")
scvWinterFile.write("H18,")
scvWinterFile.write("\n")


for feature in data['features']:
    #print(feature['properties']['ALTITUDE'])
    #alt.append(feature['properties']['ALTITUDE'])
    #m1.append(feature['properties']['M1'])
    #scvFile.write("%f," % feature['properties']['ALTITUDE'])
    
    ### Monthly
    scvFile.write("Pitch_%d," % feature['properties']['ALTITUDE'])
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
    scvSummerFile.write("Pitch_%d," % feature['properties']['ALTITUDE'])
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

    ### Hourly Equinox
    scvEquinoxFile.write("Pitch_%d," % feature['properties']['ALTITUDE'])
    scvEquinoxFile.write("%f," % feature['properties']['H3_6'])
    scvEquinoxFile.write("%f," % feature['properties']['H3_7'])
    scvEquinoxFile.write("%f," % feature['properties']['H3_8'])
    scvEquinoxFile.write("%f," % feature['properties']['H3_9'])
    scvEquinoxFile.write("%f," % feature['properties']['H3_10'])
    scvEquinoxFile.write("%f," % feature['properties']['H3_11'])
    scvEquinoxFile.write("%f," % feature['properties']['H3_12'])
    scvEquinoxFile.write("%f," % feature['properties']['H3_13'])
    scvEquinoxFile.write("%f," % feature['properties']['H3_14'])
    scvEquinoxFile.write("%f," % feature['properties']['H3_15'])
    scvEquinoxFile.write("%f," % feature['properties']['H3_16'])
    scvEquinoxFile.write("%f," % feature['properties']['H3_17'])
    scvEquinoxFile.write("%f," % feature['properties']['H3_18'])
    scvEquinoxFile.write("\n")

    ### Hourly Winter
    scvWinterFile.write("Pitch_%d," % feature['properties']['ALTITUDE'])
    scvWinterFile.write("%f," % feature['properties']['H6_6'])
    scvWinterFile.write("%f," % feature['properties']['H6_7'])
    scvWinterFile.write("%f," % feature['properties']['H6_8'])
    scvWinterFile.write("%f," % feature['properties']['H6_9'])
    scvWinterFile.write("%f," % feature['properties']['H6_10'])
    scvWinterFile.write("%f," % feature['properties']['H6_11'])
    scvWinterFile.write("%f," % feature['properties']['H6_12'])
    scvWinterFile.write("%f," % feature['properties']['H6_13'])
    scvWinterFile.write("%f," % feature['properties']['H6_14'])
    scvWinterFile.write("%f," % feature['properties']['H6_15'])
    scvWinterFile.write("%f," % feature['properties']['H6_16'])
    scvWinterFile.write("%f," % feature['properties']['H6_17'])
    scvWinterFile.write("%f," % feature['properties']['H6_18'])
    scvWinterFile.write("\n")

scvFile.close()
scvSummerFile.close()
scvEquinoxFile.close()
scvWinterFile.close()