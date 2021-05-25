groupNames = ['Eng', 'Gan', 'Fr', 'Guj', 'Indo', 'Kor', 'Rus']
#specify Group Names for Computation of Results

compItemLs = ['please', 'call', 'stella', 'ask', 'her', 'to', 'bring', 'these', 'things', 'with', 'from', 'the', 'store', 'six', 'spoons', 'of', 'fresh', 'snow', 'peas', 'five', 'thick', 'slabs', 'blue', 'cheese', 'and', 'maybe', 'a', 'snack', 'for', 'brother', 'bob', 'we', 'also', 'need', 'small', 'plastic', 'snake', 'big', 'toy', 'frog', 'kids', 'she', 'can', 'scoop', 'into', 'three', 'red', 'bags', 'will', 'go', 'meet', 'wednesday', 'at', 'train', 'station']
#List of Words in GT Provided in this case. Computation can be done without GT as well.
#Use words foung in least destructive transformation as base.
#Transformations are ordered from most to least destructive.

transList = ['Noise', 'Amp', 'Clipping', 'Drop', 'Frame', 'HP', 'LP', 'Scale']
#Comprehensive List of Transformations: Noise, Amp, Clipping, Drop,
#Frame, HP, LP, and Scale. Replace with Desired Tranformations

SNR = [2, 4, 6, 8, 10] #Parameters for Noise

amp = [0.1, 0.2, 0.3, 0.4, 0.5, 2.0] #Parameters for Amp

clipping = [0.01, 0.02, 0.03, 0.04, 0.05] #Parameters for Clipping

drop = [25, 20, 15, 10, 5] #Parameters for Drop

frame = [50, 40, 30, 20, 10] #Parameters for Frame

highpass = [900, 800, 700, 600, 500] #Parameters for HP

lowpass = [500, 600, 700, 800, 900] #Parameters for LP

scale = [0.5, 0.6, 0.7, 0.8, 0.9, 1.0] #Parameters for Scale

#Modify the transformation parameter if necessary

import re

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
    
    lenItems = len(compItemLs)
        
    fileName = 'wordCounts' + transType + '.txt'
        
    fW = open(fileName, "w")
    
    for groupSel in groupNames:
        
        fW.write(str(groupSel)+'\n')
    
        for elem in arrPar:
            
            fileA = groupSel + appChar + elem + '.txt'
            
            f1 = open(fileA, "r")
            
            lst = []
            for i in range(lenItems):
                lst.append(0)
            
            for x in f1:
                if not x[-5:-1] == '.wav':
                    
                    x = x.replace("%HESITATION", "")
                    
                    resX = re.split('[- : , ; . \s \n]',x)
                    resX[:] = [y for y in resX if y]
                    resX = [z.lower() for z in resX]
                    
                    countItem = 0
                    
                    for compItem in compItemLs:
                        
                        countNum = resX.count(compItem)
                        '''
                        if compItem in resX:  
                            lst[countItem] = lst[countItem] + 1
                        '''
                        lst[countItem] = lst[countItem] + countNum
                        countItem = countItem + 1
                                    
            f1.close()
            
            lst = [elem] + lst
            
            fW.write(str(lst)+'\n')
            
    fW.close()