import speech_recognition as sr
import pyttsx3

recognizer = sr.Recognizer()

while True:
    try:
        with sr.Microphone() as mic:
            recognizer.adjust_for_ambient_noise(mic, duration=0.2)
            audio = recognizer.listen(mic)
            text = recognizer.recognize_google(audio)
            text = text.lower()
            print(f'Recording: {text}')
            
    except sr.UnknownValueError:
        recognizer = sr.Recognizer()
        continue
    except sr.WaitTimeoutError:
        print("Listening timeout. Restarting...")
        continue
    except sr.RequestError as e:
        print(f"An error occurred: {e}")
        break 
