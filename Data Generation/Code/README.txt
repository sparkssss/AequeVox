Replication Package for AequeVox:Automated Fariness Testing for Speech Recognition Systems

README under development.

Python Packages Required

numpy
scipy
math
librosa
random
time
json
threading
re
nltk

ASR Specific Packages with associated installation instructions via pip

Google Cloud

speech
- pip install --upgrade google-cloud-speech
Storage
- pip install --upgrade google-cloud-storage

Note: Credentials cannot be embedded in code. A service key in the form of a JSON file is required.
It can be created using GCP by following the linked procedure.

Link: https://cloud.google.com/speech-to-text/docs/libraries#setting_up_authentication

Microsoft Azure

Azure.cognitiveservices.speech
- pip install azure-cognitiveservices-speech

IBM Cloud

ibm_watson
ibm_watson.websocket
- pip install ibm-watson
Ibm_cloud_sdk_core.authenticators
- pip install ibm-cloud-sdk-core

The code is separated into 2 sections, Generation and Analysis.

Generation:

For ease of use, it is recommended that all audio files belonging to a group are grouped together in an appropriately named folder.
For instance, if we had 3 files, english1.wav, english2.wav and english3.wav, they ought to be placed into a folder titled english
along with a text file named fileNames.txt containing the below.

listUse = 'english1.wav', 'english2.wav', 'english3.wav'

For end to end testing of the tool, we recommend running the following files in sequence

1. transGen.py
2. GCP_Recog.py and/or MS_Recog.py and/or IBM_Recog.py
3. compASR.py
Note: For compASR.py, the first two lines of the python file allow you to specifiy the ASRs to be used. GCP/IBM, MS/GCP, and MS/IBM are tested in the paper.
4. compTableGen.py
Note: For compTableGen.py, the first two lines of the python file allow you to specifiy the ASRs to be used. GCP/IBM, MS/GCP, and MS/IBM are tested in the paper.
5. wordDropTableGen.py
Note: For wordDropTableGen.py, the first line of the python file allow you to specifiy the ASR to be used. GCP, MS, and IBM are tested in the paper.

CONFIG.txt

Contains a list of variables used in the code.
- datasetName = 'Accents' #A meaningful name for each set of groups to consider
- groupNames = 'english', 'ganda', 'french' #Names associated with all the groups to be tested
- transList = 'Noise', 'Amp', 'Clipping', 'Drop', 'Frame', 'HP', 'LP', 'Scale' # List of transformations. Transformations can be removed as necessary
- SNR = [2, 4, 6, 8, 10] #Parameters for Noise
- amp = [0.1, 0.2, 0.3, 0.4, 0.5, 2.0] #Parameters for Amp
- clipping = [0.01, 0.02, 0.03, 0.04, 0.05] #Parameters for Clipping
- drop = [5, 10, 15, 20, 25] #Parameters for Drop
- frame = [10, 20, 30, 40, 50] #Parameters for Frame
- highpass = [500, 600, 700, 800, 900] #Parameters for HP
- lowpass = [500, 600, 700, 800, 900] #Parameters for LP
- scale = [0.5, 0.6, 0.7, 0.8, 0.9, 1.0] #Parameters for Scale

transGen.py

Generates transformed speech files with form {Original File Name}{Transformation Type Abbreviation}{Magnitude of Transformation Parameter, theta}.wav and places them in the appropriate folder.

List of Abbreviations.

A - Amplitude
C - Clipping
D - Drop
F - Frame
HP - Highpass
LP - LP
N - Noise
S - Scale

GCP_Recog.py

Requires Google cloud client libraries and associated keys.

Generates transcripts for all the transformed files. Outputs text files in the form {Group Name}_GCP_{Transformation Type Abbreviation}{Magnitude of Transformation Parameter, theta}.txt

MS_Recog.py

Requires Microsoft Azure client libraries and associated key and region.

Generates transcripts for all the transformed files. Outputs text files in the form {Group Name}_MS_{Transformation Type Abbreviation}{Magnitude of Transformation Parameter, theta}.txt

IBM_Recog.py

Requires IBM client libraries and associated key and service URL..

Generates transcripts for all the transformed files. Outputs text files in the form {Group Name}_IBM_{Transformation Type Abbreviation}{Magnitude of Transformation Parameter, theta}.txt

compASR.py

Takes the names of two ASR systems to generate a distance metric. Result yields text files with distance metrics for specified ASR pair.

compTableGen.py

Takes the results of compASR.py and generates a csv file for further analysis using functions in the Analysis section.

wordDropTableGen.py

Takes the results of the recognition files to generate a list of the word drops (csv files) for further use in the Analysis section.

Analysis:

This section requires the csv files generated in the previous Generation phase.

Tables have been included with the code to aid in replication.