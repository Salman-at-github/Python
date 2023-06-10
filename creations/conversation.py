from textToSpeechFunc import maleSpeaker,femaleSpeaker

femaleSpeaker("Enter what you want to hear:")
text = input("Enter what you want to hear: ")

femaleSpeaker("Choose a voice. Type M for Male, F for female")
choice = input("Enter the voice choice: ")

if choice.lower()=="m":
    maleSpeaker(text)
elif choice.lower()=="f":
    femaleSpeaker(text)
else:
    print("Please choose the right voice method")
    femaleSpeaker("Please choose the right voice method")