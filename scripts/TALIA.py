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
import time
import threading

def TALIA_main():
    with open('data/portfolio.pkl', 'rb') as f:#Access the prebuilt portfolio containing APPL & TSLA
        portfolio = pickle.load(f)
        print('\033[1;37m')
        welcome = pyfiglet.figlet_format("Welcome To T.A.L.I.A Messenger!")
        print(welcome)
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

        def greeting():
            print("Hey!")

        def goodbye():
            print("Bye!")
            sys.exit(0)

        def thanks():
            print("You're Welcome!")

        def name():
            print("I'm TASP")

        def tasp():
            print("T.A.S.P stands for: Totally Auto Stock Pinger")

        def save_portfolio():
            with open('data/portfolio.pkl', 'wb') as f:
                pickle.dump(portfolio, f)
            
        def update_portfolio():#Updates user stock portfolio
            print('\033[1;37m')
            symbol = input("Which stock would you like to have: ")#Stock/ticker
            quantity = input("How many shares would you like to have: ")
            if symbol in portfolio.keys():
                portfolio[symbol] += int(quantity)
            else:
                portfolio[symbol] = int(quantity)
                save_portfolio()

        def remove_portfolio():#Removes shares/stock from user stock portfolio
            print('\033[1;37m')
            symbol = input("Which stock would you like to sell: ")
            quantity = input("How many shares would you like to sell: ")
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
            print("This is you current portfolio: ")
            for symbol in portfolio.keys():
                print(f"You currently own {portfolio[symbol]} shares in {symbol}")
            
        def chart_plot():#Shows stock chart to user
            print('\033[1;37m')
            symbol = input("Enter a stock symbol: ")
            begin_str = input("Enter a start date in the DD/MM/YYYY format: ")
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
            start_date = input("Please enter the starting date in the YYYY-MM-DD format: ")
            try:
                for symbol in portfolio.keys():
                    data = web.DataReader(symbol, 'yahoo')
                    current_price = data['Close'].iloc[-1]
                    start_price = data.loc[data.index == start_date]['Close'].values[0]
                    current_sum += current_price
                    start_sum += start_price
                print(f"Your portfolio gains are: {current_sum-start_sum} USD")
            except IndexError:
                print("ERROR No Trades On This Date!")
        
        mappings = {
            'greeting': greeting,
            'goodbye': goodbye,
            'thanks': thanks,
            'name': name,
            'tasp': tasp,
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
        #tasp.train_model()
        #tasp.save_model()
        while True:
            text = input("")
            tasp.request(text)

def open_graph(data, mpf_style):
    mpf.plot(data, type='candle', style=mpf_style, volume=True)