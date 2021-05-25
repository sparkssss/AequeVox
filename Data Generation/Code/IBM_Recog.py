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

apiKey = 'insert_api_key_here'
serviceURL = '{url}'

#IBM API Key and Service URL required for recognising files. Use your own credentials.

import json
from os.path import join, dirname
from ibm_watson import SpeechToTextV1
from ibm_watson.websocket import RecognizeCallback, AudioSource
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import threading

authenticator = IAMAuthenticator(apiKey)
service = SpeechToTextV1(
    authenticator=authenticator
)

service.set_default_headers({'x-watson-learning-opt-out': "true"})

service.set_service_url(serviceURL)

import librosa

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
            
            fileNum = speechNum[:-4]
            
            newFile = fileNum + appChar + str(elem) + '.wav'
            
            resList.append(newFile)
            
            signal, sr = librosa.load(newFile, sr=None)
            
            stringContent = 'audio/l16;rate=' + str(sr)
            
            with open(join(dirname(__file__), newFile),
                      'rb') as audio_file:
                response = service.recognize(
                        audio=audio_file,
                        model='en-US_BroadbandModel',
                        content_type=stringContent,
                        rate=sr).get_result()
            
            finRes = ''
            
            for result in response['results']:
                
                intResIBM = (result['alternatives'][0]['transcript'])
                
                intResIBM = intResIBM.replace("%HESITATION", "")
                
                finRes += intResIBM
    
            resList.append(finRes)
            
            strGroup = groupName + '_IBM_' + appChar + str(elem) + '.txt' 
            
            opFile = strGroup
        
            with open(opFile, 'w') as f:
                for item in resList:
                    f.write("%s\n" % item)
