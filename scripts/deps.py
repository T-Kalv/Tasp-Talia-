import pip

def install():
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
        "mplfinance"
        "requests"
        "pyttsx3"
        "pyjokes"
        "urllib.request"
        "re"
        "webbrowser"
        "phue"
        "googletrans"
        "pprint"
        "bs4"
        "requests_html"
        "requests"
        "wikipedia"
    ])
    
    # this thing
    import nltk
    nltk.download('all')
