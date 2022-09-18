import pip

def install():
    print("installing deps")
    pip.main([
        "install",
        # tells pip to install the below

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
        "speedtest-cli"
    ])
    
    # this thing
    import nltk
    nltk.download('all')
