import os
import webbrowser

def quest_parser(line, command):
    quest = ["who", "what", "where", "when", "why", "how"]
    url = "https://www.google.com/search?q=" + line
    webbrowser.register('chrome',
	None,
	webbrowser.BackgroundBrowser("C://Program Files (x86)//Google//Chrome//Application//chrome.exe"))
    webbrowser.get('chrome').open_new(url)
    


def action_parser(line, command):
    action = ["show", "tell", "play", "start", "can", "open"]
    rest = " ".join(line.split()[1:])
    if command == "play":
        song = rest+".mp3"
        os.startfile(song)