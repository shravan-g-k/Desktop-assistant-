import webbrowser
import pyttsx3
from datetime import datetime , date
import wikipedia as wiki
import speech_recognition as sr
import os


def speak(audio):
    """speaks the string input given in 'audio' argument """
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)#for male voice change the 1 to 0 for female it will be 1 
    engine.getProperty('rate')                          
    engine.setProperty('rate', 125)# speed of the voice can be controlled here[for a slower voice change rate to a smaller no, / for speeder one change the rate to a bigger number] 
    engine.say(audio)
    engine.runAndWait()

def wishme():
    """Whishes you good morining/afternoon/evening or hi how are according to time """
    #Date format is in 24 hour format 
    now = datetime.now()
    time = int(now.strftime("%H"))
    if time >= 5 and time <= 10 :#if time is more than 5 and less than 10 then it will speak goodmorning
        speak("Good Morning SKY") 
    elif time >= 11 and time <= 15 :#if time is more than 11 and less than 15 then it will speak goog afternoon
        speak("Good Afternoon SKY") 
    elif time >= 16 and time <= 19 :#if time is more than 16 and less than 19 then it will speak goog evening
        speak("Good evening SKY") 
    else :#if time is not either in ine of them then it would be night  ,Hence it will speak hi how are sky 
        speak("hi, how are you SKY")
    speak("What can i do for you ")


def speech():
    """returns the words the user has said as string 
        It is set to use google recogniton tool if you want to change then check out https://pypi.org/project/SpeechRecognition/"""
    r = sr.Recognizer()#creating object of the recognizer class 
    with sr.Microphone() as source :
        print("Listening . . . .")
        spoken_words = r.listen(source)
    try:#using try block because there are chances that the recognition tool may not be able to recognize your words so if any error  then it will run the except block 
        print("Recognizing . . .\n ")    
        final_words = r.recognize_google(spoken_words) #Using google for voice recognition
        print("You said:",final_words)  #the words spoken by user will be printed 
        return final_words

        #speak(f"you said{final_words}") # if you want your assistant to repeat the words you have said then uncomment this speak function

    except Exception :
        speak("Say that again please...")#if the try block runs with an error then it will speak say that again   
        return speech()


if __name__ == "__main__" :
    wishme()
    while True:
        words = speech().lower()#lowering all the output we get in google recogniton so that it will be easy for us to use that in our program
        if "wiki" in words or "search" in words :
            speak("what do you want to search in wikipedia ,. just tell the key word")
            words = speech().lower()
            result = wiki.summary(words,sentences = 3)
            print(result)
            speak(result)
        elif "time" in words :#this block prints the current time & repeats it
            print(f'the current time is {datetime.now().strftime("%H hours : %M minutes ")} ')
            speak(f'the current time is {datetime.now().strftime("%H hours : %M minutes ")} ')
        elif "date" in words or "day" in words :#this block prints todays date and repeats it 
            print(f'todays date is {date.today()} ')
            speak(f'todays date is {date.today()} ')
        elif "google" in words :#you make more apps to open by creating more blocks of these      
            os.startfile("C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Google Chrome.lnk")
            speak("opening google ..... please wait ")
        elif "youtube" in words :#this is to open youtube using desktop assistant you can creaate more of these
            webbrowser.open("https://www.youtube.com")
            speak("opening YouTube .... please wait ")
        else :
            pass 
