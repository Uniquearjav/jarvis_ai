# Virtual Assistant using Python
This script uses various libraries such as `pyttsx3`, `speech_recognition`, `wikipedia`, `webbrowser`, `os`, `smtplib`, `pyautogui`, `psutil`, `pyjokes`, `requests`, `wolframalpha`, `pywhatkit`, `subprocess`,`PyPDF2`, `winshell`, `tkinter` to create a virtual assistant with text-to-speech and speech-to-text functionality.

## Functionalities
- wishMe(): Greet the user based on the time of day.
- takeCommand(): Listen and recognize user input through microphone.
- cpu(): Give the current CPU usage.
- screenshot(): Take a screenshot of the current screen.
- sendEmail(to, content): Send an email to a specified recipient with a specified content.

## User Interface
The script uses tkinter to create buttons for the user to interact with the virtual assistant:

- screenshot: Takes a screenshot of the current screen and saves it as ss.png.
- email: Opens a prompt to enter the recipient's email and the email content, and sends the email.
- exit: Exits the script.

## Additional Implementation
The script requires the following additional implementation:

Replace "youremail@gmail.com" and "your-password" with the user's email and password to send emails.
Add more functionalities and buttons to the user interface as needed.
Usage
To use this script, make sure you have all the necessary libraries installed and run the script in a Python environment. The script will greet you and prompt you to give a command, which it will then execute. Use the buttons on the user interface to interact with the virtual assistant.
