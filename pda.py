# python-3.6.8rc1-amd64
from playsound import playsound
import time
import pyttsx3
import socket
import webbrowser
import smtplib
import random
import speech_recognition as sr
import wikipedia
import datetime
import wolframalpha
import os
import sys
import os.path
from googletrans import Translator
from myWeatherForcaster import getWeatherForcastByAddress as wf
from myISP import getISPInfo as net_info
from myISP import getInternetSpeed as net_speed
from soundRecorder import record_voice
import youtube_browser


is_asking_question = False
engine = pyttsx3.init('sapi5')
client = wolframalpha.Client('G622EJ-GYP66G66XL')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[len(voices)-1].id)
user_profile = os.getenv('USERPROFILE')
cwd = os.getcwd()
current_location = "koronadal"

ainame = "sam"
#ainame = "JARVIS"
#ainame = "VERONICA"
#ainame = "FRIDAY"
#ainame = "LUCY"
#ainame = "shyam"

def getLocalIPAddress():
    hostname = socket.gethostname()
    return socket.gethostbyname(hostname)


def speak(audio):
    print('AI: ' + audio)
    engine.say(audio)
    engine.runAndWait()

def greetMe():
    currentH = int(datetime.datetime.now().hour)
    if currentH >= 0 and currentH < 12:
        speak('Good Morning!')

    if currentH >= 12 and currentH < 18:
        speak('Good Afternoon!')

    if currentH >= 18 and currentH !=0:
        speak('Good Evening!')

greetMe()

speak('Hi! I\'m ' + ainame + ', Your personal digital assistant. How may I help you?')

def myCommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print(" ... ")
        r.pause_threshold =  1
        r.dynamic_energy_threshold = False

        audio = r.listen(source)
        print(" .. ")
    try:
        query = r.recognize_google(audio, language='en-in')
        #query = r.recognize_bing(audio, language='en-in')
        

        print('User: ' + query + '\n')
        with open("latest_query.wav", "wb") as f:
            f.write(audio.get_wav_data())
            
    except sr.UnknownValueError:
        #speak('Sorry sir! I didn\'t get that! Try typing the command!')
        query = "none"
        print(query)

    return query.lower()


if __name__ == '__main__':

    while True:

        query = myCommand()
        query = query.lower()

        #Youtube browser -------------------------------------------------------------------------
        if 'open youtube' in query:
        	global yt
        	yt = youtube_browser.youtube('none')
        	yt.open()
        	speak("Youtube is ready.")

        if 'close youtube' in query:
        	if yt.close():
        		speak("Youtube closed.")
        	else:
        		speak("Im sorry sir, I can only close application you told me to open.")

        if 'search for ' in query:
        	keyword = query.replace('search for ','')
        	if yt.search(keyword):
        		if yt.waitForSearchResult():
        			cnt = yt.getResultCount()
        			speak(str(cnt) + " videos found!")

        if 'open link' in query:
        	keyword = query.replace('open link ','')
        	if not yt.link_click(keyword.title()):
        		speak("Im sorry sir, I cant find the link")

        if 'scroll down' in query:
        	yt.scroll_down()
        	
        if 'scroll up' in query:
       		yt.scroll_up()

       	if 'download this video' in query:
       		speak('Downloading video, please wait for a moment')
       		yt.download_video()
       		speak('Downloading is complete')

       	#knowledge base -------------------------------------------------------------------------

        elif 'analyze' in query:
            speak("What do you want me to analyze sir?")
            keyword = myCommand()
            try:
                res = client.query(keyword)
                speak("The result is: "+ str(next(res.results).text))
            except:
                speak("I'm sorry, I couldn't the best answer for your query!")

        elif 'tell me' in query:
            #speak("What do you want me to tell you about sir?")
            #keyword = myCommand()
            keyword = query.replace("tell me", "")
            try:
                res = client.query(keyword)
                speak(random.choice(["The result is: ","Heres what i got, "]) + str(next(res.results).text))
            except:
                speak("I'm sorry, I couldn't the best answer for your query!")


        elif 'translate' in query:
            lang = {'afrikaans':'af','albanian':'sq','amharic':'am','arabic':'ar','armenian':'hy','azerbaijani':'az','basque':'eu','belarusian':'be','bengali':'bn','bosnian':'bs','bulgarian':'bg','catalan':'ca','cebuano':'ceb','chichewa':'ny','chinese (simplified)':'zh-cn','chinese (traditional)':'zh-tw','corsican':'co','croatian':'hr','czech':'cs','danish':'da','dutch':'nl','english':'en','esperanto':'eo','estonian':'et','filipino':'tl','finnish':'fi','french':'fr','frisian':'fy','galician':'gl','georgian':'ka','german':'de','greek':'el','gujarati':'gu','haitian creole':'ht','hausa':'ha','hawaiian':'haw','hebrew':'iw','hindi':'hi','hmong':'hmn','hungarian':'hu','icelandic':'is','igbo':'ig','indonesian':'id','irish':'ga','italian':'it','japanese':'ja','javanese':'jw','kannada':'kn','kazakh':'kk','khmer':'km','korean':'ko','kurdish (kurmanji)':'ku','kyrgyz':'ky','lao':'lo','latin':'la','latvian':'lv','lithuanian':'lt','luxembourgish':'lb','macedonian':'mk','malagasy':'mg','malay':'ms','malayalam':'ml','maltese':'mt','maori':'mi','marathi':'mr','mongolian':'mn','myanmar (burmese)':'my','nepali':'ne','norwegian':'no','pashto':'ps','persian':'fa','polish':'pl','portuguese':'pt','punjabi':'pa','romanian':'ro','russian':'ru','samoan':'sm','scots gaelic':'gd','serbian':'sr','sesotho':'st','shona':'sn','sindhi':'sd','sinhala':'si','slovak':'sk','slovenian':'sl','somali':'so','spanish':'es','sundanese':'su','swahili':'sw','swedish':'sv','tajik':'tg','tamil':'ta','telugu':'te','thai':'th','turkish':'tr','ukrainian':'uk','urdu':'ur','uzbek':'uz','vietnamese':'vi','welsh':'cy','xhosa':'xh','yiddish':'yi','yoruba':'yo','zulu':'zu','Filipino':'fil','Hebrew':'he'}

            speak("What is the word of phrase do you want me to translate sir?")
            phrase = myCommand()

            speak("translate to what language sir?")
            given_lang = myCommand()
            selected_lang = "";
            if given_lang in lang:
                selected_lang = lang[given_lang]
                translator = Translator()
                trans = translator.translate(phrase, dest=selected_lang)

                if not phrase == trans.pronunciation:
                    speak("It's translation in " + given_lang + " is "  + trans.pronunciation)
                else:
                    speak("Im sorry sir, I cant translate " + phrase + " to " + given_lang)

            else:
                if not selected_lang == 'none'  or not selected_lang == '':
                    speak("Sir, " + selected_lang + " is not a language!")
                else:
                    speak("you didnt tell me the language sir! Bye!")


       	#internet and network information -------------------------------------------------------

        elif 'what is your IP' in query:
            localIP = getLocalIPAddress()
            speak("The local IP Address is " + localIP)

        elif 'what is your public IP' in query:
            speak("Just a moment sir!")
            res = net_info()

            if res[3] == 0:
                speak("Im sorry sir, I cant get your IP address information. Please check your internet connection")                
            else:    
                speak("The public IP Address is " + str(res[0]) + " and your internet service provider is " + res[1] + " with IPS rating of " + res[2])

        elif 'test internet speed' in query:
            speak("Just a moment sir!")
            res = net_speed()

            if res[7] == 0:
                speak("Im sorry sir, I cant connect to any server for your internet connection speed test. Please check your internet connection")                
            else:    
                speak("The public IP Address is " + str(res[0]) + " and your internet service provider is " + res[1] + " with IPS rating of " + res[2])
                speak("Heres the result: Your average connection speed is " + str(res[0]) + " megabytes per seconds, ")
                speak("with a upload speed of " + str(res[2]) + " and " + str(res[1]) + " download speed.")

                speak("Do you want me to display the result?")
                choice = myCommand()

                if 'yes' in choice:
                    browser.open(str(res[6]))

        elif 'test internet connection' in query:

            speak("Just a moment sir!")
            res = net_speed()

            if res[7] == 0:
                speak("It seems like your internet connection is lost.")                
            else:    
                response_time = str(res[3])
                sent   = str(res[4])
                received = str(res[5])
                lost = sent - received 

                speak("Heres the result: The response time is " + response_time + " megabytes per seconds.")

                if response_time > 200:
                    speak("Your internet connection seems slower than expected sir! I think you need to call your internet service provider")

        #Other commands -------------------------------------------------------------------------
        elif 'none' in query:
            pass

        elif 'activate sound recorder' in query:
            speak("Sound recorder activated.")
            record_voice()
            speak("Finished recording sir.")

        elif 'play last recorded audio' in query:
            playsound('records\\output.wav')

        elif 'activate ftp server' in query:
            localIP = getLocalIPAddress()
            os.system(cwd + "/tools/ftpdmin.exe root");
            speak("FTP Server activated! You can now access your resources from ftp://"+localIP)


        elif 'activate http tunnel' in query:
            os.system(cwd + '/tools/ngrok http 80')
            speak('http tunnel activated! You can now access your resources from anyware. But you only have 8 hours to use it.')
            speak('Please refer to the NG-ROK console for more information')



        elif 'what time is it' in query or 'time check' in query :
            atime = datetime.datetime.now()
            ahour = atime.hour
            aminutes = atime.minute
            speak("It's " + str(aminutes) + " minutes pass the hour of " + str(ahour))

        elif 'show command list' in query:

            speak("Listed below are the available commands")

            print("-------------------------------------------------")
            print("SHOW COMMAND LIST - Show this command list")

            print("OPEN YOUTUBE - Open youtube")
            print("CLOSE YOUTUBE - Close youtube")
            print("SCROLL DOWNLOAD - Scroll page up")
            print("SCROLL DOWNLOAD - Scroll page down")
            print("CLOSE YOUTUBE - Close youtube")
            print("SEARCH FOR [KEYWORD] - Search for youtube video")
            print("OPEN LINK [KEYWORD] - Open hyperlink")
            print("DOWNLOAD THIS VIDEO - Download youtube video")

            print("YOUTUBE SEARCH - Search for youtube video")
            print("ACTIVATE SOUND RECORDER - Record sounds")
            print("PLAY LAST RECORDED VIDEO - Play recoded sound")
            print("ANALYZE - try to answer knowledgebase questions, algorithms, arithmetic")
            print("TRANSLATE - translate english language to any language")
            print("TIME CHECK - tell the current time")
            print("EXPLAIN FUNCTIONALITIES - explains this functionalities")
            print("LOCATE - try to find location in google maps")
            print("IDENTIFY YOURSELF - self identification")
            print("SEND EMAIL - send email message")
            print("HELLO "+ainame+" - greet "+ainame)
            print("GOODBYE "+ainame+" - shutdown ai")
            print("PLAY MUSIC - play mp3 files")
            print("WEATHER FORECAST PLEASE - Tell the current weather advisory")
            print("CAN I ASK A QUESTION - try to answer questions")
            print("TIME CHECK - tell the current time")
            print("TEST INTERNET CONNECTION - ping test")
            print("TEST INTERNET SPEED - bandwidth test")
            print("WHAT IS YOUR IP - tell the local ip address")
            print("WHAT IS YOUR PUBLIC IP - tell the public ip address")
            print("ACTIVATE HTTP TUNNEL - create an http tunnel using port 80")
            print("ACTIVATE FTP SERVER - create an FTP server (can be access in local network)")

            print("")
            print(" ** you may ask any quetion that starts with 'TELL ME' ** ")
            print("")

            print("-------------------------------------------------")

        elif 'open notepad' in query:
            os.system('notepad')
        elif 'open calculator' in query:
            os.system('calc')
        elif 'open microsoft word' in query:
            os.system('winword')
        elif 'open microsoft excel' in query:
            os.system('excel')
        elif 'open microsoft powerpoint' in query:
            os.system('POWERPNT')

        elif 'shutdown computer' in query:
            speak("Are you sure you wan to shutdown this computer? If you do you will also shutdown me.")
            while True:
                shutdown_confirm = myCommand()
                if 'yes' in shutdown_confirm:
                    speak("System will shutdown in 30 seconds.")
                    os.system('shutdown -f -s -t 30')
                elif 'no' in shutdown_confirm:
                    speak('shutdown aborted')
                    break;
                elif 'abort' in shutdown_confirm or 'stop' in shutdown_confirm:
                    os.system('shutdown -f -s -t 30')
                    speak('shutdown aborted')
                    break;

        elif 'restart computer' in query:
            speak("Are you sure you wan to restart this computer?")
            while True:
                shutdown_confirm = myCommand()
                if 'yes' in shutdown_confirm:
                    speak("System will reboot in 30 seconds.")
                    os.system('shutdown -f -r -t 30')
                elif 'no' in shutdown_confirm:
                    speak('restart aborted')
                    break;
                elif 'abort' in shutdown_confirm or 'stop' in shutdown_confirm:
                    os.system('shutdown -f -s -t 30')
                    speak('restart aborted')
                    break;

        elif 'explain functionalities' in query:
            str =  "My Creator tell be to do the following functions. "
            str += "Open web browser and send email. "
            str += "search, play, and download youtube video. "
            str += "find locations. "
            str += "tell the current time and play any music you wish. "
            str += "You may ask me anything you want, I will do my best to answer you questions. "
            str += "translate anything you say to any language. "
            str += "Compute expert-level algorithms, knowledgebase and AI technology. "
            str += "record voinces from the Microphone and play recorded audio. "
            str += "tell the current weather forecast."
            str += "conduct netword and internet diagnostic test."
            str += "tell the public and private ip addresses."

            speak(str)
        elif 'how is the weather today' in query or 'weather forecast please' in query:
            speak(wf(current_location))


        elif 'locate ' in query:
            speak(query.split(' ', 1)[1].strip() + ' found, openning google maps for you')
            webbrowser.open('https://www.google.com/maps/place/'+query.split(' ', 1)[1].strip())

        elif 'open google' in query:
            speak(random.choice({'okay sir!','right away sir!','affirmative!'}))
            webbrowser.open('www.google.com')

        elif 'who are you' in query or 'identify yourself' in query :
            speak('Im '+ainame+', your personal digital assistant!')

        elif 'open gmail' in query:
            speak(random.choice({'okay sir!','right away sir!','affirmative!'}))
            webbrowser.open('www.gmail.com')

        elif "what\'s up" in query or 'how are you' in query:
            stMsgs = ['Just doing my thing!', 'I am fine!', 'Im good!', 'I am nice and full of energy']
            speak(random.choice(stMsgs))

        elif 'send email' in query:
            speak('Who is the recipient? ')
            recipient = myCommand()

            if 'me' in recipient:
                try:
                    speak('What would be the content of your message?')
                    content = myCommand()
                    content = 'Subject: {}\n\n{}'.format("PSD Send test", "Hello this is a test from my personal digital assistant.")

                    server = smtplib.SMTP('smtp.gmail.com', 587)
                    server.ehlo()
                    server.starttls()
                    server.login("alden.roxy@gmail.com", 'kalilinux4891021408271209')
                    server.sendmail('Alden Quinones', "Alden Quinones", content)
                    server.close()
                    speak('Email successfully sent sir!')

                except:
                    speak('Sorry Sir! I am unable to send your message at this moment!')

            else:
                speak('Im sorry sir, for now, i can only send mail to you. not to anyone else.')

        elif 'hello '+ainame in query or ainame+ ' are you there' in query or 'hi '+ainame in query:
        	playsound(cwd+'\\sounds\\blip.mp3')
        	speak(random.choice(['At your service sir','How may I help you sir?','Yes sir? You need something?']))

        elif 'goodbye '+ainame in query or 'nothing' in query  or 'goodbye' in query:
            speak('goodbye sir, ' + random.choice(['have a nice day.','see you soon','see you later','until next time','take care']))
            sys.exit()

        elif 'play music' in query:
            music_folder = user_profile+"\\Music\\"
            #music = ["eye of the tiger", "i_need_a hero"]
            #random_music = music_folder + random.choice(music) + '.mp3'
            #os.system(random_music)
            speak('What is the title of the music?')
            mp3_title = myCommand()

            if os.path.exists(music_folder+mp3_title+'.mp3'):
	            speak('Playing '+mp3_title+' for you. Enjoy the music')
	            playsound(music_folder+mp3_title+'.mp3')
            else:
                pass
                speak('Im sorry sir, I cant find the music you want to play!')
        elif 'can i ask a question' in query or 'i have a question' in query or 'can i ask you a question' in query:
            is_asking_question = True
            speak('what is your question sir?')

        elif query != '' and is_asking_question:
            speak('Just a moment sir!')
            try:
                try:
                    res = client.query(query)
                    results = next(res.results).text
                    #speak('WOLFRAM-ALPHA says - ')
                    #speak('Got it.')
                    speak('The result is!')
                    speak(results)

                except:
                    results = wikipedia.summary(query, sentences=2)
                    #speak('Got it.')
                    #speak('WIKIPEDIA says - ')
                    speak('heres what i got!')
                    speak(results)

            except:
            	speak('Im Sorry, I cant find what you are looking for')

            speak("Do you have any more question?")
            response = myCommand()

            while True:
                if 'no' in response:
                    is_asking_question = False
                    break
                if 'yes' in response:
                    break
                if 'pardon' in response:
                    speak("Do you have any more question?")
                    response = myCommand()


        else:
        	pass
        #speak('Next Command! Sir!')
print('Im out')