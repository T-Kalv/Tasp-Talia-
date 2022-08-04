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
    ])
    
    # this thing
    import nltk
    nltk.download('all')
