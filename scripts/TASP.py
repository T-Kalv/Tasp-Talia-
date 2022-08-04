# Totally Auto Stock Pinger
# https://github.com/T-Kalv/T.A.S.P

# you can edit these
stuff = [
    {
        "symbol":   "AMD",
        "max":      104.0,
        "min":      102.0
    },

    {
        "symbol":   "AAPL",
        "max":      170.0,
        "min":      160.0
    }
]

# how often, in seconds, to check stocks
frequency = 30


# actual code below here

import threading, os, time, pystray, PIL.Image
import pandas_datareader as web
from datetime import datetime
from winotify import Notification, audio

def fetch(stuff):
    # yes, creative, i know
    return [web.DataReader(thing["symbol"], "yahoo")["Adj Close"][-1] for thing in stuff]

def go():
    lastran = datetime.fromtimestamp(0) # epoch
    # yes, that's right, we're running this on Jan 1st, 1970
    global running
    while running:
        dtime = datetime.now() - lastran
        dtime = dtime.total_seconds()   # using datetime means we don't have to halt the thread
        if dtime > frequency:
            lastran = datetime.now()
            print("fetching")
            # Uses the yahoo finance api to get the last_prices of the stock
            last_price_update = fetch(stuff)
            print(last_price_update)
            for i in range(len(stuff)):
                if last_price_update[i] > stuff[i]["max"]:
                    toast = Notification(app_id="TASP",
                            title="Price Change For: " + stuff[i]["symbol"], 
                            msg=stuff[i]["symbol"]+ f" Has Reached A Price Of: {last_price_update[i]:.2f}. You Should Consider Selling!", 
                            icon=os.path.join(os.getcwd(), "assets/sell.png"), 
                            duration="long")
                    toast.add_actions(label = "Go To Stockbroker To SELL Stock!")
                    toast.set_audio(audio.LoopingAlarm10, loop=True)    # Notify user to sell stock through sound alert
                    toast.show()    
                elif last_price_update[i] < stuff[i]["min"]:
                    toast = Notification(app_id="TASP",
                            title="Price Change For: " + stuff[i]["symbol"], 
                            msg=stuff[i]["symbol"]+ f" Has Reached A Price Of: {last_price_update[i]:.2f}. You Should Consider Buying!", 
                            icon=os.path.join(os.getcwd(), "assets/buy.png"), 
                            duration="long")
                    toast.add_actions(label = "Go To Stockbroker To BUY Stock!")
                    toast.set_audio(audio.LoopingAlarm9, loop=True)     # Notify user to buy stock through sound alert
                    toast.show()
                    time.sleep(0.5)   # In case notifications come at the same time

def on_clicked(icon, item):
    global running, x
    if str(item) == "Start" and not x.is_alive():
        print("starting")
        running = True
        x.start()
    elif str(item) == "Stop" and x.is_alive():
        print("stopping")
        running = False
        x.join()
        x = threading.Thread(target=go, daemon=True)
    elif str(item) == "Exit":
        print("exiting")
        icon.stop()

os.chdir("..")
image = PIL.Image.open("assets/traybaricon.png")
icon = pystray.Icon("TASP", image, menu=pystray.Menu(#Allows user to run the program in the taskbar tray
    pystray.MenuItem("Start", on_clicked),
    pystray.MenuItem("Stop", on_clicked),
    pystray.MenuItem("Exit", on_clicked)#Exit 
))

print("running")
running = False # hahah, uno reverse card

x = threading.Thread(target=go, daemon=True)    # good ol' multithreading
icon.run()
