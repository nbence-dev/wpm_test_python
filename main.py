# IDEA - Create a GUI with a Textfield with pre-loaded text. The user must type the text and as they type, the text scrolls down. They can select time options. (5 seconds, 10, 60). They are timed and then after the time runs out, the WPM is displayed. Can also try and calculate it in real-time.
from tkinter import *
from texts import passages
import random

started_timer = False
total_words = 0
time_left = 0
minutes = 0


# def rb_set_time():


def on_typing(event=None):
    global started_timer, total_words, time_left, minutes
    if not started_timer:
        time_left = selected_option.get()
        minutes = time_left / 60
        start_timer()
        started_timer = True

    
    typed = text_input.get("1.0", END).rstrip("\n")
    passage = text_field.get("1.0",END).rstrip("\n")

    text_field.config(state=NORMAL)
    
    #clear previous coloring
    text_field.tag_remove('correct','1.0',END)
    text_field.tag_remove('incorrect','1.0',END)

    #color each typed character
    for i, char in enumerate(typed):
        if i < len(passage):
            tag = 'correct' if char == passage[i] else "incorrect"
            text_field.tag_add(tag,f"1.{i}",f"1.{i+1}")

    text_field.config(state=DISABLED)

    passage_words = passage.split()
    typed_words = typed.split()
    total_words = sum(1 for i, word in enumerate(typed_words) if i < len(passage_words) and word == passage_words[i])


def start_timer():
    global time_left, total_words, minutes
    if time_left > 0:
        timer_label.config(text=f"Time: {time_left}s")
        time_left -= 1
        root.after(1000, start_timer)
    else:
        timer_label.config(text="Time: 0s")
        text_field.config(state=DISABLED)
        text_input.config(state=DISABLED)
        # calc word per minute
        wpm = total_words / minutes
        wpm_label.config(text=f"WPM: {wpm:.1f}")



def close_app():
    root.destroy()

def load_passage():
    passage = random.choice(passages)
    text_field.delete("1.0",END)
    text_field.insert(END, passage)

def restart_app():
    global time_left, started_timer, total_words, minutes, chosen_passage
    started_timer = False
    total_words = 0
    time_left = -1
    minutes = 1
    text_field.tag_remove('correct','1.0',END)
    text_field.tag_remove('incorrect','1.0',END)
    text_field.config(state=NORMAL)
    text_input.config(state=NORMAL)
    text_field.delete('1.0',END)
    selected_option.set(5)
    text_input.delete('1.0',END)
    wpm_label.config(text='WPM: --')
    timer_label.config(text="Time: --")
    load_passage()
    


# TODO - Create GUI
root = Tk()
root.title("WPM Speed Test")
root.geometry("600x600")
root.configure(bg="gray")

# TODO - Add buttons with options or radiogroup (5,10,60)
# default value
selected_option = IntVar(value=5)

options = {"5 seconds": 5, "10 seconds": 10, "60 seconds": 60}
for opt in options:
    rb = Radiobutton(
        root,
        text=opt,
        variable=selected_option,
        value=options[opt],
        
    )
    rb.configure(bg="gray")
    rb.pack()

wpm_label = Label(root, text="WPM: --", bg='gray')
wpm_label.pack()

timer_label = Label(root, text="Time: --", bg='gray', font=("Arial", 14, "bold"))
timer_label.pack()

# TODO - Create Textfield where text is loaded.
text_field = Text(root, wrap="word", font=("Arial", 12), bg="white", fg="black", height=10)
text_field.tag_config('correct', foreground='green')
text_field.tag_config('incorrect', foreground='red')
load_passage()
text_field.config(state=DISABLED)
text_field.pack()

# text_field.bind("<KeyRelease>", on_typing)
type_here_label = Label(root,text="Type below:", bg='white',fg='black')

type_here_label.pack()

text_input = Text(root,wrap='word',font=('Arial',12),bg='white',fg='black', height=10)
text_input.pack()
text_input.bind('<KeyRelease>',on_typing)
# TODO - Exit application
btn_close = Button(
    root, text="Close Application", command=close_app, bg="gray", fg="black"
)
btn_close.pack()

btn_restart = Button(root, text="Restart", command=restart_app, bg='gray', fg='black')
btn_restart.pack()
# TODO - Load Text.

# TODO - Change colour of text

# TODO - Configure/create timer.

# TODO - Add replayability.

# TODO - Display WPM

# TODO - Loop
root.mainloop()
