asrType1 = 'GCP'
asrType2 = 'IBM'
#Specify Conbination of ASRs
#Available ASRs: GCP, IBM, MS

configText = 'CONFIG.txt'

fConfig = open(configText, "r")

while True:
    
    line = fConfig.readline()
    
    if not line:
        break
    
    words = line[:-1]
        
    if words.startswith('SNR'):
        
        start = words.find('[') + 1
        
        end = words.find(']')
        
        intWords = words[start:end]
        
        resWords = intWords.split(',')
        
        resWords = [int(i) for i in resWords]
        
        SNR = resWords
        
    if words.startswith('amp'):
        
        start = words.find('[') + 1
        
        end = words.find(']')
        
        intWords = words[start:end]
        
        resWords = intWords.split(',')
        
        resWords = [float(i) for i in resWords]
        
        amp = resWords
        
    if words.startswith('clipping'):
        
        start = words.find('[') + 1
        
        end = words.find(']')
        
        intWords = words[start:end]
        
        resWords = intWords.split(',')
        
        resWords = [float(i) for i in resWords]
        
        clipping = resWords
        
    if words.startswith('drop'):
        
        start = words.find('[') + 1
        
        end = words.find(']')
        
        intWords = words[start:end]
        
        resWords = intWords.split(',')
        
        resWords = [int(i) for i in resWords]
        
        drop = resWords
        
    if words.startswith('frame'):
        
        start = words.find('[') + 1
        
        end = words.find(']')
        
        intWords = words[start:end]
        
        resWords = intWords.split(',')
        
        resWords = [int(i) for i in resWords]
        
        frame = resWords
        
    if words.startswith('highpass'):
        
        start = words.find('[') + 1
        
        end = words.find(']')
        
        intWords = words[start:end]
        
        resWords = intWords.split(',')
        
        resWords = [int(i) for i in resWords]
        
        highpass = resWords
        
    if words.startswith('lowpass'):
        
        start = words.find('[') + 1
        
        end = words.find(']')
        
        intWords = words[start:end]
        
        resWords = intWords.split(',')
        
        resWords = [int(i) for i in resWords]
        
        lowpass = resWords
        
    if words.startswith('scale'):
        
        start = words.find('[') + 1
        
        end = words.find(']')
        
        intWords = words[start:end]
        
        resWords = intWords.split(',')
        
        resWords = [float(i) for i in resWords]
        
        scale = resWords
        
    if words.startswith('groupNames'):
        
        intWordInd = words.find('\'')
        
        intWords = words[intWordInd:]
        
        resWords = intWords.split(',')
        
        newResWords = []
        
        for resWord in resWords:
            
            start = resWord.find('\'') + 1
            resWord = resWord[start:]
            end = resWord.find('\'')
            resWord = resWord[:end]
            
            newResWords.append(resWord)
            
        resWords = newResWords
        
        groupNames = resWords
        
    if words.startswith('transList'):
        
        intWordInd = words.find('\'')
        
        intWords = words[intWordInd:]
        
        resWords = intWords.split(',')
        
        newResWords = []
        
        for resWord in resWords:
            
            start = resWord.find('\'') + 1
            resWord = resWord[start:]
            end = resWord.find('\'')
            resWord = resWord[:end]
            
            newResWords.append(resWord)
            
        resWords = newResWords
        
        transList = resWords
        
    if words.startswith('datasetName'):
        
        intWordInd = words.find('\'')
        
        intWords = words[intWordInd+1:]
        
        end = intWords.find('\'')
        
        resWords = intWords[:end]
        
        datasetName = resWords
        
fConfig.close()

'''

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

'''

import csv

for transType in transList:
    
    if (transType=='Noise'):
        
        arrPar = SNR
    elif (transType=='Amp'):
        
        arrPar = amp
    elif (transType=='Clipping'):
        
        arrPar = clipping
    elif (transType=='Drop'):
        
        arrPar = drop
    elif (transType=='Frame'):
        
        arrPar = frame
    elif (transType=='HP'):
        
        arrPar = highpass
    elif (transType=='LP'):
        
        arrPar = lowpass
    elif (transType=='Scale'):
        
        arrPar = scale

    fileName = datasetName + '_' + asrType1 + '_' + asrType2 + transType + '.txt'
    #File_Name_GCP_MSNoise.txt
    
    writeFile = asrType1 + "_" +asrType2 + " Differential Speech Results - " + transType + '.csv'
    
    with open(writeFile, 'w', encoding='UTF8', newline='') as fW:
    
        writer = csv.writer(fW)
        
        firstRow = ['']
        
        count = 1
        
        for group in groupNames:
            
            count = count + 1
            
            firstRow.append(group)
            
        writer.writerow(firstRow)
        
        for elem in arrPar:
            
            rowVal = [elem]
            
            for group in groupNames:
                
                fR = open(fileName, "r")
                
                groupCheck = False
                loopCheck = True
                
                while loopCheck:
                    
                    # Get next line from file
                    line = fR.readline()
                    
                    if not line:
                        break
                    
                    words = line[:-1]
                    
                    if (words==group):
                        
                        groupCheck = True
                        
                    if (words!=group) and groupCheck:
                        
                        indVal = words[1:-1].split(",")[0]
                                  
                        if (str(elem)==indVal):
                            
                            actDist = (words[1:-1].split(","))[-1]
                            
                            rowVal.append(float(actDist))
                            
                            loopCheck = False
                            
                            fR.close()
                            
            writer.writerow(rowVal)
            
        intRow = ([''] * count)
        writer.writerow(intRow)
        
        orgRow = ['Original']
        
        fScaleName = datasetName + '_' + asrType1 + '_' + asrType2 + 'Scale' + '.txt'
        
        for group in groupNames:
            
            fR = open(fScaleName, "r")
            
            groupCheck = False
            loopCheck = True
            
            while loopCheck:
                
                # Get next line from file
                line = fR.readline()
                
                if not line:
                    break
                
                words = line[:-1]
                
                if (words==group):
                    
                    groupCheck = True
                    
                if ((words!=group) and groupCheck):
                    
                    indVal = words[1:-1].split(",")[0]
                              
                    if (indVal=='1.0'):
                        
                        actDist = words[1:-1].split(",")[-1]
                        
                        orgRow.append(float(actDist))
                        
                        loopCheck = False
                        
                        fR.close()
                        
        writer.writerow(orgRow)
        writer.writerow(intRow)
        
        diffRow = 'Differences'
        
        for group in groupNames:
            
            diffRow.append('')
            
        writer.writerow(diffRow)
        
    orgRow = []
    calcRow = []
    
    rowList = []
    
    with open(writeFile, newline='') as csvfile:
        
        reader = csv.reader(csvfile)
        
        for row in reader:
            
            rowList.append(row)
            
    for elem in arrPar:
        
        rowVal = [elem]
        
        with open(writeFile, newline='') as csvfile:
            
            reader = csv.reader(csvfile)

            for row in reader:
                
                indVal = row[0]
                
                if (indVal=='Original'):
                    
                    orgRow = row
                
                if (indVal==str(elem)):
                    
                    calcRow = row
                    
        for rowInd, value in enumerate(orgRow):
            
            if (rowInd!=0):
                
                calcVal = float(calcRow[rowInd]) - float(value)
                rowVal.append(calcVal)
                
        rowList.append(rowVal)
        
    with open(writeFile, 'w', encoding='UTF8', newline='') as fW:
    
        writer = csv.writer(fW)
        
        for row in rowList:
            
            writer.writerow(row)
            
