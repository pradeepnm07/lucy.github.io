from pywhatkit.main import search
import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
from GoogleNews import GoogleNews
import webbrowser
import subprocess

googlenews = GoogleNews()
listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'lucy' in command:
                command = command.replace('lucy', '')
                print(command)
    except:
        pass
    return command

def run_lucy():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)

    elif 'search information' in command:
        search = command.replace('search', '')
        talk('opening information' + search)
        pywhatkit.search(search)

    elif 'open images of' in command:
        image = command.replace('open', '')
        talk('opening ' + image)
        pywhatkit.search(image)

    elif 'what is the time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is ' + time)

    elif 'how is the weather condition' in command:
        b='opening todays wheather report'
        engine.say(b)
        engine.runAndWait()
        webbrowser.open('https://www.accuweather.com/en/in/india-weather')

    elif 'today headlines' in command:
        engine.say('Getting news for you ')
        engine.runAndWait()
        googlenews.get_news('Today news')
        googlenews.result()
        a=googlenews.gettext()
        print(*a[1:5],sep=',')

    elif 'tech' in command:
        engine.say('Getting news for you ')
        engine.runAndWait()
        googlenews.get_news('Tech')
        googlenews.result()
        a=googlenews.gettext()
        print(*a[1:5],sep=',')

    elif 'sports' in command:
        engine.say('Getting news for you ')
        engine.runAndWait()
        googlenews.get_news('sports')
        googlenews.result()
        a=googlenews.gettext()
        print(*a[1:5],sep=',')

    elif 'youtube' in command:
        b='opening youtube'
        engine.say(b)
        engine.runAndWait()
        webbrowser.open('www.youtube.com')

    elif 'cricket live score' in command:
        b='showing cricket live scores'
        engine.say(b)
        engine.runAndWait()
        webbrowser.open('https://m.cricbuzz.com/cricket-match/live-scores')

    elif 'directions' in command:
        b='opening directions to your destination'
        engine.say(b)
        engine.runAndWait()
        webbrowser.open('https://www.google.com/maps')

    elif 'download app' in command:
        d='opening playstore'
        engine.say(d)
        engine.runAndWait()
        webbrowser.open('https://play.google.com/store/apps')     

    elif 'open mail' in command:
        g='opening your mail'
        engine.say(g)
        engine.runAndWait()
        webbrowser.open('https://mail.google.com/mail/u/0/?tab=rm&ogbl#inbox')

    elif 'instagram' in command:
        b='opening instagram'
        engine.say(b)
        engine.runAndWait()
        webbrowser.open('https://www.instagram.com/accounts/login/')

    elif 'facebook' in command:
        b='opening facebook'
        engine.say(b)
        engine.runAndWait()
        webbrowser.open('https://www.facebook.com/login/')

    elif 'book a ticket' in command:
        b='booking ticket for you'
        engine.say(b)
        engine.runAndWait()
        webbrowser.open('https://www.makemytrip.com/bus-tickets/')

    elif 'send message' in command:
        pywhatkit.sendwhatmsg("+919916865665","Hello",19, 10)
        print("Successfully Sent!")

    elif 'chrome'in command:
        a='Opening chrome..'
        engine.say(a)
        engine.runAndWait()
        programName = "C:\Program Files\Google\Chrome\Application\chrome.exe"
        subprocess.Popen([programName])

    elif 'who is' in command:
        person = command.replace('who is', '')
        info = wikipedia.summary(person, 2)
        print(info)
        talk(info)

    elif 'tell me about' in command:
        welcome = command.replace('searching', '')
        info = wikipedia.summary(welcome, 2)
        print(info)
        talk(info)

    elif 'date' in command:
        talk('sorry, I have a headache')
    
    elif 'are you single' in command:
        talk('I am in a relationship with wifi')
    
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    
    else:
        talk('Please say the command again.')

while True:
    run_lucy()
