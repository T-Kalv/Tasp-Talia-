# TASP aka Totally Auto Stock Pinger
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

frequency = 60#how often TASP checks for stocks

#Proper code below 
try:
    import threading, os, time, pystray, PIL.Image
    import pandas_datareader as web
    from datetime import datetime
    from winotify import Notification, audio
    import TALIA

except ImportError:
    import deps
    deps.install()
    print("Please re-run!")
    exit()

#Notifications
os.chdir("..")
startnotif = Notification(app_id="TASP",
                    title="TASP is currently running!", 
                    msg="Use the System Tray icon to pause!",
                    icon=os.path.join(os.getcwd(), "assets/traybaricon.ico"),
                    duration="short")
endnotif = Notification(app_id="TASP",
                    title="TASP has been paused!", 
                    msg="Use the System Tray icon to resume!",
                    icon=os.path.join(os.getcwd(), "assets/traybaricon.ico"),
                    duration="short")

def fetch(stuff):
    # yes, creative, i know
    return [web.DataReader(thing["symbol"], "yahoo")["Adj Close"][-1] for thing in stuff]

def go():
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
                    toast = Notification(app_id="TASP",
                            title="Price Change For: " + stuff[i]["symbol"], 
                            msg=stuff[i]["symbol"]+ f" Has Reached A Price Of: {last_price_update[i]:.2f}. You Should Consider Selling!", 
                            icon=os.path.join(os.getcwd(), "assets/sell.ico"), 
                            duration="long")
                    toast.add_actions(label = "Go To Stockbroker To SELL Stock!")
                    toast.set_audio(audio.LoopingAlarm10, loop=True)#Notify user to sell stock through sound alert
                    toast.show()    
                elif last_price_update[i] < stuff[i]["min"]:
                    toast = Notification(app_id="TASP",
                            title="Price Change For: " + stuff[i]["symbol"], 
                            msg=stuff[i]["symbol"]+ f" Has Reached A Price Of: {last_price_update[i]:.2f}. You Should Consider Buying!", 
                            icon=os.path.join(os.getcwd(), "assets/buy.ico"), 
                            duration="long")
                    toast.add_actions(label = "Go To Stockbroker To BUY Stock!")
                    toast.set_audio(audio.LoopingAlarm9, loop=True)#Notify user to buy stock through sound alert
                    toast.show()
                    time.sleep(1)#In case notifications come at the same time

def on_clicked(icon, item):
    global running, x, bot
    if str(item) == "Start" and not x.is_alive():
        startnotif.show()
        running = True
        x.start()
    elif str(item) == "Stop" and x.is_alive():
        endnotif.show()
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

image = PIL.Image.open("assets/traybaricon.ico")
icon = pystray.Icon("TASP", image, menu=pystray.Menu(#Allows user to run the program in the taskbar tray
    pystray.MenuItem("Start", on_clicked),
    pystray.MenuItem("Stop", on_clicked),
    pystray.MenuItem("TALIA", on_clicked),
    pystray.MenuItem("Exit", on_clicked)#Exit 
))
notif = Notification(app_id="TASP",
                    title="TASP is running", 
                    msg="Use the System Tray icon to pause or access TALIA.",
                    icon=os.path.join(os.getcwd(), "assets/traybaricon.ico"),
                    duration="short")
notif.show()
running = True
x = threading.Thread(target=go, daemon=True)#good ol' multithreading
x.start()
bot = threading.Thread(target=TALIA.TALIA_main, daemon=True)
icon.run()
