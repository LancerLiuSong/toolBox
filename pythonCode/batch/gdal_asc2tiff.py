import glob, os

dirPath = 'H:/BuildingDatasets/DSM/Ellenbrook/sample1'
#dirPath = 'H:/BuildingDatasets/DSM/Ellenbrook/YANDI_WD'
binaryPath = 'C:/GDAL/gdal_translate.exe'
os.chdir(dirPath)
for file in glob.glob("*.asc"):
    fullFilePathAsc = dirPath + '/' + file
    fillFilePathTiff = fullFilePathAsc[:-3] + 'tif'
    #print(fillFilePathTiff)
    strCmd = binaryPath + ' -of "GTiff" ' + fullFilePathAsc + ' ' + fillFilePathTiff
    #print(strCmd)
    os.system(strCmd)
    #os.startfile(strCmd)

# gdalbuildvrt.exe -a_srs EPSG:28350 H:/BuildingDatasets/DSM/Ellenbrook/sample1/mergedTiles.vrt H:/BuildingDatasets/DSM/Ellenbrook/sample1/*.tif
# gdal_translate.exe -of GTiff -a_srs EPSG:28350 H:/BuildingDatasets/DSM/Ellenbrook/sample1/mergedTiles.vrt H:/BuildingDatasets/DSM/Ellenbrook/sample1/mergedTiles.tif

# gdalbuildvrt.exe -a_srs EPSG:28351 H:/BuildingDatasets/DSM/Ellenbrook/sample1/mergedTiles.vrt H:/BuildingDatasets/DSM/Ellenbrook/sample1/*.tif
# gdal_translate.exe -of GTiff -a_srs EPSG:28351 H:/BuildingDatasets/DSM/Ellenbrook/sample1/mergedTiles.vrt H:/BuildingDatasets/DSM/Ellenbrook/sample1/mergedTiles.tif

# gdalbuildvrt.exe -a_srs EPSG:28356 H:/BuildingDatasets/DSM/Ellenbrook/sample1/mergedTiles.vrt H:/BuildingDatasets/DSM/Ellenbrook/sample1/*.tif
# gdal_translate.exe -of GTiff -a_srs EPSG:28356 H:/BuildingDatasets/DSM/Ellenbrook/sample1/mergedTiles.vrt H:/BuildingDatasets/DSM/Ellenbrook/sample1/mergedTiles.tif
