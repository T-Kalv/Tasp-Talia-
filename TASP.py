# Uses data from: https://finance.yahoo.com
import os, time, datetime, pandas_datareader as web, pystray, PIL.Image
from winotify import Notification, audio

image = PIL.Image.open("traybaricon.png")

def on_clicked(icon, item):             # Runs program from the traybar
    if str(item) == "Run TASP":         # Runs the TASP program
        now = datetime.datetime.now()   # Shows current date and time when TASP is run
        print(now)
        print("\n")
        time.sleep(1)
        symbols = ["AMD"]       # Stock symbol/ticker
        max_value = [110]       #Specify the max price to sell
        low_value = [99]        #Specify the lowest price to buy    
        while True:
            last_price_update = [web.DataReader(symbol, "yahoo")["Adj Close"][-1] for symbol in symbols]#Uses the yahoo finance api to get the last_prices of the stock
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
    elif str(item) == "Exit":#Exits the TASP program from the traybar
        icon.stop()

icon = pystray.Icon("TASP", image, menu=pystray.Menu(#Allows user to run the program in the taskbar tray
    pystray.MenuItem("Run TASP", on_clicked),#Run TASP
    pystray.MenuItem("Exit", on_clicked)#Exit 
))
icon.run()
