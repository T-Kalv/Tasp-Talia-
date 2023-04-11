import pip

packages = [
        "install",

        # tells pip to install the packages below,
        # MAKE SURE EACH ENTRY ENDS WITH A COMMA!!!
        "windows-curses",
        "pandas-datareader",
        "pystray",
        "Pillow",
        "winotify",
        "pyfiglet",
        "neuralintents",
        "matplotlib",
        "catppuccin-matplotlib",
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
        "speedtest-cli",
        "randfacts",
        "WazeRouteCalculator",

        # end of packages

        "--exists-action","i"
]

def install():

    # remove windows-curses if not on windows
    import os
    if os.name != "nt":
        packages.remove("windows-curses")

    print("installing deps")
    pip.main(packages)
    
    # this thing
    import nltk
    nltk.download('all')
