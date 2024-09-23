# Copyright 2024 Dallas Wade
# Voice to txt script in python using WitAI Speech Recognition
# REQUIRES INTERNET CONNECTION

import speech_recognition as sr
import pyttsx3
import os
from dotenv import load_dotenv

#Reading in needed intro and help files
with open("intro.txt", "r") as file:
    introtext = file.read()
with open("helptext.txt", "r") as file:
    helptext = file.read()

# Initializing recognizer, loading and creating variable for environ variable WIT_API_KEY
r = sr.Recognizer()
load_dotenv()
key = os.getenv('API_KEY')

# Printing introdution
print(introtext)

# Records text from source
def record_text():

    while(1):
        try:
            with sr.Microphone() as source2:
                
                r.adjust_for_ambient_noise(source2, duration=0.2)
                audio2 = r.listen(source2)

                Text = r.recognize_wit(audio2, key)

                # Checks for help request
                if Text.lower() == "help": 
                    print(helptext)
                
                return Text

        except sr.RequestError as e:
            print("Could not request results; {0}".format(e))
        except sr.UnknownValueError:
            print("Waiting")

    return

# Outputs text into a file
def output_text(text, f):

    f.close()
    f = open(file, "a")
    f.write(text)
    f.write("\n")
    f.close()

while(running):
    print("Do you want to overwrite a file or add to one?\n1. Overwrite \n2. Add" )

    askagain = True

    # Repeats question until user says acceptable choice
    while askagain:
        choice = record_text()
        if choice.lower() == "one":
            writetype = "w"
            askagain = False

        elif choice.lower() == "two":
            writetype = "a"
            askagain = False

        elif choice.lower() == "restart":
            break

        else: print("Please say \"One\" or \"Two\"\nDo you want to overwrite a file or add to one?\n1. Overwrite \n2. Add")

    print("What is the name of the file you would like to alter?")

    filename = record_text().lower()

    if choice.lower() == "restart":
        break

    file = filename + ".txt"

    running = True

    # Ensures user doesnt alter helptext file, 
    while file == "helptext.txt" or file == "help.txt": 
        print("What is the name of the file you would like to alter?")
        filename = record_text().lower()

        if choice.lower() == "restart":
            break

        file = filename + ".txt"

    f = open(file, writetype)

    print("Say \"Quit\" to stop the program")

    # Running loop, saying Quit changes running value and stops program
    while(running):

        text = record_text()
        
        if text.lower() == "quit": 
            print("Closing")
            running = False

        elif text.lower() == "help": 
            print(helptext)

        else:
            output_text(text, f)
            print("Wrote text")
