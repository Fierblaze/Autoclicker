import keyboard
import time
import mouse
import tkinter as tk
from tkinter import ttk
import py2exe

r = tk.Tk()
r.title('Autoclicker')
r.geometry('500x250')
label = tk.Label(r, text="Press any key", font=("Times New Roman", 30), justify="center")
label.pack()

def fun(event):
    label.destroy()
    global keybind
    keybind = event.keysym
    tk.Label(r, text="Current Keybind : " + keybind, font=("Times New Roman", 10)).grid(column=1, row=1)
    tk.Label(r, text="Select the speed :", font=("Times New Roman", 10)).grid(column=0, row=5, padx=10, pady=25)
    n = tk.StringVar()
    speed = ttk.Combobox(r, width=27, textvariable=n)
    speed['values'] = ('Yes', 0.1, 0.5, 1, 5, 10)
    speed.grid(column=1, row=5)
    button = tk.Button(r, text='Start', width=25, command=lambda: autoclicker(speed.get()), bg="green")
    button.grid(column=1, row=0)
    speed.current()


def autoclicker(speedSet):
    if speedSet == 'Yes':
        speedSet = 0

    speedSet = float(speedSet)
    while not keyboard.is_pressed(keybind):
        time.sleep(speedSet)
        mouse.click()



r.bind("<KeyRelease>", fun)
r.mainloop()