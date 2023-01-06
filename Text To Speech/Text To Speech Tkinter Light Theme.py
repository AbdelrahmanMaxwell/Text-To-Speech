from tkinter import *
import tkinter.font as font
from tkinter import messagebox

import pyttsx3

main_window = Tk()
main_window.title("Text To Speech")
# Remove titlebar
main_window.overrideredirect(False)
main_window.iconbitmap("bilder/tts.ico")
main_window.geometry("842x632+400+200")
main_window.resizable(height=False, width=False)
main_window.config(bg="#111422")

# Select male or female
def voice_gender():
    global voi_gen
    voi_gen = voi.get()

# Save audio to mp3
def SaveFile():

    if entry1.get() != "":
        # init function to get an engine instance for the speech synthesis
        engine = pyttsx3.init()

        voices = engine.getProperty('voices')       #getting details of current voice
        engine.setProperty('voice', voices[voi_gen].id)   #changing index, changes voices. o for male & 1 for female

        volume = engine.getProperty('volume')   #getting to know current volume level (min=0 and max=1)
        engine.setProperty('volume',vol_scale.get())    # setting up volume level  between 0 and 1

        engine.save_to_file(entry1.get(), entry2.get() + '.mp3')

        # run and wait method, it processes the voice commands.
        engine.runAndWait()
    else:
        messagebox.showinfo("Warning", "No text in the input field.")


# Main text to speech script
def TextToSpeech():

    # init function to get an engine instance for the speech synthesis
    engine = pyttsx3.init()

    voices = engine.getProperty('voices')       #getting details of current voice
    engine.setProperty('voice', voices[voi_gen].id)   #changing index, changes voices. o for male & 1 for female

    volume = engine.getProperty('volume')   #getting to know current volume level (min=0 and max=1)
    engine.setProperty('volume',vol_scale.get())    # setting up volume level  between 0 and 1

    # say method on the engine that passing input text to be spoken
    engine.say(entry1.get())

    # run and wait method, it processes the voice commands.
    engine.runAndWait()

# Set font & images
Hind = font.Font(family='Hind', size=12, weight='bold')
textspeech = PhotoImage(file="bilder/textspeech_Light.png")
label_speech = Label(main_window, image=textspeech, bd=0, bg="#27272c")
label_speech.place(x=0, y=0)
speakbtn = PhotoImage(file="bilder/Speek_button.png")
savebtn = PhotoImage(file="bilder/save.png")

voi = IntVar()

# Default voice mode male
voi_gen = 0

# Labels
#label1 = Label(main_window, text=" Your Text Here ", bg="#f3f6ff", fg="#d5d9e6", font=Hind, relief="flat")

# Entries
entry1 = Entry(main_window, bg="#d5d9e6", fg="black", font=Hind, relief="flat")
entry2 = Entry(main_window, bg="#f3f6ff", fg="black", relief="flat")

# Button
button1 = Button(main_window, text=" Generate ", command=TextToSpeech, image=speakbtn, relief="flat", bg="#f3f6ff", activebackground="#1b58f1")
button2 = Button(main_window, text=" save ", command=SaveFile, image=savebtn, relief="flat", bg="#d5d9e6", activebackground="#444860")
malebtn = Radiobutton(main_window, text="Male", bg="#d5d9e6", selectcolor="white", fg="#858ca0" ,variable=voi, value=0, command=voice_gender)
femalebtn = Radiobutton(main_window, text="Female", bg="#d5d9e6", selectcolor="white", fg="#858ca0", variable=voi, value=1, command=voice_gender)

# Scaler for volume
vol_scale = Scale(main_window, from_=0, to=1, resolution=0.1, orient=HORIZONTAL, bg="#d5d9e6", fg="#858ca0", relief="flat", highlightthickness=0, activebackground="#1b58f1")
vol_scale.set(1.0)

# Grid
#label1.place(x=350,y=180, height=27)
entry1.place(x=160, y=215, width=530, height=50)
entry2.place(x=363, y=490)
button1.place(x=325, y=294)
button2.place(x=370, y=525)
malebtn.place(x=80, y=430)
femalebtn.place(x=160, y=430)
vol_scale.place(x=110, y=540)

main_window.mainloop()
