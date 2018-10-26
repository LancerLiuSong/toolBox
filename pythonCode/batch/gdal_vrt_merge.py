import glob, os

dirPath = 'H:/BuildingDatasets/DSM/Ellenbrook/sample1'
vrtBinaryPath = 'C:/GDAL/gdalbuildvrt.exe'
mergeBinaryPath = 'C:/GDAL/gdal_translate.exe'

#gdalbuildvrt -a_srs EPSG:28350 out.vrt *.tif
#gdal_translate -of GTiff -a_srs EPSG:28356 in.vrt  out.tif
strVrtCmd = vrtBinaryPath + ' -a_srs EPSG:28350 ' + dirPath + '/mergedTiles.vrt ' + dirPath + '/*.tif'
strMergeCmd = mergeBinaryPath + ' -of GTiff -a_srs EPSG:28350 ' + dirPath + '/mergedTiles.vrt ' + dirPath + '/mergedTiles.tif'
strMergeCmd2 = mergeBinaryPath + ' -of GTiff -a_srs EPSG:28350 ' + dirPath + '/*.tif ' + dirPath + '/mergedTiles.tif'

print (strVrtCmd)
print (strMergeCmd)

# os.system(strVrtCmd)
# os.system(strMergeCmd)
# os.system(strMergeCmd2)

# os.chdir(dirPath)
# for file in glob.glob("*.asc"):
#     fullFilePathAsc = dirPath + '/' + file
#     fillFilePathTiff = fullFilePathAsc[:-3] + 'tif'
#     #print(fillFilePathTiff)
#     strCmd = binaryPath + ' -of "GTiff" ' + fullFilePathAsc + ' ' + fillFilePathTiff
#     #print(strCmd)
#     os.system(strCmd)
#     #os.startfile(strCmd)

