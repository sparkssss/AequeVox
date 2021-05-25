# AequeVox

Replication Package for AequeVox:Automated Fariness Testing for Speech Recognition Systems

README under development.

Python Packages Required

* numpy
* scipy
* math
* librosa
* random
* time
* json
* threading
* re
* nltk

ASR Specific Packages

Google Cloud

* speech
* Storage

Microsoft Azure

* Azure.cognitiveservices.speech

IBM Cloud

* ibm_watson
* ibm_watson.websocket
* Ibm_cloud_sdk_core.authenticators

The code is separated into 2 sections, Generation and Analysis.

Generation:

transGen.py

* Lists all transformation types and magnitudes to be used. Can be modified as necessary.
* Requires the specification of file names of all the original speech files.

Generates transformed speech files with form {Original File Name}{Transformation Type Abbreviation}{Magnitude of Transformation Parameter, theta}.wav

List of Abbreviations.

1. A - Amplitude
2. C - Clipping
3. D - Drop
4. F - Frame
5. HP - Highpass
6. LP - LP
7. N - Noise
8. S - Scale

GCP_Recog.py

Requires Google cloud client libraries and associated keys.

Takes a group name and the list of all original files in the group to generate transcripts.

MS_Recog.py

Requires Microsoft Azure client libraries and associated key and region.

Takes a group name and the list of all original files in the group to generate transcripts.

IBM_Recog.py

Requires IBM client libraries and associated key and service URL..

Takes a group name and the list of all original files in the group to generate transcripts.

compASR.py

Takes the names of two ASR systems and group names to generate a distance metric. Result yields text files with distance metrics for specified groups.

Users are requested to use the distance metrics to calculate the D values for each transformation.
