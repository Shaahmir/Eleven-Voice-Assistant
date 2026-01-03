# Eleven - Voice Assistant

**Eleven** is a Python-based voice assistant that allows you to interact with your computer using voice commands. It can open applications, search the web, play YouTube videos, take screenshots, control system volume, and provide the current date and time, all with a simple voice command. The assistant also features a GUI built with Tkinter for easy interaction.

---

## Features

- **Voice Recognition**: Understands natural language commands using `speech_recognition`.
- **Text-to-Speech**: Responds using `pyttsx3`.
- **Web and App Control**:
  - Opens websites in Chrome.
  - Searches Google or YouTube.
  - Opens installed applications like Notepad, Chrome, Edge, Word, Excel, etc.
- **Media Control**:
  - Plays YouTube videos directly.
  - Mutes and unmutes system volume.
- **System Utilities**:
  - Takes screenshots and saves them with timestamps.
  - Provides the current time and date.
- **GUI Interface**:
  - Interactive GUI using `Tkinter` with a ScrolledText output area.
  - Speak button for voice commands.
  - Visual feedback in the output window.

---

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/Eleven-Voice-Assistant.git
   cd Eleven-Voice-Assistant


## Command Logic

Press the Speak button and give commands like such as:

```text
- "Open notepad/ word/ vscode ..."
- "Play Cocomelon on YouTube ..."
- "Open Google and search Python tutorials ..."
- "Take a screenshot"
- "What is the time?"
- "What is today's date?"
- "Mute/ Unmute the system"
- Greetings: "Hello", "Hi", "Assalam o Allaikum", etc.
```

---

## Libraries / Requirements

This project uses the following Python libraries:

- [`tkinter`]([https://pypi.org/project/opencv-python/](https://docs.python.org/3/library/tkinter.html)): For the graphical user interface (built-in with Python).
- [`pyttsx3`]([https://pypi.org/project/mediapipe/](https://pyttsx3.readthedocs.io/en/latest/)): Text-to-speech engine for voice feedback.
- [`speech_recognition`]([https://pypi.org/project/PyAutoGUI/](https://pypi.org/project/SpeechRecognition/)): To capture and recognize voice commands.
- [`Pillow`]([https://pypi.org/project/screen-brightness-control/](https://pypi.org/project/pillow/)): For screenshot capture.

---

## Installation & Run

Install all required dependencies:

```bash
pip install pyttsx3 SpeechRecognition pillow
```

## Run the Project

```bash
python Eleven.py
```
---

## GUI

Eleven features a modern **Tkinter GUI**:

- **Main Window:** Displays voice assistant messages and responses  
- **Speak Button:** Click to start voice recognition  
- **Scrolled Text:** Shows conversation history

---

## GUI Screenshot

![GUI Screenshots](https://github.com/user-attachments/assets/dcf4ebc2-4361-43dc-aee0-45d90c17f024)

---

