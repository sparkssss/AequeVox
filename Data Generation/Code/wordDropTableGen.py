asrType = 'GCP'

wordList = ['please','call','stella','ask','her','to','bring','these',
            'things','with','from','the','store','six','spoons','of','fresh',
            'snow','peas','five','thick','slabs','blue','cheese','and',
            'maybe','a','snack','for','brother','bob','we','also','need',
            'small','plastic','snake','big','toy','frog','kids','she',
            'can','scoop','into','three','red','bags','will','go','meet',
            'wednesday','at','train','station']

countGT = [4,4,4,4,16,4,4,8,8,4,4,12,
           4,4,4,8,4,4,4,4,4,4,4,4,12,
           4,12,4,8,4,4,8,4,4,4,4,4,4,4,
           4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4]

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

asrType = 'GCP'
#Specify ASR
#Available ASRs: GCP, IBM, MS

transList = ['Noise', 'Amp', 'Clipping', 'Drop', 'Frame', 'HP', 'LP', 'Scale']
#Comprehensive List of Transformations: Noise, Amp, Clipping, Drop,
#Frame, HP, LP, and Scale. Replace with Desired Tranformations

wordList = ['please','call','stella','ask','her','to','bring','these',
            'things','with','from','the','store','six','spoons','of','fresh',
            'snow','peas','five','thick','slabs','blue','cheese','and',
            'maybe','a','snack','for','brother','bob','we','also','need',
            'small','plastic','snake','big','toy','frog','kids','she',
            'can','scoop','into','three','red','bags','will','go','meet',
            'wednesday','at','train','station']

countGT = [4,4,4,4,16,4,4,8,8,4,4,12,
           4,4,4,8,4,4,4,4,4,4,4,4,12,
           4,12,4,8,4,4,8,4,4,4,4,4,4,4,
           4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4]

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

import re

fileWrite2 = asrType + ' Word Counts - Average' + '.csv'

with open(fileWrite2, 'w', encoding='UTF8', newline='') as fW2:
    
    writer2 = csv.writer(fW2)
    
    writer2Row = 'Average Word Drops'
    
    writer2.writerow(writer2Row)
    
    writer2Row = ''
    
    for group in groupNames:
        
        writer2Row.append(group)
        
    writer2.writerow(writer2Row)

    for transType in transList:
        
        useArr = [transType]
        
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
            
        fileWrite = asrType + ' Word Counts - ' + transType + '.csv'
        
        with open(fileWrite, 'w', encoding='UTF8', newline='') as fW:
            
            writer = csv.writer(fW)
            
            firstRow = ['']
            
            count = 1
            
            for word in wordList:
                
                count = count + 1
                
                firstRow.append(word)
                
            firstRow.append('')
                
            writer.writerow(firstRow)
             
            gtRow = ['GT']
             
            for gtNum in countGT:
                
                gtRow.append(gtNum)
                
            gtRow.append('')
                 
            writer.writerow(gtRow)
                 
            intRow = ['']*count
            
            for group in groupNames:
                
                writer.writerow(intRow.append(''))
                
                nextRow = intRow
                nextRow.insert(0, group)
                nextRow = nextRow[:-1]
                
                nextRow.append('')
                
                writer.writerow(nextRow)
                
                orgRow = ['Original']
                
                fileScale = group + '_' + asrType + '_' + 'S' + str(1.0) + '.txt'
                
                fScale = open(fileScale, "r")
                
                comp1 = []
                
                for x in fScale:
                    if not x[-5:-1] == '.wav':
                        
                        x = x.replace("%HESITATION", "")
                        
                        resX = re.split('[- : , ; . \s \n]',x)
                        resX[:] = [y for y in resX if y]
                        resX = [z.lower() for z in resX]
                        
                        comp1.append(resX)
                        
                fScale.close()
                             
                for word in wordList:
                    
                    wordCount = 0
                    
                    for sen in comp1:
                        
                        wordCount = wordCount + sum((curWord == word for (curWord) in sen))
                        
                    orgRow.append(wordCount)
                    
                orgRow.append('')
                    
                writer.writerow(orgRow)
                
                dumRow = []
                
                for elem in arrPar:
                    
                    fileCur = group + '_' + asrType + '_' + appChar + str(elem) + '.txt'
                    
                    fCur = open(fileCur, "r")
                    
                    nextRow = [str(elem)]
                    dumRow = ['Dummy']
                    
                    for i in range(count-1):
                        
                        dumRow.append(float('inf'))
                    
                    comp1 = []
                    
                    for x in fCur:
                        if not x[-5:-1] == '.wav':
                            
                            x = x.replace("%HESITATION", "")
                            
                            resX = re.split('[- : , ; . \s \n]',x)
                            resX[:] = [y for y in resX if y]
                            resX = [z.lower() for z in resX]
                            
                            comp1.append(resX)
                            
                    fCur.close()
                                 
                    for wordInd, word in enumerate(wordList):
                        
                        wordCount = 0
                        
                        for sen in comp1:
                            
                            wordCount = wordCount + sum((curWord == word for (curWord) in sen))
                            
                        nextRow.append(wordCount)
                        
                        if (wordCount<dumRow[wordInd+1]):
                            
                            dumRow[wordInd+1] = wordCount
                            
                    nextRow.append('')
                    
                    writer.writerow(nextRow)
                    
                endRow = ['Drops']
                
                for wordInd, word in enumerate(wordList):
                    
                    dropCount = orgRow[wordInd+1] - dumRow[wordInd+1]
                    
                    endRow.append(dropCount)
                    
                divCalc = sum(endRow[1:])/(count-1)
                
                useArr.append(divCalc)
                
                endRow.append(divCalc)
                    
                writer.writerow(endRow)
                
        writer2.writerow(useArr)
            
