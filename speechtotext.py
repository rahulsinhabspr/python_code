# -*- coding: utf-8 -*-
"""
Created on Thu Sep  7 22:30:15 2023

@author: rahul
"""

import speech_recognition as sphrecog
AUDIO_FILE = sphrecog.AudioFile("C:\\Users\\rahul\\OneDrive\\Desktop\\rahul-python\\rahul.wav")

print(AUDIO_FILE)


r = sphrecog.Recognizer()

with AUDIO_FILE as source:
      audio = r.record(source)
      

try:
    print('audio file contain:: '+ r.recognize_google(audio))
except sphrecog.UnknownValueError:
    print('Google speech recognition could not understand audio')
except sphrecog.RequestError:
    print('could not get the  results from Google Speech Recognition ')
    
