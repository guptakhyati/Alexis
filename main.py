import speech_recognition as sr
import time
from time import ctime
import webbrowser
from playsound import playsound    #To play the saved audio file
import os                          #To remove audio files from being piled up in our code at the end
import random                     #To randomly generate a name for the audio file
from gtts import gTTS
import datetime
from datetime import date
r=sr.Recognizer()

def record_audio(ask=False):
    with sr.Microphone() as source:
        #print('Say something')
        if ask:
            #print(ask)
            alexis_speak(ask)
        r.adjust_for_ambient_noise(source, duration = 1) #To remove background noises
        r.energy_threshold += 280
        audio=r.listen(source)
        voice_data = ''
        try:

            voice_data=r.recognize_google(audio)
            #print(voice_data)
        except sr.UnknownValueError:
            alexis_speak('Sorry, I did not get that')
        except sr.RequestError:
            alexis_speak('Sorry, my speech service is down')
        return voice_data

def respond(voice_data):
    if 'what is your name' in voice_data:
        alexis_speak('My name is Alexis')
    if 'what time is it' in voice_data:
        alexis_speak('It is '+ time.ctime())
    if 'search' in voice_data:
        search=record_audio('What do you want to search?')
        url='https://google.com/search?q='+search
        webbrowser.get().open(url)
        alexis_speak('Here is what I found for '+search)
    if 'find location' in voice_data:
        location=record_audio('What is the location?')
        url='https://google.nl/maps/place/'+location+'/&amp;'
        webbrowser.get().open(url)
        alexis_speak('Here is the location of '+location)
    if 'suggest me some latest movies' in voice_data:
        movie=record_audio('Which kind of movies do you like?')
        url='https://google.com/search?q='+movie
        webbrowser.get().open(url)
        alexis_speak('Here is what I found for '+movie)
    if 'thank you so much for your assistance' in voice_data:
        alexis_speak('You are welcome!')
    if 'exit' in voice_data:
        exit()

def alexis_speak(audio_string):
    tts=gTTS(text=audio_string,lang='en-GB')
    r=random.randint(1,10000000)
    audio_file='audio-'+str(r)+'.mp3'
    tts.save(audio_file)
    playsound(audio_file)
    print(audio_string)
    os.remove(audio_file)



time.sleep(1)
alexis_speak('How can I help you?')
while 1:
    voice_data=record_audio()
    #print(voice_data)
    respond(voice_data)
