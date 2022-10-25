import pip

def install():
    print("installing deps")
    pip.main([
        "install",

        # tells pip to install the packages below,
        # MAKE SURE EACH ENTRY ENDS WITH A COMMA!!!

        "pandas-datareader",
        "pystray",
        "Pillow",
        "winotify",
        "pyfiglet",
        "neuralintents",
        "matplotlib",
        "mplfinance",
        "requests",
        "pyttsx3",
        "pyjokes",
        "nltk",
        "wikipedia",
        "phue",
        "googletrans",
        "requests-html",
        "pyautogui",
        "pyqrcode",
        "opencv-python",
        "playsound",
        "speedtest-cli"

        # end of packages

        "--exists-action","i"
    ])
    
    # this thing
    import nltk
    nltk.download('all')
