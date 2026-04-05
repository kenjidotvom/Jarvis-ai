import speech_recognition as sr
from openai import OpenAI
import datetime
from playsound import playsound
import os
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

def speak(text):
    print("Jarvis:", text)

    speech_file_path = "jarvis.mp3"

    with client.audio.speech.with_streaming_response.create(
        model="tts-1",
        voice="alloy",
        input=text
    ) as response:
        response.stream_to_file(speech_file_path)

    playsound(speech_file_path)

def listen():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        try:
            audio = r.listen(source, timeout=5)
        except sr.RequestError:
            return ""
    
    try:
        command = r.recognize_google(audio)
        print("You:", command)
        return command.lower()
    except sr.UnknownValueError:
        print("Could not understand audio")
        return ""
    except sr.RequestError:
        print("Could not request results from Google Speech Recognition")
        return ""

speak("Jarvis online. Hello Lucas, how can I help you?")

while True:
    command = listen()

    if command == "":
        continue

    elif "hello" in command:
        speak("Hello Lucas. I am ready.")

    elif "time" in command:
        time = datetime.datetime.now().strftime("%I:%M %p")
        speak(f"The time is {time}")

    elif "who are you" in command:
        speak("I am Jarvis, your personal AI assistant.")

    elif "stop" in command or "shutdown" in command:
        speak("Goodbye Lucas.")
        break

    else:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are Jarvis, a helpful AI assistant that speaks like Iron Man's assistant."},
                {"role": "user", "content": command}
            ]
        )

        reply = response.choices[0].message.content
        speak(reply)