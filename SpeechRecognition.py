import speech_recognition as sr

listener = sr.Recognizer()

with sr.Microphone() as input_source:
    print("I am Listening....")
    voice_input = listener.listen(input_source)
    text = listener.recognize_google(voice_input)
    print(text)