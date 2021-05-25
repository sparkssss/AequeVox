groupNames = ['nativeEnglish', 'nativeGanda']
#specify Group Names for Computation of Results

genFileName = 'File_Name'
#Specify filename to store results in. Recommended to use meaningful name
#Accents for groups from Accents Dataset

asrType1 = 'GCP'
asrType2 = 'MS'
#Specify Conbination of ASRs
#Available ASRs: GCP, IBM, MS

transList = ['Noise', 'Amp', 'Clipping', 'Drop', 'Frame', 'HP', 'LP', 'Scale']
#Comprehensive List of Transformations: Noise, Amp, Clipping, Drop,
#Frame, HP, LP, and Scale. Replace with Desired Tranformations

SNR = [2, 4, 6, 8, 10] #Parameters for Noise

amp = [0.1, 0.2, 0.3, 0.4, 0.5, 2.0] #Parameters for Amp

clipping = [0.01, 0.02, 0.03, 0.04, 0.05] #Parameters for Clipping

drop = [5, 10, 15, 20, 25] #Parameters for Drop

frame = [10, 20, 30, 40, 50] #Parameters for Frame

highpass = [500, 600, 700, 800, 900] #Parameters for HP

lowpass = [500, 600, 700, 800, 900] #Parameters for LP

scale = [0.5, 0.6, 0.7, 0.8, 0.9, 1.0] #Parameters for Scale

#Modify the transformation parameter if necessary

import re

import nltk

for transType in transList:

    if (transType=='Noise'):
        
        arrPar = SNR
        appChar = 'N'
    elif (transType=='Amp'):
        
        arrPar = amp
        appChar = 'A'
    elif (transType=='Clipping'):
        
        arrPar = clipping
        appChar = 'C'
    elif (transType=='Drop'):
        
        arrPar = drop
        appChar = 'D'
    elif (transType=='Frame'):
        
        arrPar = frame
        appChar = 'F'
    elif (transType=='HP'):
        
        arrPar = highpass
        appChar = 'HP'
    elif (transType=='LP'):
        
        arrPar = lowpass
        appChar = 'LP'
    elif (transType=='Scale'):
        
        arrPar = scale
        appChar = 'S'
    
    fileName = genFileName + '_' + asrType1 + '_' + asrType2 + transType + '.txt'
        
    fW = open(fileName, "w")
    
    for groupSel in groupNames:
        
        fW.write(str(groupSel)+'\n')
            
        distList = []
    
        for elem in arrPar:
            
            comp1 = []
            comp2 = []
            
            fileA = groupSel + '_' + asrType1 + '_' + appChar + str(elem) + '.txt'
            fileB = groupSel + '_' + asrType2 + '_' + appChar + str(elem) + '.txt'
            
            f1 = open(fileA, "r")
            
            for x in f1:
                if not x[-5:-1] == '.wav':
                    
                    x = x.replace("%HESITATION", "")
                    
                    resX = re.split('[- : , ; . \s \n]',x)
                    resX[:] = [y for y in resX if y]
                    resX = [z.lower() for z in resX]
                    
                    comp1.append(resX)
                    
            f1.close()
                    
            comp1 = comp1[:-1]
            
            f1 = open(fileB, "r")
            
            for x in f1:
                if not x[-5:-1] == '.wav':
                    
                    x = x.replace("%HESITATION", "")
                    
                    resX = re.split('[- : , ; . \s \n]',x)
                    resX[:] = [y for y in resX if y]
                    resX = [z.lower() for z in resX]
                    
                    comp2.append(resX)
                    
            f1.close()
            
            comp2 = comp2[:-1]
            
            sumDist = 0.0
            sumWords = 0
            
            count = 0
            
            for sen1 in comp1:
                
                sen2 = comp2[count]
                
                dist = nltk.edit_distance(sen1, sen2)
                
                len1 = len(sen1)
                len2 = len(sen2)
                
                numWords = max(len1, len2)
                
                sumDist = sumDist + dist
                sumWords = sumWords + numWords
                
                count = count + 1
                
            avgDist = sumDist/sumWords
    
            distList.append((elem, avgDist))
        
        for tup in distList:
            
            fW.write(str(tup)+'\n')
            
    fW.close()