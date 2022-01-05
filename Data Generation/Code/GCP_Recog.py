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
        
fConfig.close()

'''

groupName = 'nativeEnglish'
#specify Group Name for Storage of Results

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

listUse = ['example1.wav', 'example2.wav', 'example3.wav']
#List of Original Unmodified Files in Group

'''

# Imports the Google Cloud client library
from google.cloud import speech

# Instantiates a client
client = speech.SpeechClient()

from google.cloud import storage

storage_client = storage.Client()
bucketName = "bucket_name"
bucket = storage_client.bucket(bucketName)

#Google Cloud Storage Required for recognising files. Use your own credentials.

import librosa

for group in groupNames:
    
    fNamesText = group + '/' + 'fileNames.txt'
    
    fNames = open(fNamesText, "r")
    
    while True:
        
        line = fNames.readline()
        
        if not line:
            break
        
        words = line[:-1]
        
        if words[:7] == 'listUse':
            
            intWords = words[7:]
            
            intWordInd = intWords.find('\'')
            
            intWords = intWords[intWordInd:]
            
            resWords = intWords.split(',')
            
            newResWords = []
            
            for resWord in resWords:
                
                start = resWord.find('\'') + 1
                resWord = resWord[start:]
                end = resWord.find('\'')
                resWord = resWord[:end]
                
                newResWords.append(resWord)
                
            resWords = newResWords
            
            listUse = resWords

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
            
        for elem in arrPar:
            
            resList = []
            
            for speechNum in listUse:
                
                speechNum = group + '/' + speechNum
                
                fileNum = speechNum[:-4]
                
                newFile = fileNum + appChar + str(elem) + '.wav'
                
                signal, sr = librosa.load(newFile, sr=None)
                
                resList.append(newFile)
                
                blob = bucket.blob(newFile)
            
                blob.upload_from_filename(newFile)
                
                gcsURI = "gs://" + bucketName + "/" + newFile
                
                audio = speech.RecognitionAudio(uri=gcsURI)
                    
                config = speech.RecognitionConfig(
                encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
                sample_rate_hertz=sr,
                language_code="en-US",
                )
                
                operation = client.long_running_recognize(
                    request={"config": config, "audio": audio}
                )
                
                response = operation.result()
                
                finRes = ''
                
                for result in response.results:
                    finRes += result.alternatives[0].transcript
        
                resList.append(finRes)
                
            strGroup = group + '_GCP_' + appChar + str(elem) + '.txt' 
            
            opFile = strGroup
        
            with open(opFile, 'w') as f:
                for item in resList:
                    f.write("%s\n" % item)
                        
    fNames.close()
