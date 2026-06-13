# 1) Import required libraries:
#    a) Import everything from `tkinter` to build the GUI.
#    b) Import `date` from `datetime` to display today’s date.
import tkinter as tk
from datetime import date
root = tk.Tk()
root.title("Welcome Buddy!")
root.geometry("400x300")
lbl = tk.Label(root, text="Hey There!", fg="black", bg="white", height=10, width=20)
name_lbl = tk.Label(root, text="Enter your full name:")
name_entry = tk.Entry(root)
def display():
    global message
    username = name_entry.get()
    greeting = f"Hello, {username}!"
    today = date.today()
    message = f"{greeting}\nWelcome to the program!\nToday's date is: {today}"
    text_box.insert(tk.END, message)
text_box = tk.Text(root, height=10, width=50)
btn = tk.Button(root, text="Begin", command=display, height=2, bg="blue", fg="white")
lbl.pack()
name_lbl.pack()
name_entry.pack()
btn.pack()
text_box.pack()
root.mainloop()



# 2) Create the main window using `root = Tk()`.

# 3) Set window properties:
#    a) Set the title using `root.title(...)`.
#    b) Set window size using `root.geometry(...)`.

# 4) Create the first label `lbl`:
#    a) Display text "Hey There!".
#    b) Set foreground (text) color, background color, height, and width.

# 5) Create a label `name_lbl` to ask the user for their full name.

# 6) Create an Entry widget `name_entry`:
#    a) This provides a text box for the user to type their name.

# 7) Define a function `display()` that runs when the button is clicked:
#    a) Read the user’s input from the entry box using `name_entry.get()`.
#    b) Create a greeting message using the entered name.
#    c) Create a message string that includes a welcome text and the date heading.
#    d) Use a global variable `message` so it can be accessed anywhere if needed.
#    e) Insert the greeting, message, and today’s date into the text box using `text_box.insert(...)`.

# 8) Create a Text widget `text_box`:
#    a) This is used to display output messages inside the GUI.

# 9) Create a Button widget `btn`:
#    a) Set button text to "Begin".
#    b) Set `command=display` so clicking the button calls the `display()` function.
#    c) Set height, background color, and text color.

# 10) Arrange all widgets in the window using `pack()`:
#     a) Pack the main label.
#     b) Pack the name label.
#     c) Pack the name entry box.
#     d) Pack the button.
#     e) Pack the text box.

# 11) Start the GUI event loop using `root.mainloop()`
#     so the window stays open and responds to user actions.