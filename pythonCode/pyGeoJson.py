import json

jsonFileName = "H:/solarDemo/output/mock/0_0_solarRoofsBaseN.GeoJSON"
csvFileName = "H:/solarDemo/output/mock/0_0_solarRoofsBaseN.csv"

with open(jsonFileName) as f:
    data = json.load(f)

#print(data['features'][0]['properties']['M1'])

for feature in data['features']:
    print(feature['properties']['ALTITUDE'])
    






    #print(feature['geometry']['type'])
    #print(feature['geometry']['coordinates'])
    #for property in feature