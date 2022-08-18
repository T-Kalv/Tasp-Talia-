# TALIA aka Totally Artificial Language Intelligence Assistant
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
import time
engine = pyttsx3.init()
engine.setProperty('rate', 220) 

def TALIA_main():
    import time
    with open('data/portfolio.pkl', 'rb') as f:#Access the prebuilt portfolio containing APPL & TSLA
        portfolio = pickle.load(f)
        print('\033[1;37m')
        welcome = pyfiglet.figlet_format("Welcome To T.A.L.I.A Messenger!")
        print(welcome)
        engine.say("Welcome To Talia Messenger!")
        engine.say("Importing all preferences from home interface")
        time.sleep(2)
        engine.say("Systems are now fully operational")
        engine.runAndWait()
        import time
        time.sleep(4)
        print(r"""
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@%**========+*#%@@@@@@@@@@@@
@@@@@@@@@@*+=++*********+*+==*%@@@@@@@@@
@@@@@@@%*=+++++##%%%%%%%#+++++++#@@@@@@@
@@@@@@*=+*=+%@@@@@@@@@@@@@@@#=**==@@@@@@
@@@@@+=**=%@@@@@@@@#=@@@@@@@@@==%++@@@@@
@@@@#=*+=%@@@@@@..======@@@@@@@+=*==@@@@
@@@@==*=*@@@@@@@.@@@@@@@@@@@@@@@==*=#@@@
@@@@==#=#@@@@@@@.+######@@@@@@@@==#=#@@@
@@@@==#=#@@@@@@@#######-+@@@@@@@==#=#@@@
@@@@==#=#@@@@@@@@@@@@@@++@@@@@@@==#=#@@@
@@@@*=*==@@@@@@@=======:*@@@@@@*=*++@@@@
@@@@@+=*++@@@@@@@@@#=@@@@@@@@@*+**+%@@@@
@@@@@%*+**+*%@@@@@@@@@@@@@@@%+***+%@@@@@
@@@@@@@%++**++*%@@@@@@@@%*+++*++*@@@@@@@
@@@@@@@@@#++****+++++++++****+*@@@@@@@@@
@@@@@@@@@@@@%*++********++**%@@@@@@@@@@@
@@@@@@@@@@@@@@@@%%%%%%%%@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
""")
        print("-----------------------------------------------------")
        print("\n")
        time.sleep(1)
        now = datetime.datetime.now()
        print(now)
        print("\n")
        time.sleep(2)
        engine.say("Hi, How Can I Help?")
        print("Hi, How Can I Help?")
        engine.runAndWait()

        def greeting():
            engine.say("Hi There!")
            print("Hi There!")
            engine.runAndWait()

        def goodbye():
            engine.say("Bye!")
            print("Bye!")
            engine.runAndWait()
            sys.exit(0)

        def thanks():
            engine.say("You're Welcome")
            print("You're Welcome!")
            engine.runAndWait()

        def name():
            engine.say("I'm TALIA")
            print("I'm TALIA")
            engine.runAndWait()

        def tasp():
            engine.say("T.A.L.I.A stands for: Totally Artificial Intelligence System")
            print("T.A.L.I.A stands for: Totally Artificial Intelligence System")
            engine.runAndWait()

        def time():#Shows current time to user
            now = datetime.datetime.now()
            engine.say("The Current Time Is")
            print("The Current Time Is...")
            engine.say(now)
            print(now)
            engine.runAndWait()

        def date():#Shows the current date to user
            now = datetime.datetime.now()
            engine.say("The Date Today Is")
            print("The Date Today Is...")
            engine.say(now)
            print(now)
            engine.runAndWait()

        def weather():#Shows the weather for the user by using https://www.wttr.in/
            engine.say("Which City Would You Like The Weather For?")
            engine.runAndWait()
            location = input("Which City Would You Like The Weather For?")
            engine.say('This Is The Weather For: ' + location)
            print('This Is The Weather For: ' + location)
            engine.runAndWait()
            url = 'https://wttr.in/{}'.format(location)
            res = requests.get(url)
            print(res.text)
        
        def joke():
            engine.say("Here Is A Joke")
            print("Here's A Joke...")
            new_joke = pyjokes.get_joke(language="en", category="all")
            engine.say(new_joke)
            print(new_joke)
            engine.runAndWait()

        def save_portfolio():
            with open('data/portfolio.pkl', 'wb') as f:
                pickle.dump(portfolio, f)
                          
        def update_portfolio():#Updates user stock portfolio
            print('\033[1;37m')
            engine.say("Which stock would you like to have")
            symbol = input("Which stock would you like to have: ")#Stock/ticker
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
            symbol = input("Which stock would you like to sell: ")
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
            begin_str = input("Enter a start date in the DD/MM/YYYY format: ")
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
            print(f"Your current portfolio is valued at {sum} USD")
            
        def portfolio_gains():#Shows stock gains
            print('\033[1;37m')
            engine.say("Please enter the starting date in the YYYY-MM-DD format")
            start_date = input("Please enter the starting date in the YYYY-MM-DD format: ")
            engine.runAndWait()
            try:
                for symbol in portfolio.keys():
                    data = web.DataReader(symbol, 'yahoo')
                    current_price = data['Close'].iloc[-1]
                    start_price = data.loc[data.index == start_date]['Close'].values[0]
                    current_sum += current_price
                    start_sum += start_price
                print(f"Your portfolio gains are: {current_sum-start_sum} USD")
            except IndexError:
                engine.say("ERROR No Trades On This Date!")
                print("ERROR No Trades On This Date!")
        
        mappings = {
            'greeting': greeting,
            'goodbye': goodbye,
            'thanks': thanks,
            'name': name,
            'tasp': tasp,
            'time': time,
            'date': date,
            'joke': joke,
            'getweather': weather,
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