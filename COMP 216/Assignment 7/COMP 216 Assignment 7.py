# -*- coding: utf-8 -*-
"""
Created on Tue Mar 19 13:00:47 2024

@author: drago
"""
import tkinter as tk
from tkinter import Tk, Canvas, Frame, BOTH, W
import math

# Temperature generator from the previous lab
class DataGenerator:
    def __init__(self, ymin=18, ymax=25, daily_mean=19, daily_amps=[2, 1.5, 2, 1.8, 2.2], stddev=0.5):
        self.ymin = ymin
        self.ymax = ymax
        self.daily_mean = daily_mean
        self.daily_amps = daily_amps
        self.daily_freqs = [2 * math.pi / 100, 0.5 * math.pi / 100, 1.8 * math.pi / 100, 0.8 * math.pi / 100, 1.1 * math.pi / 100]
        self.stddev = stddev
        self.t = 0

    def generate_data(self):
        daily_variation = sum([amp * math.sin(self.t * freq) for amp, freq in zip(self.daily_amps, self.daily_freqs)])
        value = self.daily_mean + daily_variation
        self.t += 1
        return value

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
        self.canvas.create_text(170, 40, anchor=W, text="20.0", font=("Arial", 20))
        
        self.canvas.create_text(187, 60, anchor=W, text="0.0", font=("Arial", 14))
        self.canvas.create_text(265, 130, anchor=W, text="30.0", font=("Arial", 14))
        self.canvas.create_text(180, 200, anchor=W, text="60.0", font=("Arial", 14))
        self.canvas.create_text(95, 130, anchor=W, text="90.0", font=("Arial", 14))

        # Oval
        self.canvas.create_oval(140, 70, # top left
                                260, 190, # bottom right
                                width=2)

        # Needle in the oval, to change based on entry
        self.needle_length = 50
        self.needle = self.canvas.create_line(200, 130, 200, 120 - self.needle_length, width=2, fill='red')

        # Entry
        self.entry_widget = tk.Entry(self.canvas)
        self.entry_window = self.canvas.create_window(140, 220, anchor=tk.W, window=self.entry_widget)

        # Button
        self.button_widget = tk.Button(self.canvas, text="Change Value", command=self.buttonHandle)
        self.button_window = self.canvas.create_window(160, 250, anchor=tk.W, window=self.button_widget)

        self.canvas.pack(fill=BOTH, expand=1)

    def buttonHandle(self):
        r = 60
        angle = ((int(self.entry_widget.get())-30)*(math.pi/60))
        new_x = 200 + (r*math.cos(angle))
        new_y = 130 + (r*math.sin(angle))
        
        self.canvas.coords(self.needle, 200, 130, new_x, new_y)
        return self.needle


root = Tk()
ex = Gauge()
root.geometry('400x300+300+300')
root.mainloop()