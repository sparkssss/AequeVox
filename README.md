# Replication Package for AequeVox: Automated Fairness Testing for Speech Recognition Systems

![Detecting Unfairness in Speech Recognition System](https://github.com/sparkssss/AequeVox/blob/main/intro-diagram.png?raw=true)

AequeVox is an automated testing framework for evaluating the fairness of ASR systems. AequeVox simulates different environments through meaningful transformations to assess the effectiveness of ASR systems for different populations. It also introduces a fault localization technique capable of identifying words that are not robust to these varying environments. Both components of AequeVox are able to operate in the absence of ground truth data.

## Requirements

### Python Packages Required

* numpy (1.21.5)
* scipy
* math
* librosa
* random
* time
* json
* threading
* re
* nltk

### ASR Specific Packages with associated installation instructions via pip

#### Google Cloud

speech
Storage

```
pip install --upgrade google-cloud-speech
pip install --upgrade google-cloud-storage
```

Note: Credentials cannot be embedded in code. A service key in the form of a JSON file is required.
It can be created using GCP by following the linked procedure.

Link: [GCP Credentials](https://cloud.google.com/speech-to-text/docs/libraries#setting_up_authentication)

#### Microsoft Azure

Azure.cognitiveservices.speech

```
pip install azure-cognitiveservices-speech
```

#### IBM Cloud

ibm_watson
ibm_watson.websocket
Ibm_cloud_sdk_core.authenticators

```
pip install ibm-watson
pip install ibm-cloud-sdk-core
```

## For Offline pip Installation (Ubuntu)

'''
pip install numpy-1.21.5-cp38-cp38-manylinux_2_12_x86_64.manylinux2010_x86_64.whl
pip install appdirs-1.4.4-py2.py3-none-any.whl
pip install audioread-2.1.9.tar.gz
pip install azure_cognitiveservices_speech-1.19.0-cp38-cp38-manylinux1_x86_64.whl
pip install cachetools-4.2.4-py3-none-any.whl
pip install certifi-2021.10.8-py2.py3-none-any.whl
pip install cffi-1.15.0-cp38-cp38-manylinux_2_12_x86_64.manylinux2010_x86_64.whl
pip install charset_normalizer-2.0.10-py3-none-any.whl
pip install click-8.0.3-py3-none-any.whl
pip install cycler-0.11.0-py3-none-any.whl
pip install decorator-5.1.1-py3-none-any.whl
pip install fonttools-4.28.5-py3-none-any.whl
pip install google_api_core-2.4.0-py2.py3-none-any.whl
pip install googleapis_common_protos-1.54.0-py2.py3-none-any.whl
pip install google_auth-2.3.3-py2.py3-none-any.whl
pip install google_cloud_core-2.2.2-py2.py3-none-any.whl
pip install google_cloud_speech-2.12.0-py2.py3-none-any.whl
pip install google_cloud_storage-2.1.0-py2.py3-none-any.whl
pip install google_crc32c-1.3.0-cp38-cp38-manylinux_2_12_x86_64.manylinux2010_x86_64.whl
pip install google_resumable_media-2.1.0-py2.py3-none-any.whl
pip install grpcio-1.43.0-cp38-cp38-manylinux_2_17_x86_64.manylinux2014_x86_64.whl
pip install grpcio_status-1.43.0-py3-none-any.whl
pip install ibm-cloud-sdk-core-3.14.0.tar.gz
pip install ibm-watson-5.3.0.tar.gz
pip install idna-3.3-py3-none-any.whl
pip install joblib-1.1.0-py2.py3-none-any.whl
pip install kiwisolver-1.3.2-cp38-cp38-manylinux_2_5_x86_64.manylinux1_x86_64.whl
pip install libcst-0.4.0-cp38-cp38-manylinux_2_17_x86_64.manylinux2014_x86_64.whl
pip install librosa-0.8.1-py3-none-any.whl
pip install llvmlite-0.38.0-cp38-cp38-manylinux_2_17_x86_64.manylinux2014_x86_64.whl
pip install matplotlib-3.5.1-cp38-cp38-manylinux_2_5_x86_64.manylinux1_x86_64.whl
pip install mypy_extensions-0.4.3-py2.py3-none-any.whl
pip install nltk-3.6.7-py3-none-any.whl
pip install numba-0.55.0-cp38-cp38-manylinux2014_x86_64.manylinux_2_17_x86_64.whl
pip install packaging-21.3-py3-none-any.whl
pip install Pillow-9.0.0-cp38-cp38-manylinux_2_17_x86_64.manylinux2014_x86_64.whl
pip install pooch-1.5.2-py3-none-any.whl
pip install protobuf-3.19.3-cp38-cp38-manylinux_2_17_x86_64.manylinux2014_x86_64.whl
pip install proto_plus-1.19.8-py3-none-any.whl
pip install pyasn1-0.4.8-py2.py3-none-any.whl
pip install pyasn1_modules-0.2.8-py2.py3-none-any.whl
pip install pycparser-2.21-py2.py3-none-any.whl
pip install PyJWT-2.3.0-py3-none-any.whl
pip install pyparsing-3.0.6-py3-none-any.whl
pip install pyparsing-3.0.7-py3-none-any.whl
pip install python_dateutil-2.8.2-py2.py3-none-any.whl
pip install PyYAML-6.0-cp38-cp38-manylinux_2_5_x86_64.manylinux1_x86_64.manylinux_2_12_x86_64.manylinux2010_x86_64.whl
pip install regex-2022.1.18-cp38-cp38-manylinux_2_17_x86_64.manylinux2014_x86_64.whl
pip install requests-2.27.1-py2.py3-none-any.whl
pip install resampy-0.2.2.tar.gz
pip install rsa-4.8-py3-none-any.whl
pip install scikit_learn-1.0.2-cp38-cp38-manylinux_2_17_x86_64.manylinux2014_x86_64.whl
pip install scipy-1.7.3-cp38-cp38-manylinux_2_17_x86_64.manylinux2014_x86_64.whl
pip install setuptools-60.5.0-py3-none-any.whl
pip install six-1.16.0-py2.py3-none-any.whl
pip install SoundFile-0.10.3.post1-py2.py3-none-any.whl
pip install threadpoolctl-3.0.0-py3-none-any.whl
pip install tqdm-4.62.3-py2.py3-none-any.whl
pip install typing_extensions-4.0.1-py3-none-any.whl
pip install typing_inspect-0.7.1-py3-none-any.whl
pip install urllib3-1.26.8-py2.py3-none-any.whl
pip install websocket_client-1.1.0-py2.py3-none-any.whl
'''



## Usage

The code is separated into 2 sections, Generation and Analysis.

### Generation:

For ease of use, it is recommended that all audio files belonging to a group are grouped together in an appropriately named folder.
For instance, if we had 3 files, english1.wav, english2.wav and english3.wav, they ought to be placed into a folder titled english
along with a text file named fileNames.txt containing the below.

```
listUse = 'english1.wav', 'english2.wav', 'english3.wav'
```

```
Code
│   README.md
│   CONFIG.txt    
│
└───english
│   │   fileNames.txt
│   │   english1.wav
│   │   english2.wav
|   |   english3.wav
│   │
│   
└───french
    │   fileNames.txt
    │   french1.wav
    │   french2.wav
```

For end to end testing of the tool, we recommend running the following files in sequence

1. transGen.py
2. GCP_Recog.py and/or MS_Recog.py and/or IBM_Recog.py
3. compASR.py
 * Note: For compASR.py, the first two lines of the python file allow you to specify the ASRs to be used. GCP/IBM, MS/GCP, and MS/IBM are tested in the paper.
4. compTableGen.py
 * Note: For compTableGen.py, the first two lines of the python file allow you to specify the ASRs to be used. GCP/IBM, MS/GCP, and MS/IBM are tested in the paper.
5. wordDropTableGen.py
 * Note: For wordDropTableGen.py, the first line of the python file allow you to specify the ASR to be used. GCP, MS, and IBM are tested in the paper.

#### CONFIG.txt

Contains a list of variables used in the code.

```
datasetName = 'Accents' #A meaningful name for each set of groups to consider
groupNames = 'english', 'ganda', 'french' #Names associated with all the groups to be tested
transList = 'Noise', 'Amp', 'Clipping', 'Drop', 'Frame', 'HP', 'LP', 'Scale' # List of transformations. Transformations can be removed as necessary
SNR = [2, 4, 6, 8, 10] #Parameters for Noise
amp = [0.1, 0.2, 0.3, 0.4, 0.5, 2.0] #Parameters for Amp
clipping = [0.01, 0.02, 0.03, 0.04, 0.05] #Parameters for Clipping
drop = [5, 10, 15, 20, 25] #Parameters for Drop
frame = [10, 20, 30, 40, 50] #Parameters for Frame
highpass = [500, 600, 700, 800, 900] #Parameters for HP
lowpass = [500, 600, 700, 800, 900] #Parameters for LP
scale = [0.5, 0.6, 0.7, 0.8, 0.9, 1.0] #Parameters for Scale
```

#### transGen.py

Generates transformed speech files with form {Original File Name}{Transformation Type Abbreviation}{Magnitude of Transformation Parameter, theta}.wav and places them in the appropriate folder.

List of Abbreviations.

* A - Amplitude
* C - Clipping
* D - Drop
* F - Frame
* HP - Highpass
* LP - LP
* N - Noise
* S - Scale

#### ASR Specific Files

These files take in the transformed audio files and return transcripts in the form of text files. For instance one generated file might be named
english_GCP_N2.txt and contain text similar to the below block.

```
english/english1N2.wav
please call stella ...
english/english2N2.wav
please call stella ...
english/english3N2.wav
please call stella ...
```

##### GCP_Recog.py

Requires Google cloud client libraries and associated keys.

Generates transcripts for all the transformed files. Outputs text files in the form {Group Name}_GCP_{Transformation Type Abbreviation}{Magnitude of Transformation Parameter, theta}.txt

##### MS_Recog.py

Requires Microsoft Azure client libraries and associated key and region.

Generates transcripts for all the transformed files. Outputs text files in the form {Group Name}_MS_{Transformation Type Abbreviation}{Magnitude of Transformation Parameter, theta}.txt

##### IBM_Recog.py

Requires IBM client libraries and associated key and service URL..

Generates transcripts for all the transformed files. Outputs text files in the form {Group Name}_IBM_{Transformation Type Abbreviation}{Magnitude of Transformation Parameter, theta}.txt

#### compASR.py

Takes the names of two ASR systems to generate a distance metric. Result yields text files with distance metrics for specified ASR pair. The resultant text file takes the form {Dataset Name}_{ASR Type 1}_{ASR Type 2}{Transformation Type}.txt. Suggested pairs: GCP_IBM, MS_GCP, and MS_IBM.

A sample text file generated is given below.

```
english
(2, 0.37432)
(4, 0.25334242)
(6, 0.37432)
french
(2, 0.24132)
(4, 0.20034242)
(6, 0.17432)
```

#### compTableGen.py

Takes the results of compASR.py and generates a csv file for further analysis using functions in the Analysis section in the form of 
{AsrType1}_{AsrType2} Differential Speech Results - {Transformation Type}.csv. Suggested pairs: GCP_IBM, MS_GCP, and MS_IBM.

```

|           |Eng                |Gan                |Fr                 |Guj                |Ind                |Kor                |Rus                |
|-----------|-------------------|-------------------|-------------------|-------------------|-------------------|-------------------|-------------------|
|5          |0.12363636363636364|0.24468085106382978|0.12363636363636364|0.16666666666666666|0.17562724014336917|0.41454545454545455|0.23272727272727273|
|10         |0.13768115942028986|0.26480836236933797|0.14909090909090908|0.18840579710144928|0.19424460431654678|0.4684014869888476 |0.23826714801444043|
|15         |0.12681159420289856|0.33935018050541516|0.1391941391941392 |0.21978021978021978|0.21245421245421245|0.5019607843137255 |0.23333333333333334|
|20         |0.15018315018315018|0.3861003861003861 |0.17883211678832117|0.25274725274725274|0.21454545454545454|0.51953125         |0.31970260223048325|
|25         |0.15579710144927536|0.4846153846153846 |0.2600732600732601 |0.2936802973977695 |0.32567049808429116|0.6072874493927125 |0.34099616858237547|
|           |                   |                   |                   |                   |                   |                   |                   |
|Original   |0.1090909091       |0.2132867133       |0.1123188406       |0.152173913        |0.1612903226       |0.3455882353       |0.1781818182       |
|           |                   |                   |                   |                   |                   |                   |                   |
|Differences|                   |                   |                   |                   |                   |                   |                   |
|5          |0.01454545455      |0.03139413778      |0.01131752306      |0.01449275362      |0.01433691756      |0.06895721925      |0.05454545455      |
|10         |0.02859025033      |0.05152164908      |0.03677206851      |0.03623188406      |0.03295428174      |0.1228132517       |0.06008532983      |
|15         |0.01772068511      |0.1260634672       |0.02687529861      |0.06760630674      |0.05116388987      |0.156372549        |0.05515151515      |
|20         |0.04109224109      |0.1728136728       |0.06651327621      |0.1005733397       |0.05325513196      |0.1739430147       |0.141520784        |
|25         |0.04670619236      |0.2713286713       |0.1477544195       |0.1415063844       |0.1643801755       |0.2616992141       |0.1628143504       |

```

#### wordDropTableGen.py

Takes the results of the recognition files to generate a list of the word drops (csv files) for further use in the Analysis section. These files take the form
{AsrType} Word Counts - {Transformation Type}.csv and {AsrType} Word Counts - Average.csv. A sample average counts table is shown below.

```

|         |English     |Ganda       |French      |Gujarati    |Indonesian  |Korean      |Russian     |
|---------|------------|------------|------------|------------|------------|------------|------------|
|Clipping |2.581818182 |3.036363636 |2.727272727 |3.454545455 |2.890909091 |2.963636364 |4.036363636 |
|Amplitude|0.4909090909|0.3090909091|0.2181818182|0.2545454545|0.1636363636|0.4909090909|0.2909090909|
|Drop     |0.4909090909|1           |0.8909090909|0.7454545455|0.7636363636|1.345454545 |0.9272727273|
|Frame    |0.7090909091|1.163636364 |1.036363636 |0.9636363636|0.6727272727|1.545454545 |0.8363636364|
|HP       |2.145454545 |1.854545455 |0.8181818182|0.4727272727|1.272727273 |1.145454545 |2.109090909 |
|LP       |0.5272727273|1.127272727 |0.8363636364|0.8545454545|0.5090909091|1.109090909 |1.290909091 |
|Noise    |0.8363636364|1.490909091 |1.363636364 |1.690909091 |0.9454545455|1.818181818 |1.981818182 |
|Scale    |1.927272727 |2.127272727 |1.818181818 |0.9090909091|1.327272727 |1.981818182 |1.618181818 |

```

### Analysis

This section requires the csv files generated in the previous Generation phase.

Tables have been included with the code to aid in replication.

#### NOTE

Differential Testing Stats, Explainability_Unfairness and non-robust-words.ipynb require csv files to be placed in appropriate locations. Alternatively, the get_file_data() function can be used to ensure it points to the correct file. 

#### Differential Testing Stats

Calculates the number of errors induced by each group in the dataset as you vary tau. It utillises the outputs from compTableGen.py. 

* To compare groups in the Accents dataset, the file for the GCP/IBM comparison ought to be placed under the subfolder Accents/GCP_IBM. 

* The graphs can then be generated using the Diff_Testing_Stats.ipynb.

#### Explainability_Unfairness

It uses the Average Word Counts csv file to generate graphs for average word mispredictions. It utillises the outputs from wordDropTableGen.py.

* To compare word drops, the generated csv file for IBM must be placed into the subfolder Data.

* The graphs can then be generated using the Explainability_Graphs.ipynb.

#### non-robust-words.ipynb

Uses the csv file generated by wordDropTableGen.py. In particular, it uses the per transformation csv file to generate word drop graphs on a per transformation basis.
It also prints a word drop array. (This array lists words in increasing order of robustness)

* To check the non-robust for the IBM ASR, the file ought to be placed in the subfolder IBM.

* The graphs can then be generated using the non-robust-words.ipynb.

#### ASR Specific Sentence Generation Notebooks

They utillise a constructed grammar to generate sentences that comprise of robust and non-robust words respectively.

* These can be generated using the ASR specific notebooks. They take the form {ASR Type}-Sentence-Gen-Template.ipynb.

#### Generalizability RQ

We use a TTS engine followed by an ASR engine to verify that the generated sentences containing non-robust words induce mispredictions of said non-robust words.

* The Gen_Graphs.ipynb generates the graph comparing the errors between the two classes of sentences.

#### User Study

The data for the user study is included in the Repo and running the Graphs.ipynb will allow users to generate the comprehensibility rating diagram shown below.

![Comprehensibilty Threshold Based on User Study](https://github.com/sparkssss/AequeVox/blob/main/Analysis/User%20Study/User-Study-Graph.png?raw=true)

## Datasets Used

Audio data (and the transformed audio files) used in the evaluation of the paper is linked below. The link also contains a copy of this Repo in addition to the dataset.

Link: [DOI](https://doi.org/10.5281/zenodo.5819311)

Additionally, the tables used for analysis are also included in the Analysis section.

## Caveats

Code associated with counting number of dropped words and generation of non-robust sentences is specific to the Accents dataset.
As such, the list of words checked against is drawn from the dataset. This cannot be replicated with other datasets. Additionally,
the generation of sentences is also dependent on a constructed grammar that is specific to the words in question.

## License

Shield: [![CC BY-NC-SA 4.0][cc-by-nc-sa-shield]][cc-by-nc-sa]

This work is licensed under a
[Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License][cc-by-nc-sa].

[![CC BY-NC-SA 4.0][cc-by-nc-sa-image]][cc-by-nc-sa]

[cc-by-nc-sa]: http://creativecommons.org/licenses/by-nc-sa/4.0/
[cc-by-nc-sa-image]: https://licensebuttons.net/l/by-nc-sa/4.0/88x31.png
[cc-by-nc-sa-shield]: https://img.shields.io/badge/License-CC%20BY--NC--SA%204.0-lightgrey.svg

## Citing AequeVox

```
@inproceedings{aequevox,
  title={AequeVox: Automated Fairness Testing of Speech Recognition Systems},
  author={Sai Sathiesh Rajan and
               Sakshi Udeshi and
               Sudipta Chattopadhyay},
  booktitle={25th International Conference on Fundamental Approaches to Software Engineering (FASE)},
  year={2022}
}
```
