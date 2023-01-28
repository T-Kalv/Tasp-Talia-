# TASP aka Totally Auto Stock Pinger (now cross-platform...)
# https://github.com/T-Kalv/T.A.S.P
#Uses data from: https://finance.yahoo.com

# Default stocks that the user will be notified
stuff = [
    {
        "symbol":   "TSLA",
        "max":      870.0,
        "min":      700.0
    },

    {
        "symbol":   "AAPL",
        "max":      170.0,
        "min":      160.0
    }
]

frequency = 300#how often TASP checks for stocks, here it's every 5 mins by default

#Proper code below 
try:
    import threading, os, time, pystray, PIL.Image
    import pandas_datareader as web
    from datetime import datetime
    import TALIA
    from notifypy import Notify

except ImportError:
    import deps
    deps.install()
    print("Please re-run!")
    exit()

#Notifications
os.chdir("../")
startnotif = Notify()
startnotif.title = "TASP is currently running!"
startnotif.message = "Use the System Tray icon to pause!"
startnotif.icon = "assets/Talia_chat.ico"

endnotif = Notify()
endnotif.title = "TASP has been paused"
endnotif.message = "Use the System Tray icon to resume!"
endnotif.icon = "assets/Talia_chat.ico"

# deal with these later on
sellnotif = Notify()
buynotif = Notify()

def fetch(stuff):
    # yes, creative, i know
    return [web.DataReader(thing["symbol"], "yahoo")["Adj Close"][-1] for thing in stuff]

def go():
    global sellnotif, buynotif
    lastran = datetime.fromtimestamp(0)#Let's gooooooo Jan 1st, 1970
    global running
    while running:
        dtime = datetime.now() - lastran
        dtime = dtime.total_seconds()#Uses datetime so no need to halt the thread
        if dtime > frequency:
            lastran = datetime.now()
            last_price_update = fetch(stuff)
            for i in range(len(stuff)):
                if last_price_update[i] > stuff[i]["max"]:
                    #Notify user to sell stock
                    sellnotif.title = "Price Change For: " + stuff[i]["symbol"]
                    sellnotif.message = stuff[i]["symbol"]+ f" Has Reached A Price Of: {last_price_update[i]:.2f}. You Should Consider Selling!"
                    sellnotif.icon = "assets/sell.ico"
                    sellnotif.send()
                    time.sleep(1)
                elif last_price_update[i] < stuff[i]["min"]:
                    #Notify user to buy stock
                    buynotif.title = "Price Change For: " + stuff[i]["symbol"]
                    buynotif.message = stuff[i]["symbol"]+ f" Has Reached A Price Of: {last_price_update[i]:.2f}. You Should Consider Buying!"
                    buynotif.icon = "assets/buy.ico"
                    buynotif.send()
                    time.sleep(1)#In case notifications come at the same time

def on_clicked(icon, item):
    global running, x, bot
    if str(item) == "Start" and not x.is_alive():
        startnotif.send()
        running = True
        x.start()
    elif str(item) == "Stop" and x.is_alive():
        endnotif.send()
        running = False
        x.join()
        x = None
        x = threading.Thread(target=go, daemon=True)
    elif str(item) == "TALIA":
        if not bot.is_alive():
            bot = None  # always set to none first
            bot = threading.Thread(target=TALIA.TALIA_main, daemon=True)
            bot.start()
    elif str(item) == "Exit":
        icon.stop()

image = PIL.Image.open("assets/Talia_chat.ico")
icon = pystray.Icon("TASP", image, menu=pystray.Menu(#Allows user to run the program in the taskbar tray
    pystray.MenuItem("Start", on_clicked),
    pystray.MenuItem("Stop", on_clicked),
    pystray.MenuItem("TALIA", on_clicked),
    pystray.MenuItem("Exit", on_clicked)#Exit 
))
notif = Notify()
notif.title = "Tasp-Talia is running!"
notif.message = "Use the System Tray icon to pause Tasp or access Talia!"
notif.icon = "assets/Talia_chat.ico"
notif.send()


running = True
x = threading.Thread(target=go, daemon=True)#good ol' multithreading
x.start()
bot = threading.Thread(target=TALIA.TALIA_main, daemon=True)
icon.run()
