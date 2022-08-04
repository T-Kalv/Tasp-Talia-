# Totally Auto Stock Pinger
# https://github.com/T-Kalv/T.A.S.P

# stocks you will be notified for
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
frequency = 60


# actual code below here

try:
    import threading, os, time, pystray, PIL.Image
    import pandas_datareader as web
    from datetime import datetime
    from winotify import Notification, audio
    import messenger

except ImportError:
    import deps
    deps.install()
    print("please re-run")
    exit()


# notifs

startnotif = Notification(app_id="TASP",
                    title="TASP is running", 
                    msg="Use the System Tray icon to pause.",
                    duration="short")

endnotif = Notification(app_id="TASP",
                    title="TASP has paused", 
                    msg="Use the System Tray icon to resume.",
                    duration="short")


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
            # Uses the yahoo finance api to get the last_prices of the stock
            last_price_update = fetch(stuff)
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
    elif str(item) == "Messenger":
        if not bot.is_alive():
            bot = None  # always set to none first
            bot = threading.Thread(target=messenger.messenger_main, daemon=True)
            bot.start()
    elif str(item) == "Exit":
        icon.stop()

os.chdir("..")
image = PIL.Image.open("assets/traybaricon.png")
icon = pystray.Icon("TASP", image, menu=pystray.Menu(#Allows user to run the program in the taskbar tray
    pystray.MenuItem("Start", on_clicked),
    pystray.MenuItem("Stop", on_clicked),
    pystray.MenuItem("Messenger", on_clicked),
    pystray.MenuItem("Exit", on_clicked)#Exit 
))
notif = Notification(app_id="TASP",
                    title="TASP is running", 
                    msg="Use the System Tray icon to pause or access Messenger.",
                    duration="short")
notif.show()
running = True
x = threading.Thread(target=go, daemon=True)    # good ol' multithreading
x.start()
bot = threading.Thread(target=messenger.messenger_main, daemon=True)
icon.run()
