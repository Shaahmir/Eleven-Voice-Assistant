import pyttsx3
import speech_recognition as sr
import pyautogui
import pywhatkit
import tkinter as tk
from tkinter.scrolledtext import ScrolledText
import webbrowser
from datetime import datetime 
import os 
import threading

# -------------------- App Dictionary --------------------

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

# -------------------- Output Text --------------------

def add_text(text):
    ouput_text.configure(state="normal")
    ouput_text.insert(tk.END, text + "\n")
    ouput_text.configure(state="disabled")
    ouput_text.see(tk.END)

# -------------------- Initialize Voice Model --------------------

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
engine.setProperty('rate',160)
engine.setProperty('volume',1)

# -------------------- Website Opener --------------------

def web_opener(message):
    list_1=list(message.split())
    i=list_1.index("open")
    desire_variable=list_1[i+1]
    add_text(f"El: opening, {desire_variable} in chrome")
    engine.say(f"opening {desire_variable} in chrome")
    webbrowser.open(f"http://www.{desire_variable}.com")

# -------------------- App Opener --------------------

def app_opener(message):
    list_1=list(message.split())
    i=list_1.index("open")
    desire_variable=list_1[i+1: ]
    str_1=""
    for x in desire_variable:
        str_1 += (x+" ")
    str_1 = str_1.strip()
    if str_1 in apps:
        os.system(apps[str_1])
        add_text(f"El: opening, {desire_variable}")
        engine.say(f"opening {desire_variable}")
    else:
        add_text(f"El: sorry, I didn't find {desire_variable} anywhere")
        engine.say(f"sorry, I didn't find {desire_variable} anywhere")      

# -------------------- Action Function --------------------

def action(message):
    add_text(f"you said: {message}")

    # ----------------- Opening Google and searching -----------------
    if "open google and search" in message:
        list_1 = list(message.split())
        i = list_1.index("search")
        desire_variable = list_1[i + 1:]
        str_1 = ""
        for x in desire_variable:
            str_1 += (x + " ")
        str_1 = str_1.strip()
        add_text(f"El: Opening Google and searching for {str_1}")
        engine.say(f"Opening Google and searching for {str_1}")
        webbrowser.open(f"https://www.google.com/search?q={str_1}")

    # ----------------- Opening Youtube and searching -----------------          
    elif "open youtube and search" in message:
        list_1 = list(message.split())
        i = list_1.index("search")
        desire_variable = list_1[i + 1:]
        str_1 = ""
        for x in desire_variable:
            str_1 += (x + " ")
        str_1 = str_1.strip()
        add_text(f"El: Opening Youtube and searching for {str_1}")
        engine.say(f"Opening Youtube and searching for {str_1}")
        webbrowser.open(f"https://www.youtube.com/results?search_query={str_1}")

    # ----------------- Playing the first video appears on yt after searching -----------------
    elif "play" in message:
        list_1 = list(message.split())
        i = list_1.index("play")
        desire_variable = list_1[i+1:]
        str_1 = " "
        for x in desire_variable:
            str_1 += (x + " ")
        str_1 = str_1.strip()
        add_text(f"El: Currently Playing {str_1}")
        engine.say(f"Roger that, playing {str_1} on youtube")
        pyautogui.press("volumeup", presses=100)
        pywhatkit.playonyt(str_1)

    # ----------------- Mute -----------------
    elif "mute" in message:
        add_text(f"El: system muted {message}")
        pyautogui.press("volumemute")

    # ----------------- Umute -----------------
    elif "unmute" in message:
        add_text(f"El: system muted {message}")
        pyautogui.press("volumemute")
        engine.say(f"Umuted the system {message}")

    # ----------------- Opening direct website link -----------------    
    elif "open" in message and ("web" in message or "in chrome" in message):
        web_opener(message)

    # ----------------- Opening apps -----------------
    elif "open" in message:
        app_opener(message)

    # ----------------- Showing Time -----------------
    elif "time" in message:
        time_now = datetime.now().strftime("%I:%M %p")
        add_text(f"El: The current time is {time_now}")
        engine.say(f"The current time is {time_now}")

    # ----------------- Showing Date -----------------
    elif "date" in message:
        today = datetime.now().strftime("%d %B %Y")
        add_text(f"El: The current time is {today}")
        engine.say(f"The current time is {today}")
    
    # ----------------- Screenshot -----------------
    elif "screenshot" in message:
        add_text("El: Screenshot Taken")
        engine.say("Screenshot Taken")
        screenshot = pyautogui.screenshot()
        screenshot.save(f"Screenshot {datetime.now().strftime('%f')}.png")

    #----------------- Greetings in English -----------------
    elif ("hello" in message or "hey" in message or "hi" in message) and not("what" in message):
        add_text(f"El: Hello, How may I help you?")
        engine.say("Hello, How may I help you?")

    #----------------- Greetings in Urdu -----------------
    elif "salam" in message or "assalam" in message:
        add_text(f"El: Wallikum Assalam, How may I help you?") 
        engine.say("Wallikum Assalam, How may I help you?")

    #----------------- If none of above match search it on google -----------------
    else:
        add_text(f"El: searching {message} on Google")
        engine.say(f"searching {message} on Google")
        webbrowser.open(f"https://www.google.com/search?q={message}")

# ----------------- Voice Recognition -----------------

def recognizer():
    recognizer = sr.Recognizer()

    try:
        with sr.Microphone(device_index=2) as source:
            add_text("Calibrating Microphone...")
            recognizer.adjust_for_ambient_noise(source,duration=1)
            add_text("Listening...")
            audio = recognizer.listen(source,timeout=10,phrase_time_limit=10)
            message= recognizer.recognize_google(audio)
            action(message.lower())

    except sr.WaitTimeoutError:
        add_text("Eleven: Listening timed out, please try again") #add this text

    except sr.UnknownValueError: ##add text 
        add_text("Eleven: Could not understand, please speak clearly") #add this text

    except sr.RequestError: ##add text
        add_text("Server: Speech service unavailable") #add this text

    except Exception as e:
         add_text(f"Error:{str(e)}")

# ----------------- Threading -----------------
 
def start_listening():
    threading.Thread(target=recognizer).start()

# ----------------- GUI -----------------

root = tk.Tk()
root.title("Eleven - Voice Assistant")
root.iconbitmap("./images/favicon_transparent.ico")
root.geometry("1080x700")
root.configure(bg="#E6E6FA")

# ----------------- Heading -----------------

icon_img = tk.PhotoImage(file="./images/logo.png")
label_text = tk.Label(root, text="Eleven - A Voice Assistant", font=("Segoe UI", 24, "bold"), fg="#6A5ACD", bg="#E6E6FA", image=icon_img, compound="left", padx=10)
label_text.pack(pady=20)

# ----------------- Output textarea -----------------

ouput_text = ScrolledText(root, width=60, height=12, font=("Segoe UI", 12), wrap=tk.WORD, bg="#FFFFFF", fg="#606060", state="disabled")
ouput_text.pack(pady=20)

# ----------------- Speak button -----------------

listen_button = tk.Button(root, text="Speak", width=10, font=("Segoe UI", 14), bg="#9370DB", fg="#FFFFFF", command=start_listening)
listen_button.pack(pady=20)

# ----------------- Starting text -----------------

add_text("El: Welcome to Eleven a Voice Assistant Chatbot")
engine.runAndWait()
engine.say("Welcome to Eleven A Voice Assistant Chatbot")

root.mainloop()
