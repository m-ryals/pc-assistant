#!/usr/bin/python3

# Import Libraries
import getcommand
import speech_recognition as sr
import os
import time
from playsound import playsound
from retrying import retry

# Init Recognizer, Mic
r = sr.Recognizer()
mic = sr.Microphone(device_index=0)

# Using the mic variable set earlier, listen and adjust for ambient noise, then begin listening for the keyword

with mic as source:
    while 1:
        r.adjust_for_ambient_noise(source)
        #r.energy_threshold = 150
        #r.pause_threshold = 1.1
        print('speak')
        audio = r.listen(source)
        try: 
            text = r.recognize_google(audio)
            print(text)
            if('computer' in text):
                 getcommand.getcommand(text)
        except sr.UnknownValueError:
            os.system('echo [$TIME]: error: not recognized >> /home/ryals/log/assist.log')
        except sr.RequestError:
            os.system('echo [$TIME] error: could not get a reply from google >> /home/ryals/log/assist.log')
