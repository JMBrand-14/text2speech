# pip install pyttsx3
# Import the required module for text to speech conversion
import argparse

from gtts import gTTS

#from mpg123 import Mpg123, Out123

# This module is imported os that we can play the converted audio
import os

# Read the file
# The text that you want to convert to audio

my_file = "my_file"
f = open(my_file+'.txt', 'rb')
mytext = f.read()
f.close()

# Language in which you want to convert
language = 'en'

# Passing the text and language to the engine, here we have marked slow=False.
# Which tells the module that the converted audio should have a high speed
myobj = gTTS(text=mytext, lang=language, slow=True)

# Saving the converted audio in a mp3 file named monica.mp3
myobj.save(my_file+'.mp3')

# Playing the converted file
os.system('afplay '+my_file+'.mp3')
# load an mp3 file
#mp3 = Mpg123('monica.mp3')

# use libout123 to access the sound device
#out = Out123()

#for frame in mp3.iter_frames(out.start):
#    out.play(frame)