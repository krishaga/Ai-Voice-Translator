import speech_recognition as sr
import pyttsx3
from googletrans import Translator

def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        try:
            recognizer.pause_threshold = 0.5
            audio = recognizer.listen(source)
            text = recognizer.recognize_google(audio)
            print("You said -", text)
            return text
        except Exception as e:
            print("Sorry, I could not understand. Error:", e)
            return None

def speak(text, language='en'):
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)
    engine.setProperty('volume', 1.5)
    if language == 'kn':
        engine.setProperty('voice', 'english+f5')
    engine.say(text)
    engine.runAndWait()

def translate_to_kannada(text):
    translator = Translator()
    try:
        translated_text = translator.translate(text, dest='kn')
        return translated_text.text
    except AttributeError as e:
        print("AttributeError occurred during translation:", e)
    except Exception as e:
        print("An error occurred during translation:", e)
    return None

def translate_to_hindi(text):
    translator = Translator()
    try:
        translated_text = translator.translate(text, dest='hi')
        return translated_text.text
    except AttributeError as e:
        print("AttributeError occurred during translation:", e)
    except Exception as e:
        print("An error occurred during translation:", e)
    return None

def main():
    while True:
        user_input = listen()
        if user_input:
            if "bye" in user_input.lower():
                response = "Bye-bye, it's time to sleep."
                speak(response)
                break
            else:
                translated_input_kannada = translate_to_kannada(user_input)
                translated_input_hindi = translate_to_hindi(user_input)
                if translated_input_kannada and translated_input_hindi:
                    print("Translated to Kannada:", translated_input_kannada)
                    print("Translated to Hindi:", translated_input_hindi)
                    speak(user_input, language='en')
                    speak("Translated to Kannada:", language='kn')
                    speak(translated_input_kannada, language='kn')
                    speak("Translated to Hindi:", language='hi')
                    speak(translated_input_hindi, language='hi')

if __name__ == "__main__":
    main()
