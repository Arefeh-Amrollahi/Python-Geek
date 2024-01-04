import tkinter as tk

def on_button_click():
    label.config(text="Hello, " + entry.get())

# Create the main window
window = tk.Tk()
window.title("Simple Tkinter Example")

# Create a label
label = tk.Label(window, text="Enter your name:")
label.pack()

# Create an entry widget for user input
entry = tk.Entry(window)
entry.pack()

# Create a button that triggers an action
button = tk.Button(window, text="Say Hello", command=on_button_click)
button.pack()

# Run the Tkinter event loop
window.mainloop()
