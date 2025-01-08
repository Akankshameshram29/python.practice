#NOVA virtual assistant which can listen to the command and open the application said by the user

import speech_recognition as sr
import webbrowser 
import pyttsx3 
from gtts import gTTS
import pygame
import io

recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak_old(text):
    engine.say(text)
    engine.runAndWait()



def processCommand(c):
    # Convert the command to lower case for case insensitive matching
    command = c.lower()
    
    # Check if the command contains "open"
    if "open " in command:
        # Extract the part of the command after "open "
        site = command.split("open ")[1]
        
        # Construct the full URL
        if not site.startswith("http://") and not site.startswith("https://"):
            site = "https://" + site
        
        # Open the site in the web browser
        webbrowser.open(site)
    else:
        print("Command not recognized.")





def speak(text):
    # Initialize gTTS and convert text to speech
    tts = gTTS(text, lang='en')
    # Use an in-memory buffer to store the audio
    audio_buffer = io.BytesIO()
    # Write the audio data to the buffer
    tts.write_to_fp(audio_buffer)
    # Move the cursor to the beginning of the buffer
    audio_buffer.seek(0)
    
    # Initialize pygame mixer
    pygame.mixer.init()
    # Load the audio from the buffer
    pygame.mixer.music.load(audio_buffer, 'mp3')
    # Play the audio
    pygame.mixer.music.play()
    # Keep the script running while the audio is playing
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)


if __name__ == "__main__":
    speak("starting Nova...")  
    recognizer = sr.Recognizer()
    microphone = sr.Microphone()
    
    while True:
        try:
             with microphone as source:
                 recognizer.adjust_for_ambient_noise(source)
                 print("listening ...")
                 audio = recognizer.listen(source, timeout = 2)
                 word = recognizer.recognize_google(audio)
                 print(word)
                 if word.lower() == "nova": 
                     speak("HI,how can I help you?")
                     print("listening to the command")
                     audio = recognizer.listen(source, timeout=2) 
                     command = recognizer.recognize_google(audio)
                     processCommand(command)
        
        except sr.WaitTimeoutError:
            print("Listening timed out while waiting for phrase to start")
        except sr.UnknownValueError:
            print("Could not understand the audio")
        except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition service; {e}")
        except Exception as e:
            print("Error; {0}".format(e))