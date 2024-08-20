import speech_recognition as sr
import os
import datetime
import speech_recognition as sr
import os
import datetime

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")  # Uncommented to provide user feedback
        r.pause_threshold = 1  # Uncommented to set the pause threshold
        audio = r.listen(source)
        try:
            print("Recognizing your voice...")
            query = r.recognize_google(audio, language='en-in')
            print(f"User input: {query}\n")
            return query
        except Exception as e:
            print("Sorry, I am unable to recognize your voice.")  # Changed to print the error message
            return None  # Changed to return None for clarity

    # The following code should be part of a different function or block as it's unreachable in its current position
    # extractedTime = open("Alarm.txt", "rt")
    # time = extractedTime.read()
    # time = str(time)
    # extractedTime.close()

    # deletetime = open("Alarm.txt", "r+")
def ring(time):
    timeset = str(time)
    timenow = timeset.replace("jarvish", "")
    timenow = timenow.replace("set an alarm", "")
    Alarmtime = str(timenow).strip()  # Added strip() to remove any leading/trailing spaces
    print(Alarmtime)
    while True:
        currentime = datetime.datetime.now().strftime("%H:%M")  # Fixed missing format string
        if currentime == Alarmtime:
            print("Alarm ringing!")  # Added action when alarm time matches current time
            break  # Exit the loop when the alarm time is reached

# this code will be executed later leave it please
