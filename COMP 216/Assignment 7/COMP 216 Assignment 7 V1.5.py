# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 16:36:58 2024

@author: drago
"""

import tkinter as tk
from tkinter import Tk, Canvas, Frame, BOTH, W
import math


class Gauge(Frame):
    def __init__(self):
        super().__init__()
        self.initUI()


    def initUI(self):
        self.master.title('Temperature Gauge')
        self.pack(fill=BOTH, expand=1)

        self.canvas = tk.Canvas(self, width=300, height=5)

        # Text labels
        self.canvas.create_text(140, 10, anchor=W, font='Purisa',text='Temperature (°C)')
        self.temperature_label = self.canvas.create_text(175, 40, anchor=W, text="0.0", font=("Arial", 20))

        self.canvas.create_text(187, 80, anchor=W, text="0.0", font=("Arial", 14))
        self.canvas.create_text(265, 150, anchor=W, text="30.0", font=("Arial", 14))
        self.canvas.create_text(180, 220, anchor=W, text="60.0", font=("Arial", 14))
        self.canvas.create_text(95, 150, anchor=W, text="90.0", font=("Arial", 14))

        # Oval
        self.canvas.create_oval(140, 90, # top left
                                260, 210, # bottom right
                                width=2)

        # Needle in the oval, to change based on entry
        self.needle_length = 50
        self.needle = self.canvas.create_line(200, 150, 200, 140 - self.needle_length, width=2, fill='red')

        # Entry
        self.entry_widget = tk.Entry(self.canvas)
        self.entry_window = self.canvas.create_window(140, 250, anchor=tk.W, window=self.entry_widget)

        # Button
        self.button_widget = tk.Button(self.canvas, text="Change Value", command=self.buttonHandle)
        self.button_window = self.canvas.create_window(160, 280, anchor=tk.W, window=self.button_widget)

        self.canvas.pack(fill=BOTH, expand=1)

    def buttonHandle(self):
        r = 60
        angle = ((float(self.entry_widget.get())-30)*(math.pi/60))
        new_x = 200 + (r*math.cos(angle))
        new_y = 150 + (r*math.sin(angle))

        self.canvas.coords(self.needle, 200, 150, new_x, new_y)

        temperature = float(self.entry_widget.get())  # Convert input temperature to float
        # Update temperature label
        self.canvas.itemconfig(self.temperature_label, text=str(temperature))
        return self.needle


root = Tk()
ex = Gauge()
root.geometry('400x300+300+300')
root.mainloop()