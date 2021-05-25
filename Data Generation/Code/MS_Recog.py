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

import azure.cognitiveservices.speech as speechsdk

apiKey = "insert_api_key"
regionName = "region_name"

#MS Azure STT Key and Region required for recognising files. Use your own credentials.

import time

speech_config = speechsdk.SpeechConfig(subscription=apiKey, region=regionName)
speech_config.speech_recognition_language="en-US"

def speech_recognize_continuous_from_file(fileName):
    """performs continuous speech recognition with input from an audio file"""
    # <SpeechContinuousRecognitionWithFile>
    speech_config = speechsdk.SpeechConfig(subscription=apiKey, region=regionName)
    speech_config.speech_recognition_language="en-US"
    audio_config = speechsdk.audio.AudioConfig(filename=fileName)

    speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config, audio_config=audio_config)

    done = False

    def stop_cb(evt):
        """callback that stops continuous recognition upon receiving an event `evt`"""
        print('CLOSING on {}'.format(evt))
        speech_recognizer.stop_continuous_recognition()
        nonlocal done
        done = True
        
    all_results = []
    
    def handle_final_result(evt):
        all_results.append(evt.result.text)
    
    speech_recognizer.recognized.connect(handle_final_result)

    '''
    # Connect callbacks to the events fired by the speech recognizer
    speech_recognizer.recognizing.connect(lambda evt: print('RECOGNIZING: {}'.format(evt)))
    speech_recognizer.recognized.connect(lambda evt: print('RECOGNIZED: {}'.format(evt)))
    speech_recognizer.session_started.connect(lambda evt: print('SESSION STARTED: {}'.format(evt)))
    speech_recognizer.session_stopped.connect(lambda evt: print('SESSION STOPPED {}'.format(evt)))
    speech_recognizer.canceled.connect(lambda evt: print('CANCELED {}'.format(evt)))
    '''
    
    # stop continuous recognition on either session stopped or canceled events
    speech_recognizer.session_stopped.connect(stop_cb)
    #speech_recognizer.canceled.connect(stop_cb)

    # Start continuous speech recognition
    speech_recognizer.start_continuous_recognition()
    while not done:
        time.sleep(.1)
    # </SpeechContinuousRecognitionWithFile>
    
    return all_results

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
            
            result = speech_recognize_continuous_from_file(newFile)
            
            finRes = ''
            
            for resElem in result:
                
                finRes += resElem
    
            resList.append(finRes)
            
            strGroup = groupName + '_MS_' + appChar + str(elem) + '.txt' 
            
            opFile = strGroup
        
            with open(opFile, 'w') as f:
                for item in resList:
                    f.write("%s\n" % item)