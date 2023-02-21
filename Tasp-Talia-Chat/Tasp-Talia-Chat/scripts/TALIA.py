# TALIA Chat aka Totally Artificial Language Intelligence Assistant Chat Edition
import pyfiglet
from neuralintents import GenericAssistant
import matplotlib.pyplot as plt
import pandas_datareader as web
import mplfinance as mpf
import pickle
import sys
import datetime as dt
import os
import threading
import datetime
import requests
import pyjokes
import pyttsx3
import calendar
import time
import wikipedia
import urllib.request
import re 
import webbrowser
from phue import Bridge
from ph_ip_address import bridge_ip_address
from googletrans import Translator, constants
from pprint import pprint
from requests_html import HTMLSession
from bs4 import BeautifulSoup as soup
import requests
from tqdm import tqdm
import pyautogui
import speedtest
from colorama import Fore, Back, Style
import random
import curses
import pyqrcode
import platform
import csv, re
import cv2
from PIL import Image
from playsound import playsound
import calendar
import randfacts
import subprocess
import cmath

# info
version_name = "v3.0.7-public-beta-preview"
last_update = "19/02/23"


engine = pyttsx3.init()
engine.setProperty('rate', 220) 

def TALIA_main():
    import time
    #For linux
    #os.chdir("..")
    with open('data/portfolio.pkl', 'rb') as f:#Access the prebuilt portfolio containing APPL & TSLA
        portfolio = pickle.load(f)
        print('\033[1;37m')
        welcome = pyfiglet.figlet_format("Welcome To T.A.L.I.A Chat!")
        print(welcome)
        engine.say("Welcome To Talia Chat!")
        import time
        time.sleep(2)
        print(r"""                                                                                                                                                                                                      
               .^~!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!~^.               
              ^!77!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!77!^              
             .!?7:                                                     :7?!.             
             .!?7:                                                    :7?!.                          
             .!?7:                                                    :7?!.             
             .!?7:             ....                  ....             :7?!.             
             .!?7:          .~J5PP5J~.            .~J5PP5J~.          :7?!.             
             .!?7:          !5PPPPPPP7            7PPPPPPP5!          :7?!.             
             .!?7:          7PPGPPGPP7            ?PGGPPGPP7          :7?!.             
             .!?7:          .~J5PP5Y!:            :!Y5PP5J~.          :7?!.             
             .!?7:            .:^^:.                .:^^:.            :7?!.             
             .!?7:                                                    :7?!.             
             .!?7:                  ^!!7!77!!!7!7!!^                  :7?!.             
             .!?7:                  JGGGGGGGGGGGGGGJ                  :7?!.             
             .!?7:                  ?PPPPPPPPPPPPPP?                  :7?!.             
             .!?7:                  ^?PGPPPPPPPPGPJ~                  :7?!.             
             .!?7:                   :!YPPGGGGPPY7:                   :7?!.             
             .!?7:                     .^!7??7!^.                     :7?!.             
             .!?7:                                                    :7?!.             
             .7?7:                                                    :7?7.             
             .!?7:                                                    :7?!.             
              ^7?7!!!!!!!!!!!!!~^:              :!!!!!!!!!!!!!!!!!!!!!7?7^              
               .^!!77777777777777?!^.          .~??777777777777777777!~^.               
                               .:!?7~:        .~7?~.                                                
                                 .~??^       .^7?!.                                                 
                                 .!?7^     .^7?7~.                                                  
                               .^!?7~. .:^!7?7~:                                                    
                             :7?????77777?7!^.                                                      
                             :!!!~~~~~~^:.                                                          
 
""")
        print("-----------------------------------------------------")
        engine.say("Importing all preferences from home interface")
        
        for i in tqdm (range (101), #Update progress bar
               desc="Updating", 
               ascii=False, ncols=75):
            time.sleep(0.05)
        print("\n")
        print(Fore.CYAN +'Version: v3.0.7-public-beta-preview')
        print(Fore.WHITE)
        engine.say("Systems are now fully operational")
        engine.runAndWait()
        print(Fore.WHITE)
        print('Status: '+ Fore.GREEN + 'ONLINE')
        print(Fore.WHITE)
        now = datetime.datetime.now()
        print(now)
        print("\n")
        time.sleep(2)
        engine.say("Hi, How Can I Help?")
        print("Hi, How Can I Help? 💬")
        engine.runAndWait()

        def greeting():#Greets the user
            engine.say("Hi There!")
            print("Hi There! 👋")
            engine.runAndWait()

        def goodbye():
            engine.say("Bye! ")
            print("Bye! 👋")
            engine.runAndWait()
            sys.exit(0)

        def thanks():
            engine.say("You're Welcome")
            print("You're Welcome! 😇")
            engine.runAndWait()

        def name():
            engine.say("I'm TALIA")
            print("I'm TALIA 😇")
            engine.runAndWait()

        def tasp():
            engine.say("T.A.L.I.A stands for: Totally Artificial Language Intelligence System")
            print("T.A.L.I.A stands for: Totally Artificial Language Intelligence System 🙃")
            engine.runAndWait()

        def talia():
            engine.say("TALIA stands for: Totally Artificial Language Intelligence System")
            print("TALIA stands for: Totally Artificial Language Intelligence System 🙃")
            engine.runAndWait()

        def feeling():
            engine.say("I'm doing great thanks for asking")
            print("I'm Doing Great!")
            print("Thanks For Asking 😇 ")
            engine.runAndWait()

        def language():
            engine.say("I can only speak and understand English right now but I'm willing to learn other languages so I can assist more people")
            print("I can only speak and understand English right now")
            print("but I'm willing to learn other languages so I can assist more people 🧠")
            engine.runAndWait()


        def gettime():#Shows current time to user
            now = datetime.datetime.now()
            engine.say("The Current Time Is")
            print("The Current Time Is ⏰...")
            engine.say(now)
            print(now)
            engine.runAndWait()

        def date():#Shows the current date to user
            now = datetime.datetime.now()
            engine.say("The Date Today Is")
            print("The Date Today Is 📅...")
            engine.say(now)
            print(now)
            engine.runAndWait()

        def calendar():#Displays the calendar to the user
            import calendar
            response = input("What would you like to see, the year or the month 📅? ")
            if response in ["year", "the year"]:
                yy = int(input("Enter Year: "))
                print(calendar.calendar(yy))
            elif response in ["month", "the month"]:
                mm = int(input("Enter Month: "))
                yy = int(input("Enter Year: "))
                print("Here's Your Calendar Below 📅: ")
                print(calendar.month(yy, mm))
            else:
                print("ERROR, TRY AGAIN!!!")




        def weather():#Shows the weather for the user by using https://www.wttr.in/
            engine.say("Which City Would You Like The Weather For?")
            engine.runAndWait()
            location = input("Which City Would You Like The Weather For ☁️?")
            engine.say('This Is The Weather For: ' + location)
            print('This Is The Weather For: ' + location)
            engine.runAndWait()
            url = 'https://wttr.in/{}'.format(location)
            res = requests.get(url)
            print(res.text)
        
        def joke():#Shows a random joke to the user
            engine.say("Here Is A Joke")
            print("Here's A Joke 🤣...")
            new_joke = pyjokes.get_joke(language="en", category="all")
            engine.say(new_joke)
            print(new_joke)
            engine.runAndWait()

        def wiki():#Wikipedia Search
            engine.say("What would you like to wiki search?")
            engine.runAndWait()
            query = input("What would you like to wiki search? 🔍 ")
            print (wikipedia.summary(query))
            engine.say("According to Wikipedia...")
            engine.say (wikipedia.summary(query))
            engine.runAndWait()
            
        def youtube():#YouTube Search
            engine.say("What would you like to YouTube search?")
            engine.runAndWait()
            search_keyword = input("What would you like to YouTube search? 🔍 ")
            html = urllib.request.urlopen("https://www.youtube.com/results?search_query="+search_keyword)
            video_ids = re.findall(r"watch\?v=(\S{11})", html.read().decode())
            print("Here's what I found on YouTube 🌐...")
            engine.say("Here's what I found on YouTube...")
            print("https://www.youtube.com/watch?v="+video_ids[0])
            engine.runAndWait()



        def video():#Plays a video using ASCII style using ASCII_VID.py
            import ASCII_VID

        def image():
            import PIL
            from PIL import Image
            Characters = ["@", "#", "S", "%", "?", "*", "+", ";", ":", ",", "."]

            def update_image(image, update_width=100):
                width, height = image.size
                ratio = height/width
                update_height = int(update_width * ratio)
                update_image = image.resize((update_width, update_height))
                return(update_image)


            def greyscale(image):
                grayscale_image = image.convert("L")
                return(grayscale_image)
    

            def pixels(image):
                pixels = image.getdata()
                characters = "".join([Characters[pixel//25] for pixel in pixels])
                return(characters)    

            def main(update_width=100):
                engine.say("Enter file path")
                path = input("Enter File Path: \n")
                image = PIL.Image.open(path)
                update_image_data = pixels(greyscale(update_image(image)))

                number_of_pixels = len(update_image_data)  
                ascii_img = "\n".join([update_image_data[index:(index+update_width)] for index in range(0, number_of_pixels, update_width)])
    
                engine.say("Here is your image converted to ASCII style")
                print("Here Is Your Image Converted To ASCII Style 🖼️ : ")
                print(ascii_img)
                engine.runAndWait()
    
            main()

        def play_song():#Plays song through spotify
            import time
            engine.say("What song would you like to play?")
            song = input("What song would you like to play? 🎵 ")
            engine.runAndWait()
            os.system("spotify")
            time.sleep(5)
            pyautogui.hotkey('ctrl', 'l')
            pyautogui.write(song, interval = 0.1)
            for key in ['enter', 'pagedown', 'tab', 'enter', 'enter']:
                time.sleep(2)
                pyautogui.hotkey(key)
            print("Playing "+song+" on Spotify...")
            engine.say("Playing "+song+" on Spotify!")
            engine.runAndWait()
            

        def app():#NEED TO FIX!!!
            engine.say("What would you like to open?")
            response = input("What would you like to open? 🖥️ ")
            engine.say("Sorry Open Command is unavailable at the moment!")
            print(Fore.RED + 'Sorry Open Command is unavailable atm 😥!')
            print(Fore.WHITE)
            #if "youtube" or "yt" or "YouTube" or "you tube" or "You Tube" in response:
            #    engine.say("Opening YouTube...")
            #    webbrowser.open("youtube.com")
            #elif "google" in response:
            #    engine.say("Opening Google...")
            #    webbrowser.open("google.com")
            # "stackoverflow" or "stack overflow" in response:
            #engine.say("Opening Stackoverflow...")
            #    webbrowser.open("stackoverflow.com") 
            #elif "github" or "GitHub" in response:
            #    engine.say("Opening GitHub...")
            #    webbrowser.open("github.com")
            #elif "duckduckgo" in response:
            #    engine.say("Opening Duckduckgo...")
            #    webbrowser == ("duckduckgo.com")
            #else:
            #    engine.say("Sorry I don't understand!")
            #    print("Sorry I don't understand!")
            engine.runAndWait()
      
        def access_lights(bridge_ip_address):
            b = Bridge(bridge_ip_address)
            light_names_list = b.get_light_objects('name')
            return light_names_list

        def philips_hue():#Controls Philips Hue Lights
            b = Bridge(bridge_ip_address)
            b.connect()
            print("Here are the current lights you can control 💡:")
            engine.say("Here are the current lights you can control:")
            engine.runAndWait()
            lights = b.lights
            for l in lights:
                print(l.name)#Lists all available lights to control
                engine.say(l.name)
            engine.say("What would you like to do?")
            engine.runAndWait()
            response = input("What would you like to do 💬?")
            if response in ['turn off all lights', 'turn off', 'turn off light']:#Turns off lights
                lights = access_lights(bridge_ip_address)
                for light in lights:
                    lights[light].on = False
                print("Turning off all the light")
                engine.say("Turning off all the light")
                engine.runAndWait()
            elif response in ['turn on all lights', 'turn on', 'turn on light']:#Turns on lights
                lights = access_lights(bridge_ip_address)
                for light in lights:
                    lights[light].on = True
                print("Turning on all the light")
                engine.say("Turning on all the light")
                engine.runAndWait()
            else:
                engine.say("Sorry only turning on and off commands are avaliable at the moment!")
                print("Sorry only turning on and off commands are available atm 😥!")
            engine.runAndWait()
            
        def translate():#Translates given text to another language
            translator = Translator()
            engine.say("What langauge would you like to translate to?")
            engine.runAndWait()
            language = input("What language would you like to translate to 🌍?")
            engine.say("Type the phrase you would like to translate: ")
            engine.runAndWait()
            response = input("Type the phrase you would like to translate: ")
            translation = translator.translate((response), dest=(language))
            engine.say(f"{translation.origin} ({translation.src}) --> {translation.text} ({translation.dest})")
            engine.runAndWait()
            print(f"{translation.origin} ({translation.src}) --> {translation.text} ({translation.dest})")
            
        def news():#Displays top 10 news headlines
            from bs4 import BeautifulSoup
            print("Here are the top 10 news headlines 📰:")
            engine.say("Here are the top 10 news headlines")
            engine.runAndWait()
            url = 'https://news.google.com/news/rss'
            request = requests.get(url)
            soup = BeautifulSoup(request.content, 'xml')
            headlines = soup.findAll('item')[:10]
            news = [news.title.text for news in headlines]
            for x in news:
                print(x)
                engine.say(x)
                engine.runAndWait()


        def covid():#Shows covid-19 data to user
            url = "https://www.worldometers.info/coronavirus/"
            r = requests.get(url)
            s = soup(r.text, "html.parser")
            data = s.find_all("div", class_="maincounter-number")
            status = s.find_all("div", class_="number-table-main")
            active = s.find_all("span", class_="number-table")
            per = s.find_all("strong")
            country = s.find_all("td")
            cou=[]

            for a in country:
                cou.append(a.text)
            print("Please Enter Country Name 😷:")
            time.sleep(1)
            c=input().title()
            if c=="":
                c="World"
            b=cou.index(c)
            print("Showing Covid-19 Data for "+c)
            engine.say("Showing Covid-19 Data for"+c)
            print(cou[b].upper()+" Total Number Of Cases:"+cou[b+1]+"   New Number Of Cases:"+cou[b+2]+"   Total Number Of Deaths:"+cou[b+3]+"   New Number Of Deaths:"+cou[b+4]+" Number Of People Recovered:"+cou[b+5]+"   Active Number Of Cases:"+cou[b+6]+"   Serious Number Of Cases:"+cou[b+7]+"   cases/1Mpop:"+cou[b+8]+"   deaths/1Mpop:"+cou[b+9]+"   tests:"+cou[b+10]+"  tests/1Mpop:"+cou[b+11])
            print("\nGlobal Results")
            print("Total Number Of Cases: " + data[0].text.strip())
            print("Total Number Of Deaths: " + data[1].text.strip())
            print("Total Number Of Recovered: " + data[2].text.strip())
            print("Active Number Of Cases: " + status[0].text.strip() + "\t\t--Mild: " + active[0].text.strip() + " (" + per[
                2].text.strip() + "%)\t\t--Critical: " + active[1].text.strip() + " (" + per[3].text.strip() + "%)")
            print("Closed Cases: " + status[1].text.strip() + "\t\t--Discharged: " + active[2].text.strip() + " (" + per[
                4].text.strip() + "%)\t--Deaths: " + active[3].text.strip() + " (" + per[5].text.strip() + "%)\n")
            time.sleep(2)
            engine.say("The Data Used Is From: https://www.worldometers.info/coronavirus/")
            engine.say("For More Information On Covid-19, Please Visit: https://www.nhs.uk/conditions/coronavirus-covid-19/")
            print("The Data Used Is From: https://www.worldometers.info/coronavirus/")
            print("For More Information On Covid-19, Please Visit: https://www.nhs.uk/conditions/coronavirus-covid-19/")
            engine.runAndWait()

        def speed_test():#Speed test
            engine.say("Sped test currently offline")
            print('Speed test currently' +Fore.WHITE+ 'OFFLINE')
            print(Fore.WHITE)
            engine.runAndWait()
        #    test = speedtest.Speedtest()
        #    engine.say("Getting server list")
        #    print("Getting server list...")
        #    test.get_servers()#Gets current list of servers that can be tested
        #    engine.say("Choosing best server")
        #    print("Choosing best server to test...")
        #    best = test.get_best_server()#Gets the best server to test
        #    print(f"Found: {best['host']} loacted in {best['country']}")
        #    print("Perfoming speed test...")
        #    download_result = test.download()
        #    upload_result = test.upload()
        #   ping_result = test.results.ping_result
        #    engine.say(f"Download speed: {download_result/1024/1024:.2f} Mbit/s")
        #    engine.say(f"Upload speed: {upload_result/1024/1024:.2f} Mbit/s")
        #    engine.say(f"Ping: {ping_result:.2f} ms")
        #    print(f"Download speed: {download_result/1024/1024:.2f} Mbit/s")
        #print(f"Upload speed: {upload_result/1024/1024:.2f} Mbit/s")
        #    print(f"Ping: {ping_result:.2f} ms")
        #   engine.runAndWait()

        def help():#Shows help commands to user
            print("Here are some commands you can ask me 😃: ")
            engine.say("Here are some commands you can ask me ")
            engine.runAndWait()
            commands = ["time", "date", "calendar", "weather", "about", "clear", "joke", "wiki", "app", "qrcode", "youtube", "video", "song", "video", "lights", "translate", "wordle", "news", "covid", "periodic table",  "plot chart", "add stock", "remove stock", "portfolio value", "stock value"]
            print('\n'.join(commands))
            engine.say('\n'.join(commands))
            engine.runAndWait()


        def periodic_table():#Displays the period table in the termianl
            #period_table.csv source = https://physicallychemist.blogspot.com/2014/05/periodic-table-as-text.html
            periodicTableFile = open('periodic_table.csv', encoding='utf-8')#Opens the Periodic table csv file and reads it and closes it to access the data
            periodTableReader = csv.reader(periodicTableFile)
            elements = list(periodTableReader)
            periodicTableFile.close()

            COLUMNS = ['atomic Number','symbol', 'name','atomic mass','CPK color','electronic config','electronegativity','atomic radius','ion radius','van der Waals','IE-1','EA','oxidation states','standard state','bonding type', 'melting point','boiling point','density','metal','year discovered']
            LONGEST_COLUMN = 0
            for key in COLUMNS:
                if len(key) > LONGEST_COLUMN:
                    LONGEST_COLUMN = len(key)

            ELEMENTS = {}
            for line in elements:
                element = {'atomic Number': line[0],'symbol': line[1],'name': line[2],'atomic mass': line[3] +'au','CPK color': line[4],'electronic config': line[5],'electronegativity': line[6],'atomic radius': line[7],'ion radius': line[8],'van der Waals': line[9],'IE-1': line[10],'EA': line[11],'oxidation states': line[12],'standard state': line[13],'bonding type': line[14],'melting point': line[15],'boiling point': line[16],'density': line[17],'metal': line[18],'year discovered': line[19]}
            for key, value in element.items():
                element[key] = re.sub(r'\[(I|V|X)+\]', '', value)

            ELEMENTS[line[0]] = element
            ELEMENTS[line[1]] = element
            print()
            engine.say("Showing The Periodic Table Of Elements")
            print("The Periodic Table Of Elements")
            print('''    1   2   3   4   5   6   7   8   9   10  11  12  13  14  15  16  17  18
   -----                                                               -----
 1 | H |                                                               |He |
   |---+----                                       --------------------+---|
 2 |Li |Be |                                       | B | C | N | O | F |Ne |
   |---+---|                                       |---+---+---+---+---+---|
 3 |Na |Mg |                                       |Al |Si | P | S |Cl |Ar |
   |---+---+---------------------------------------+---+---+---+---+---+---|
 4 | K |Ca |Sc |Ti | V |Cr |Mn |Fe |Co |Ni |Cu |Zn |Ga |Ge |As |Se |Br |Kr |
   |---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---|
 5 |Rb |Sr | Y |Zr |Nb |Mo |Tc |Ru |Rh |Pd |Ag |Cd |In |Sn |Sb |Te | I |Xe |
   |---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---|
 6 |Cs |Ba |LAN|Hf |Ta | W |Re |Os |Ir |Pt |Au |Hg |Tl |Pb |Bi |Po |At |Rn |
   |---+---+---+------------------------------------------------------------
 7 |Fr |Ra |ACT|
   -------------
                -------------------------------------------------------------
     Lanthanide |La |Ce |Pr |Nd |Pm |Sm |Eu |Gd |Tb |Dy |Ho |Er |Tm |Yb |Lu |
                |---+---+---+---+---+---+---+---+---+---+---+---+---+---+---|
     Actinide   |Ac |Th |Pa | U |Np |Pu |Am |Cm |Bk |Cf |Es |Fm |Md |No |Lw |
                ------------------------------------------------------------- ''')
            engine.say("Enter An Element Symbol Or The Atomic Number To Find Out More Information Or Type back ")
            print("Enter An Element Symbol Or The Atomic Number To Find Out More Information Or Type back: ")
            user_response = input('Enter Element: ').title()
            if user_response == 'back':
                print("\n")
                engine.say("Hi, How Can I Help?")
                print("Hi, How Can I Help? 💬")

            if user_response in ELEMENTS:
                for key in COLUMNS:
                    keyJustified = key.rjust(LONGEST_COLUMN)
                    print(keyJustified +':' + str(ELEMENTS[user_response][key]))
                engine.say("To Continue Press The Enter Key")
                input('To Continue Press The ENTER KEY!!!')
            engine.runAndWait()







        def version():#Shows system/app info
            print(Fore.CYAN)
            print("About Talia Chat:")
            print(Fore.WHITE)
            text = pyqrcode.create('https://github.com/T-Kalv/Tasp-Talia-')
            print(text.terminal(module_color='black', background='white'))
            time.sleep(1)
            my_system = platform.uname()
            print()
            print("Edition: Chat")
            print(f"OS: {my_system.system}")
            print(f"Device Name: {my_system.node}")
            print(f"Machine: {my_system.machine}")
            print(f"Processor: {my_system.processor}\n")
            print(Fore.YELLOW)
            print("Software Version Number: "+ version_name)
            print("Software Type: Public-Beta-Preview")
            print(Fore.GREEN)
            print("Last Update: "+last_update)
            print(Fore.WHITE)

        def networking():#Displays network info
            print("Here's your system networking information 🖥️ : ")
            engine.say("Here's your system networking information")
            print(Fore.WHITE)
            network_data = subprocess.check_output(['ipconfig','/all']).decode('utf-8').split('\n') #Tracerses the ipconfig info
            for item in network_data:
                print(item.split('\r')[:-1])#Outputs the ipconfig info in a readable format
            engine.runAndWait()

            

        def wordle():

            def checkwordle(theAnswer, theGuess):
                position = 0
                hint = ""
                colours = []
                for letter in theGuess:
                    if letter == theAnswer[position]:
                        hint += "G"
                        colours.append(Fore.GREEN)
                    elif letter in theAnswer:
                        hint += "Y"
                        colours.append(Fore.YELLOW)
                    else:
                        hint += "#"
                        colours.append(Fore.WHITE)
                    position +=1
                print(
                    colours[0]+theGuess[0]+Fore.RESET+
                    colours[1]+theGuess[1]+Fore.RESET+
                    colours[2]+theGuess[2]+Fore.RESET+
                    colours[3]+theGuess[3]+Fore.RESET+
                    colours[4]+theGuess[4]+Fore.RESET
                    )
                return hint == "GGGGG"


            wordle_list = []
            wordle_file = open("wordle_words.txt")
            for word in wordle_file:
                wordle_list.append(word.strip())
            answer = random.choice(wordle_list)
            number_of_guess = 0
            correct_guess = False
            print(Fore.WHITE)
            while number_of_guess < 6 and not correct_guess:
                guess = input("Enter a 5 letter word: ")
                engine.say("Enter a 5 letter word")
                print("\n")
                number_of_guess +=1
                correct_guess = checkwordle(answer, guess)
                print("\n")
            if correct_guess:
                engine.say("let's goooooooo! you correctly guessed the word in "+str(number_of_guess)+" tries")
                print("Let's goooooooooooo! You correctly guessed the word in "+str(number_of_guess)+" tries!")
            else:
                engine.say("Unfortunately, you have used up all of your guesses. The correct word to guess was "+answer)
                print("Unfortunately, you have used up all of your guesses. The correct word to guess was "+answer)
            engine.runAndWait()


        def snake():
            print("Add snake cli code!")

        def games():#Displays available games that you can play
            engine.say("Here are the games you can play")
            print("Here are the games you can play:")
            engine.say("wordle")
            print("wordle")
            engine.runAndWait()


        def qrcode():#Genetaye a qrcode from user input
            engine.say("Enter url or text to generate qr code")
            print("Enter URL or text to generate QR CODE: ")
            code = input()
            time.sleep(1)
            text = pyqrcode.create(code)
            engine.say("Here is your generated qr code")
            print(text.terminal(module_color='black', background='white'))
            engine.runAndWait()

        def code():#Shows the user code for a programming langauge (currenlt hello world in 7 languages)
            engine.say("Which programming langauge would you like?")
            response = input("Which programming language would you like? ")
            if response in ["C#", "c#"]:
                engine.say("What would you like the code for?")
                code = input("What would you like the code for? ")
                if code in ["hello world", "Hello World"]:
                    test = open("scripts\C#_code\hello_world.txt","r+")
                    print(test.read())
                    test.close()
            elif response in ["python", "Python"]:
                engine.say("What would you like the code for?")
                code = input("What would you like the code for? ")
                if code in ["hello world", "Hello World"]:
                    test = open("scripts\Python_code\hello_world.txt","r+")
                    print(test.read())
                    test.close()
            elif response in ["C", "c"]:
                engine.say("What would you like the code for?")
                code = input("What would you like the code for? ")
                if code in ["hello world", "Hello World"]:
                    test = open("scripts\C_code\hello_world.txt","r+")
                    print(test.read())
                    test.close()
            elif response in ["C++", "c++"]:
                engine.say("What would you like the code for?")
                code = input("What would you like the code for? ")
                if code in ["hello world", "Hello World"]:
                    test = open("scripts\C++_code\hello_world.txt","r+")
                    print(test.read())
                    test.close()
            elif response in ["HTML", "html"]:
                engine.say("What would you like the code for?")
                code = input("What would you like the code for? ")
                if code in ["hello world", "Hello World"]:
                    test = open("scripts\HTML_code\hello_world.txt","r+")
                    print(test.read())
                    test.close()
            elif response in ["Java", "java"]:
                engine.say("What would you like the code for?")
                code = input("What would you like the code for? ")
                if code in ["hello world", "Hello World"]:
                    test = open("scripts\Java_code\hello_world.txt","r+")
                    print(test.read())
                    test.close()
            elif response in ["typescript", "TypeScript"]:
                engine.say("What would you like the code for?")
                code = input("What would you like the code for? ")
                if code in ["hello world", "Hello World"]:
                    test = open("scripts\TypeScript_code\hello_world.txt","r+")
                    print(test.read())
                    test.close()
                else:
                    engine.say("Sorry I can't provide code for that right now!")
                    print("Sorry I can't provide code for that right now!")
            else:
                engine.say("Unfortunaly, I don't support that programming language right now. Please try a different programming langauge instead!")
                print("Unfortunaly, I don't support that programming language right now. Please try a different programming langauge instead!")
            engine.runAndWait()    
            
                
        def world():
            print("Here's the world map 🌎: ")
            engine.say("Here's the world map")
            print(r"""
                      ..::^^::::^^^^^^^^^::.        ....                  ..                        
     .....     :::::.:::::^:....:^!!!!!!!!^.        .....     ........::^^~~~~^::::...^:...         
:...^~!!~~~~~~~~~~~~~^~~::::^~^.  :~~^:....:.     .:^^^~~~^^^^~~~~~!~!!!!!!!!!!!!!!!~!!!!!~~~~~^^   
    .::...::^!!!!!!!!!!^:. :~~^^.   .          .  :~~::~~!!!!!!!!!!!!!!!!!!!!!!!!!!!!~^:::^~:...    
             .^~!!!!!!!!!!~~!!~::^            .:^^~!~!!!~~~!!~~!!!!!!!!!!!!!!!!!!!!!!^:.  ..        
               ~!!!!!!!!!!!!^^.               :^^:::^^~^:::~!^:!!!!!!!!!!!!!!!!!~~~^..:             
                :~~!!!~~~~~:                  ^~^~~^:.:..:~!!~~!!!!!!!!!!!!!!!!!~ . .:.             
                  :^~!^ . .                 :~!!!!!!!!!!~~^~!~^~^^^~!!!!~!!!!~~~:                   
                    .^::^: .                ~!!!!!!!!!!!!!^:~~~:    ^!^...^~!^.  .                  
                         :  ^~^^:           :~~~~~~!!!!!!!!~~^       :     .::   ..                 
                           ^!!!!!~^.          .   .~!!!!!!!~:.             :: :^.    .              
                          .~!!!~!!!!~~^            .~!!~!!~.                . ....   :^::           
                           .^~!~~!~!!~.            .~!~~!!~:.^                   .:^~:::.           
                             :!~~!!~^.              ^!!!!~  ::                 :~~!!!!!!^.          
                             ^!!!~^                  ^~^^                      ^~^^^^~!!!^          
                            .~!^:.                                                    :^:     .:.   
                            :!^                                                              .:     
                            .:.                                                                     
                                                              ..            .  .                    
                ... .:......:^^^            .:::::^:^^^:^^^^~~~~~~~:^^~~~~~~~~~~~~~~~~~~^^^^:.      
      .::~~~~~~~~~~~~!!!!!!~^^::. .^^..:^^~~~!!!!!!!!!!!!!!!!!!~!!!!!!!!!!!!!!!!!!!!!!!!!!!!^.      
^^~^^^^~~~~~!~~~~!!~~~~~~~~~~~!~~~~!!!!~~!!~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^.  
""")
            engine.runAndWait()

        def unit_converter():
            print("Here are all the options available to convert: ")
            engine.say("Here are all the options available to convert")
            engine.runAndWait()
            print(Fore.GREEN)
            units = [(1, 'mi', 'km'),
                     (2, 'km', 'mi'),
                     (3, '°C', '°F'),
                     (4, '°F', '°C'),
                     (5, 'kg', 'lbs'),
                     (6, 'lbs', 'kg')
                    ]

            for unit_number, from_unit, to_unit in units:
                print(f'{unit_number}: {from_unit} --> {to_unit}')

            print()
            print(Fore.WHITE)
            conversion = input("Which option would you like to convert: ")
            engine.say("Which option would you like to convert")
            engine.runAndWait()
            try:
                unit_index = int(conversion) - 1
            except:
                print("Enter a valid option!")
                engine.say("Enter a valid option")
                engine.runAndWait()

            unit_number, from_unit, to_unit = units[unit_index]
            from_value = float(input(f'Input: {from_unit} = '))

            if unit_number == 1:#mi to km
                engine.say("Converting mile to kilometre")
                engine.runAndWait()
                to_value = from_value*1.61
                print(f'{from_value} {from_unit} --> {to_value} {to_unit}')

            elif unit_number == 2:#km to mi
                engine.say("Converting kilometre to mile")
                engine.runAndWait()
                to_value = from_value*0.62
                print(f'{from_value} {from_unit} --> {to_value} {to_unit}')

            elif unit_number == 3:# °F to °C
                engine.say("Converting fahrenheit to celsius")
                engine.runAndWait()
                to_value = (from_value - 32)/1.8
                print(f'{from_value} {from_unit} --> {to_value} {to_unit}')

            elif unit_number == 4:# °C to °F
                engine.say("Converting celsius to fahrenheit")
                engine.runAndWait()
                to_value = from_value*1.8+32
                print(f'{from_value} {from_unit} --> {to_value} {to_unit}')

            elif unit_number == 5:#kg to lbs
                engine.say("Converting kilogram to pound")
                engine.runAndWait()
                to_value = from_value*0.45
                print(f'{from_value} {from_unit} --> {to_value} {to_unit}')

            elif unit_number == 6:#lbs to kg
                engine.say("Converting pound to kilogram")
                engine.runAndWait()
                to_value = from_value*2.22
                print(f'{from_value} {from_unit} --> {to_value} {to_unit}')

            else:
                print("Please enter a valid option!")
                engine.say("Please enter a valid option")
                engine.runAndWait()

        def random_fact():
            random_facts = randfacts.get_fact()
            print("Here's a random fact for you: ")
            engine.say("Here's a random fact for you")
            print(random_facts)
            print("*Disclaimer: The Facts Provided May Not Always be True!")
            engine.say(random_facts)
            engine.runAndWait()

        def quadratic_solver():
            print("Here's the Quadratic Solver: ")
            engine.say("Here's the Quadratic Solver")
            engine.runAndWait()
            print(Fore.GREEN)
            print("ax^2 + bx + c = 0")
            print(Fore.WHITE)
            print("Please enter the values of a, b and c!")
            engine.say("Please enter the values of a, b and c")
            engine.runAndWait()
            a = float(input("a: "))
            b = float(input("b: "))
            c = float(input("c: "))
            d = (b**2) - (4*a*c)
            if d > 0:
                x1 = (-b-cmath.sqrt(d))/(2*a)
                x2 = (-b+cmath.sqrt(d))/(2*a)
                print("x = {0} or x = {1}".format(x1, x2))
                engine.say("x = {0} or x = {1}".format(x1, x2))
                engine.runAndWait()
            elif d == 0:
                x1 = -b/(2*a)
                print("x = {0}".format(x1))
                engine.say("x = {0}".format(x1))
                engine.runAndWait()
            else:
                print("No soltions exist!")
                engine.say("No soltions exist")
                engine.runAndWait()




        def clear():#Clears the terminal to default view
            response = input("Would you like to clear the termial/cli 🥺 [Y/n]?")
            if response in ['y', 'Y']:
                if os.name == "nt":
                    os.system('cls')
                else:
                    os.system("clear")
                print("-----------------------------------------------------")
                print("\n")
                print(Fore.WHITE)
                print('Status: '+ Fore.GREEN + 'ONLINE')
                print(Fore.WHITE)
                print("\n")
                now = datetime.datetime.now()
                print(now)
                print("\n")
                engine.say("Hi, How Can I Help?")
                print("Hi, How Can I Help? 💬")
                engine.runAndWait()
            elif response in ['n', 'N']:
                print("Ok 😌")
                engine.say("Ok")
                engine.runAndWait()
            else:
                print("Sorry I don't understand 😥")
                engine.say("Sorry I don't understand")
                engine.runAndWait()    

        def save_portfolio():
            with open('data/portfolio.pkl', 'wb') as f:
                pickle.dump(portfolio, f)
                          
        def update_portfolio():#Updates user stock portfolio
            print('\033[1;37m')
            engine.say("Which stock would you like to have")
            symbol = input("Which stock would you like to have 📈: ")#Stock/ticker
            engine.say("How many shares would you like to have")
            quantity = input("How many shares would you like to have: ")
            engine.runAndWait()
            if symbol in portfolio.keys():
                portfolio[symbol] += int(quantity)
            else:
                portfolio[symbol] = int(quantity)
                save_portfolio()

        def remove_portfolio():#Removes shares/stock from user stock portfolio
            print('\033[1;37m')
            engine.say("Which stock would you like to sell")
            symbol = input("Which stock would you like to sell 📉: ")
            engine.say("How many shares would you like to sell")
            quantity = input("How many shares would you like to sell: ")
            engine.runAndWait()
            if symbol in portfolio.keys():
                if int(quantity) <= portfolio[symbol]:
                    portfolio[symbol] -= int(quantity)
                    save_portfolio()
                else:
                    print(f"You don't own enough shares for {symbol}")
            else:
                print(f"You don't own any shares in {symbol}")
            
        def view_portfolio():#Shows stock portfolio to user
            print('\033[1;37m')
            engine.say("This is your current portfolio")
            print("This is you current portfolio: ")
            engine.runAndWait()
            for symbol in portfolio.keys():
                print(f"You currently own {portfolio[symbol]} shares in {symbol}")
            
        def chart_plot():#Shows stock chart to user
            print('\033[1;37m')
            engine.say("Enter a stock symbol")
            symbol = input("Enter a stock symbol: ")
            engine.say("Enter a start date in the DD/MM/YYYY format")
            begin_str = input("Enter a start date in the DD/MM/YYYY format 📅: ")
            engine.runAndWait()
            plt.style.use('dark_background')
            begin = dt.datetime.strptime(begin_str, "%d/%m/%Y")
            finish = dt.datetime.now()
            data = web.DataReader(symbol, 'yahoo', begin, finish)
            colors = mpf.make_marketcolors(up='#00ff00', down='#ff0000', wick='inherit', edge='inherit', volume='in')
            mpf_style = mpf.make_mpf_style(base_mpf_style='nightclouds', marketcolors=colors)
            chart_proc = threading.Thread(target=open_graph,args=[data,mpf_style],daemon=True)
            chart_proc.start()

        def portfolio_value():#Shows value of stock portfolio to user
            print('\033[1;37m')
            sum = 0
            for symbol in portfolio.keys():
                data = web.DataReader(symbol, 'yahoo')
                price = data['Close'].iloc[-1]
                sum += price
            print(f"Your current portfolio is valued at 💲{sum} USD")
            
        def portfolio_gains():#Shows stock gains
            print('\033[1;37m')
            engine.say("Please enter the starting date in the YYYY-MM-DD format")
            start_date = input("Please enter the starting date in the YYYY-MM-DD format 📅: ")
            engine.runAndWait()
            try:
                for symbol in portfolio.keys():
                    data = web.DataReader(symbol, 'yahoo')
                    current_price = data['Close'].iloc[-1]
                    start_price = data.loc[data.index == start_date]['Close'].values[0]
                    current_sum += current_price
                    start_sum += start_price
                print(f"Your portfolio gains are: 💲{current_sum-start_sum} USD")
            except IndexError:
                engine.say("ERROR No Trades On This Date!")
                print("ERROR No Trades On This Date! 😥")

        def understand():
            engine.say("Sorry I don't understand!")
            print("Sorry I don't understand! 😥")
            engine.runAndWait()
        
        mappings = {
            'greeting': greeting,
            'goodbye': goodbye,
            'thanks': thanks,
            'help': help,
            'name': name,
            'tasp': tasp,
            'talia': talia,
            'feeling': feeling,
            'language': language,
            'tasp': tasp,
            'time': gettime,
            'calendar': calendar,
            'date': date,
            'joke': joke,
            'getweather': weather,
            'wiki': wiki,
            'youtube': youtube,
            'video': video,
            'image': image,
            'play_song': play_song,
            'app': app,
            'version': version,
            'philips_hue': philips_hue,
            'translate': translate,
            'news': news,
            'covid': covid,
            'speed_test': speed_test,
            'networking': networking,
            'wordle': wordle,
            'snake': snake,
            'games': games,
            'qrcode': qrcode,
            'code': code,
            'clear': clear,
            'world': world,
            'unit_converter': unit_converter,
            'random_fact': random_fact,
            'quadratic_solver': quadratic_solver,
            'understand': understand,
            'periodic_table': periodic_table,
            'chart_plot': chart_plot,
            'update_portfolio': update_portfolio,
            'remove_portfolio': remove_portfolio,
            'view_portfolio': view_portfolio,
            'portfolio_gains': portfolio_gains,
            "portfolio_value": portfolio_value
        }
        tasp = GenericAssistant('data/intents.json', mappings, "TALIA_Messenger_Model")#Uses the pre-trained TALIA model to enable AI-like messaging using TALIA
        os.chdir("data")
        tasp.load_model()
        os.chdir("..")
        #For re-training TALIA model below!
        #tasp.train_model()
        #tasp.save_model()
        while True:
            text = input("")
            tasp.request(text)

    def open_graph(data, mpf_style):
        mpf.plot(data, type='candle', style=mpf_style, volume=True)

