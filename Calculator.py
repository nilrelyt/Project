import tkinter as tk
from tkinter import ttk

# create window
window = tk.Tk()
window.title('PyCalculator')
window.geometry('500x600')

entry = ttk.Entry(master = window)
entry.pack()

button = ttk.Button(master = window, text = 'Enter')
button.pack()

label = ttk.Label(master = window, text = '^')
label.pack()

# should run LAST
# mainloop updates the GUI and checks for events
window.mainloop()
