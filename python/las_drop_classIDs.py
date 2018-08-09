import os
import numpy as np

strDirIn = 'H:/Spectrum_Ecology/BHP Vegetation/BHP Remote Sensing Phase 2/HOMESTEAD CREEK/RGB POINT CLOUD'
strDirOut = 'H:/Spectrum_Ecology/BHP Vegetation/BHP Remote Sensing Phase 2/HOMESTEAD CREEK/RGB POINT CLOUD/unclassified'
fileExt = '.las'
binaryPath = 'D:/lib_build/LAStools_20160906/bin/las2las.exe'

if not os.path.isdir(strDirOut):
    os.mkdir(strDirOut)

for file in os.listdir(strDirIn):
    if file.endswith(fileExt):
        strFileIn = os.path.join(strDirIn, file)
        #print('Processing ' + strFileIn)
        strFileOut = os.path.join(strDirOut, file)[:-len(fileExt)] + '_unclassified.laz'
        strCmd = binaryPath + ' -i "' + strFileIn + '" -o "' + strFileOut + '" -set_classification 0'
        print(strCmd)
        os.system(strCmd)
