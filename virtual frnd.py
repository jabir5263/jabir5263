import pyttsx3
friend = pyttsx3.init()
speech = input("Say anything : ")
friend.say("Hello. I am reading what you entered.")
print("Hello. I am reading what you entered.")
friend.say(speech)
print("\n                 You entered : " , speech)

friend.runAndWait()
print("                       good bye")