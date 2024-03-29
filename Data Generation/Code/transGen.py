import numpy as np
from scipy.signal import butter,filtfilt

import math

import librosa

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
#List of Files to be transformed
'''

def butter_lowpass_filter(data, cutoff, fs, order):
    
    nyq = 0.5 * fs
    normal_cutoff = cutoff / nyq
    # Get the filter coefficients 
    b, a = butter(order, normal_cutoff, btype='low', analog=False)
    y = filtfilt(b, a, data)
    
    return y

def butter_highpass_filter(data, cutoff, fs, order):
    
    nyq = 0.5 * fs
    normal_cutoff = cutoff / nyq
    # Get the filter coefficients 
    b, a = butter(order, normal_cutoff, btype='high', analog=False)
    y = filtfilt(b, a, data)
    
    return y

from scipy.io.wavfile import write

import random

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
                fileName = speechNum
                signal, sr = librosa.load(fileName, sr=None)
                
                if transType=='Noise':
                    
                    RMS_Signal=math.sqrt(np.mean(signal**2))
                    
                    RMSNoise = math.sqrt(RMS_Signal**2/(pow(10,elem/10)))
                    noise=np.random.normal(0, RMSNoise, len(signal))
                    finSpeech = signal + noise
                elif transType=='Drop':        
                
                    numSec = signal.shape[0]/sr
                    numBlocks = math.floor(numSec/(0.04))
                    
                    numSelect = math.floor((elem/100)*numBlocks*2)
                    
                    sBlocks = random.sample(range(1, numBlocks+1), numSelect)
                    
                    for block in sBlocks:
                        
                        blockInd = math.floor((block-1)*sr*0.04)
                        jumpInd = math.floor(sr*0.02)
                        signal[blockInd:blockInd+jumpInd] = 0
                        
                    finSpeech = signal
                elif transType=='Frame':
                
                    numSec = signal.shape[0]/sr
                    frameSize = elem/1000
                    
                    numBlocks = math.floor(numSec/(frameSize*2))
                    
                    numSelect = math.floor((10/100)*numBlocks*2)
                    
                    sBlocks = random.sample(range(1, numBlocks+1), numSelect)
                    
                    for block in sBlocks:
                        
                        blockInd = math.floor((block-1)*sr*frameSize*2)
                        jumpInd = math.floor(sr*frameSize)
                        signal[blockInd:blockInd+jumpInd] = 0
                        
                    finSpeech = signal
                elif transType=='Amp':
                    
                    signal = signal * elem
                    finSpeech = signal
                elif transType=='HP':
                    
                    order = 2
                    
                    finSpeech = butter_lowpass_filter(signal, elem, sr, order)
                elif transType=='LP':
                    
                    order = 2
                
                    finSpeech = butter_highpass_filter(signal, elem, sr, order)
                
                finSpeech /=1.414
                
                if transType=='Clipping':
                    
                    boolOver = finSpeech > elem
                    boolUnder = finSpeech < (elem * -1)
                    
                    finSpeech[boolOver] = elem
                    finSpeech[boolUnder] = (elem * -1)
                
                finSpeech *= 32767
                speechWav = finSpeech.astype(np.int16)
                
                newFile = fileNum + appChar + str(elem) + '.wav'
                
                if transType=='Scale':
                    
                    write(newFile, math.floor(sr*elem), speechWav)
                else:
                    
                    write(newFile, sr, speechWav)
                    
    fNames.close()