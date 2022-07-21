#Uses data from: https://finance.yahoo.com
import os
import time
import datetime
import pandas_datareader as web
from winotify import Notification, audio

now = datetime.datetime.now()#Shows current date and time
print(now)
print("\n")
time.sleep(1)
symbols = ["AAPL"]#Stock symbol/ticker
max_value = [112]#Specify the max price to sell
low_value = [110]#Specify the lowest price to buy    
while True:
    last_price_update = [web.DataReader(symbol, "yahoo")["Adj Close"][-1] for symbol in symbols]#Uses the yahoo api to get the last_prices of the stock
    print(last_price_update)
    time.sleep(5)
    for i in range(len(symbols)):
        if last_price_update[i] > max_value[i]:
            toast = Notification(app_id="TASP",
            title="Price Change For: " + symbols[i], 
            msg=f"{symbols[i]} Has Reached A Price Of: {last_price_update[i]:.2f}. You Should Consider Selling!", 
            icon=os.path.join(os.getcwd(), "sell.png"), 
            duration="long")
            toast.add_actions(label = "Go To Stockbroker To SELL Stock!")
            toast.set_audio(audio.LoopingAlarm10, loop=True)#Notify user to sell stock through sound alert
            toast.show()    
        elif last_price_update[i] < low_value[i]:
            toast = Notification(app_id="TASP",
            title="Price Change For: " + symbols[i], 
            msg=f"{symbols[i]} Has Reached A Price Of: {last_price_update[i]:.2f}. You Should Consider Buying!", 
            icon=os.path.join(os.getcwd(), "buy.png"), 
            duration="long")
            toast.add_actions(label = "Go To Stockbroker To BUY Stock!")
            #toast.add_actions(label = "Go To Stockbroker To BUY Stock!, launch="https://...") you can link directly to your desired stockbroker
            toast.set_audio(audio.LoopingAlarm9, loop=True)#Notify user to buy stock through sound alert
            toast.show()
        time.sleep(1)#Incase notifications come at the same time    






















