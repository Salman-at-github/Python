import win32com.client

def maleSpeaker(text):
    speaker = win32com.client.Dispatch("SAPI.SpVoice")
    voices = speaker.GetVoices()
    for voice in voices:
        if voice.GetDescription().startswith("Microsoft David"):
            speaker.Voice = voice
            break
    speaker.Rate = 1 # set speaking rate to normal speed
    speaker.Speak(text)

def femaleSpeaker(text):
    speaker = win32com.client.Dispatch("SAPI.SpVoice")
    voices = speaker.GetVoices()
    for voice in voices:
        if voice.GetDescription().startswith("Microsoft Zira"):
            speaker.Voice = voice
            break
    speaker.Rate = 0.8 # set speaking rate to slower speed
    speaker.Speak(text)

maleSpeaker("Wow! This is working!")
femaleSpeaker("In the maleSpeaker function, we use the win32com.client.Dispatch method to create a SAPI.SpVoice object, which represents the Windows Speech API. We then use the GetVoices method to get a list of available voices, and loop through them to find the voice with the name Microsoft David.")