import speech_recognition as sr
import pyttsx3
import os
import webbrowser
import datetime

# --------- SPEAK ENGINE ----------
engine = pyttsx3.init()
engine.setProperty('rate', 170)

def speak(text):
    engine.say(text)
    engine.runAndWait()

# --------- LISTEN FUNCTION (Continuous + Reliable) ----------
def listen():
    r = sr.Recognizer()
    # Mic devices list (for troubleshooting)
    # print(sr.Microphone.list_microphone_names())
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration=1.5)  # Calibrate noise
        print("🎤 Listening...")
        try:
            audio = r.listen(source, timeout=5, phrase_time_limit=7)
        except sr.WaitTimeoutError:
            return ""
    try:
        command = r.recognize_google(audio).lower()
        print("You said:", command)
        return command
    except sr.UnknownValueError:
        return ""
    except sr.RequestError as e:
        print("❌ Could not request results; {0}".format(e))
        return ""

# --------- MAIN PROGRAM ----------
WAKE_WORD = "abhim"
speak("Hello, I am Abhim. Say my name to give commands.")

while True:
    command = listen()

    if WAKE_WORD in command:
        speak("Yes, tell me")
        cmd = listen()

        if "open chrome" in cmd:
            speak("Opening Chrome")
            os.startfile("C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe")

        elif "open notepad" in cmd:
            speak("Opening Notepad")
            os.system("notepad")

        elif "open youtube" in cmd:
            speak("Opening YouTube")
            webbrowser.open("https://youtube.com")

        elif "time" in cmd:
            now = datetime.datetime.now().strftime("%I:%M %p")
            speak(f"The time is {now}")

        elif "shutdown" in cmd:
            speak("Shutting down the system")
            os.system("shutdown /s /t 5")

        elif "exit" in cmd or "stop" in cmd:
            speak("Goodbye")
            break

    elif command != "":
        # Optional: respond to direct commands without wake word
        if "open notepad" in command:
            speak("Opening Notepad")
            os.system("notepad")
        elif "time" in command:
            now = datetime.datetime.now().strftime("%I:%M %p")
            speak(f"The time is {now}")
