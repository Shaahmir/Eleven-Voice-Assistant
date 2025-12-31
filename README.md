# Eleven – Voice Assistant (Python)

A **Voice Assistant** built with Python that listens to your voice commands and performs practical tasks on your computer. Eleven can **open desktop applications**, **launch websites in Chrome**, **take screenshots**, and **search queries on Google or YouTube**. Experience quick computing and control your system naturally using just your voice.

---

## Features

- Real-time voice recognition using `speech_recognition`
- Text-to-speech responses using `pyttsx3`
- Open desktop apps (Notepad, Calculator, Chrome, Word, Excel, VS Code, etc.)
- Open websites and search queries on **Google** and **YouTube**
- Take screenshots of your screen
- Check current **time** and **date**
- Interactive GUI with Tkinter
- Beginner-friendly and easily extendable

---

## Command Logic

Eleven responds to predefined commands such as:

```text
- "Open Chrome"
- "Open Google and search Python tutorials"
- "Open YouTube and search music videos"
- "Take screenshot"
- "What is the time?"
- "What is today's date?"
- Greetings: "Hello", "Hi", "Assalam", etc.
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
