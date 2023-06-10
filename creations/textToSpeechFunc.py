import pyttsx3


def maleSpeaker(text):
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)
    engine.say(text)
    engine.runAndWait()

def femaleSpeaker(text):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    for voice in voices:
        if "Zira" in voice.name:
            engine.setProperty('voice', voice.id)
            break
    engine.setProperty('rate', 150) #rate of speech, default is 200
    engine.say(text)
    engine.runAndWait()

if __name__ == '__main__':
    maleSpeaker("Here's an example code:")

    femaleSpeaker("You can control the speed of the spoken words using the setProperty method of the pyttsx3 engine object. You can set the value of the rate property to a number between 0 and 400 to control the speaking rate. The default value is 200.")
    maleSpeaker("I am still in charge here.")
        