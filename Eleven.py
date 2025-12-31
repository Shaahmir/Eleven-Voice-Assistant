import tkinter as tk #importing Tkinter for GUI
from tkinter.scrolledtext import ScrolledText #importig some part of Tkinter.scrolled Text
import pyttsx3 #Stands for Python Text-to-speech for voice output
import speech_recognition as sr #for voice recognition
from PIL import ImageGrab

#Default Python Libraries
import webbrowser #for opening URLs
from datetime import datetime #for getting today's Date and Time
import os #importing os just to open calculator
import threading #for multi tasking

apps = {
    "notepad": "notepad",
    "calculator": "calc",
    "cmd": "cmd",
    "command prompt": "cmd",
    "powershell": "powershell",
    "task manager": "taskmgr",
    "control panel": "control",
    "settings": "start ms-settings:",
    "file explorer": "explorer",
    "file": "explorer",

    "chrome": r'"C:\Program Files\Google\Chrome\Application\chrome.exe"',
    "google chrome": r'"C:\Program Files\Google\Chrome\Application\chrome.exe"',
    "edge": "msedge",
    "microsoft edge": "msedge",
    "firefox": r'"C:\Program Files\Mozilla Firefox\firefox.exe"',
    "brave": r"C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe",

    "word": r'"C:\Program Files\Microsoft Office\root\Office16\WINWORD.EXE"',
    "excel": r'"C:\Program Files\Microsoft Office\root\Office16\EXCEL.EXE"',
    "powerpoint": r'"C:\Program Files\Microsoft Office\root\Office16\POWERPNT.EXE"',

    "player": "wmplayer",
    "spotify": "spotify",

    "paint": "mspaint",
    "snipping tool": "snippingtool",
    "camera": "start microsoft.windows.camera:",

    "vs code": "code",
    "visual studio code": "code",
    "python idle": "idle",
}

# ----------------- Initialize TTS -----------------
engine = pyttsx3.init() #initializing voice agent
voices = engine.getProperty('voices') #getting all available voice agents
engine.setProperty('voice', voices[1].id)  # Female voice 0 for Male
engine.setProperty('rate', 160) #160 wpm
engine.setProperty('volume', 1) #with full volume

# ----------------- Helper Function to Add Text -----------------
def add_text(text):
    output_text.configure(state='normal') #enable editing mode
    output_text.insert(tk.END, text + "\n") #inserting text
    output_text.configure(state='disabled') #disable editing mode
    output_text.see(tk.END) #automatically scrolls down to show the latest message

# ----------------- Open Web -----------------
def web_opener(message):
    message_list = message.split(' ')
    idx = message_list.index("open")
    des_msg = message_list[idx + 1 ]
    add_text(f"El: Opening {des_msg} in Chrome")
    engine.say(f"Opening {des_msg} in Web")
    webbrowser.open(f"https://{des_msg}.com")

#----------------- Open App -----------------

def app_opener(message):
    message_list = message.split(' ')
    idx = message_list.index('open')
    des_msg_list = message_list[idx + 1:]
    des_msg = ''
    for x in des_msg_list:
        des_msg += (x + ' ')
    if des_msg.strip() in apps.keys():
        add_text(f"El: Opening {des_msg.strip()}")
        engine.say(f"Opening {des_msg.strip()}")
        os.system(apps[des_msg.strip()])
    else:
        add_text(f"El: Sorry, I didn't find {des_msg.strip()} anywhere")
        engine.say(f"Sorry, I didn't find {des_msg.strip()} anywhere")


# ----------------- Command Processing -----------------
def process_command(message):
    add_text(f"You said: {message}")

    if "open google and search" in message:
        add_text(f"El: Opening Google and searching {message}")
        engine.say(f"Opening Google and searching {message}")
        webbrowser.open(f"https://www.google.com/search?q={message.replace(' ', '+')}")

    elif "open youtube and search" in message:
        add_text(f"El: Opening YouTube and searching {message}")
        engine.say(f"Opening YouTube and searching {message}")
        webbrowser.open(f"https://www.youtube.com/results?search_query={message.replace(' ', '+')}")

    elif "open" in message and ("web" in message or "in chrome" in message):
        web_opener(message)

    elif "open" in message:
        app_opener(message)

    elif "screenshot" in message:
        add_text("El: Screenshot Taken")
        engine.say("Screenshot Taken")
        screenshot = ImageGrab.grab()
        screenshot.save(f"screenshot{datetime.now().strftime('%f')}.png")

    elif "time" in message:
        time_now = datetime.now().strftime("%I:%M %p") #Hours Minutes AM/PM
        add_text(f"El: The current time is {time_now}")
        engine.say(f"The current time is {time_now}")

    elif "date" in message:
        date_now = datetime.now().strftime("%B %d %Y") #Month Date Year
        add_text(f"El: The current time is {date_now}")
        engine.say(f"Today's date is {date_now}")

    elif "hello" in message or "hey" in message or "hi" in message or "yo" in message or "heya" in message:
        add_text(f"El: Hello, How may I help you?")
        engine.say("Hello, How may I help you?")

    elif "assalam" in message or "salam" in message:
        add_text(f"El: Wallikum Assalam, How may I help you?")
        engine.say("Wallikum Assalam, How may I help you?")

    else:
        add_text(f"El: searching {message} on Google")
        engine.say(f"searching {message} on Google")
        webbrowser.open(f"https://www.google.com/search?q={message.replace(' ', '+')}")

# ----------------- Voice Recognition -----------------
def take_command():
    recognizer = sr.Recognizer()

    try:
        with sr.Microphone(device_index=2) as source: #automatically open/close the microphone and set souce as Microphone, 2 = Conexant ISST Audio
            add_text("Calibrating microphone...") #add this text
            recognizer.adjust_for_ambient_noise(source, duration=1) #set energy_threshold and ignore bg noise
            add_text("Listening...")#add this text

            audio = recognizer.listen( #starts listening
                source, #The microphone object you got from with sr.Microphone(...) as source:
                timeout=10, #Maximum seconds to wait for someone to start speaking. If no speech is detected in 10 seconds, it raises WaitTimeoutError.
                phrase_time_limit=10 #Maximum length of speech to record, in seconds. Even if you keep talking, it stops recording after 10 seconds.
            )

        add_text("Recognizing...") #add this text

        message = recognizer.recognize_google(audio) #sends the recorded audio to Google’s speech recognition engine
        process_command(message.lower()) #Calling process_command fucntion

    except sr.WaitTimeoutError: #After 10 sec
        add_text("Eleven: Listening timed out, please try again") #add this text
    except sr.UnknownValueError: #if the system not comprehending
        add_text("Eleven: Could not understand, please speak clearly") #add this text
    except sr.RequestError: #if microphone not working
        add_text("Server: Speech service unavailable") #add this text
    except Exception as e: #catch every error and display it as a string
        add_text(f"Error: {str(e)}") #add this text

# ----------------- Run in Thread -----------------
def start_listening():
    threading.Thread(target=take_command).start() #call take_command function and starts the thread running in the background

# ----------------- GUI -----------------
root = tk.Tk() #main GUI Window
root.title("Eleven - Voice Assistant ") #window name
root.iconbitmap("./images/favicon_transparent.ico")  #favicon
root.geometry("640x480") #window size
root.resizable(False, False) #make it unable to resize
root.configure(bg="#E6E6FA") #Adds a background in the window

# ----------------- Main Heading -----------------
icon_img = tk.PhotoImage(file="./images/logo.png")
title_label = tk.Label(root, text="Eleven - A Voice Assistant",
                       font=("Segoe UI", 24, "bold"), fg="#6A5ACD", bg="#E6E6FA", image=icon_img, compound="left",  padx=10)
title_label.pack(pady=20)

# ----------------- Main Heading -----------------
output_text = ScrolledText(root, width=60, height=12, font=("Segoe UI", 12), wrap=tk.WORD,
                           bg="#FFFFFF", fg="#606060", state='disabled')
output_text.pack(pady=20)

# ----------------- Speak Button -----------------
listen_button = tk.Button(root, text="Speak", font=("Segoe UI", 14), command=start_listening, 
                          bg="#9370DB", fg="white", width=10)
listen_button.pack(pady=20)

# ----------------- Greetings-----------------
add_text("Eleven: How May I Help You? Press Speak To Start.")
engine.runAndWait()
engine.say("Welcome to Eleven A Voice Assistant Chatbot")

#----------------- Calling in a loop -----------------
root.mainloop()