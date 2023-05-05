import tkinter as tk
# create a window
window = tk.Tk()
window.geometry("500x400")
# create a function to be called when button is clicked
def say_hello():
    print("Hello")

def clear_frame():
   for widgets in window.winfo_children():
      widgets.destroy()

def o():
    button = tk.Button(window, text="bye")

# add the button to the window
    button.pack()
# create a button widget



button = tk.Button(window, text="hi", command=lambda: [clear_frame(), o()])

# add the button to the window
button.pack()

# start the event loop
window.mainloop()
