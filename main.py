# IDEA - Create a GUI with a Textfield with pre-loaded text. The user must type the text and as they type, the text scrolls down. They can select time options. (5 seconds, 10, 60). They are timed and then after the time runs out, the WPM is displayed. Can also try and calculate it in real-time.
from tkinter import *


def change_time():
    pass


def on_typing(event=None):
    current_text = text_field.get("1.0", END).strip()
    print("Live input:", current_text)


def close_app():
    root.destroy()


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
        command=change_time,
    )
    rb.configure(bg="gray")
    rb.pack()

# TODO - Create Textfield where text is loaded.
text_field = Text(root, wrap="word", font=("Arial", 12), bg="white", fg="black")
text_field.pack()

text_field.bind("<KeyRelease>", on_typing)
# TODO - Exit application
btn_close = Button(
    root, text="Close Application", command=close_app, bg="gray", fg="black"
)
btn_close.pack()

# TODO - Load Text.

# TODO - Change colour of text

# TODO - Configure/create timer.

# TODO - Add replayability.

# TODO - Display WPM

# TODO - Loop
root.mainloop()
