# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 16:40:09 2024

@author: drago
"""

#This is the code for the one I posted in our Teams chat. 
#I used your code and combined it to the one I made last week.

import tkinter as tk
from tkinter import ttk, messagebox
import random
import math

class DataGenerator:
    def __init__(self, root, ymin=0, ymax=60, daily_mean=19, daily_amps=[2, 1.5, 2, 1.8, 2.2], stddev=0.5):
        self.root = root
        self.ymin = ymin
        self.ymax = ymax
        self.daily_mean = daily_mean
        self.daily_amps = daily_amps
        self.daily_freqs = [2 * math.pi / 100, 0.5 * math.pi / 100, 1.8 * math.pi / 100, 0.8 * math.pi / 100, 1.1 * math.pi / 100]
        self.stddev = stddev
        self.t = 0

        self.root.title("Temperature Gauge")

        self.canvas = tk.Canvas(self.root, width=400, height=250)
        self.canvas.pack()

        self.label = ttk.Label(self.root, text="Temp(°C):")
        self.label.pack()

        self.temp_label = ttk.Label(self.root, text="", font=("Helvetica", 16, "bold"))
        self.temp_label.pack(pady=(0, 30))

        self.input_label = ttk.Label(self.root, text="Enter temperature:")
        self.input_label.pack()

        self.input_entry = ttk.Entry(self.root, width=10)
        self.input_entry.pack(pady=(0, 20))

        self.input_entry.insert(0, str(random.randint(self.ymin, self.ymax)))

        self.update_btn = ttk.Button(self.root, text="UPDATE", command=self.update_temp)
        self.update_btn.pack(pady=(10, 40))

        self.update_temp()

    def _normalized_value(self):
        return random.gauss(0, 1)

    def update_temp(self):
        try:
            temp_input = int(self.input_entry.get())
            if temp_input < self.ymin or temp_input > self.ymax:
                messagebox.showerror("Error", f"Please enter a valid temperature (between {self.ymin} and {self.ymax}).")
            else:
                self.temp_label.config(text=str(temp_input))

                self.canvas.delete("all")
                self.canvas.create_arc(50, 50, 350, 350, start=0, extent=180, outline='#CACFD6', fill='#CACFD6', width=1)
                percentage = (temp_input - self.ymin) / (self.ymax - self.ymin)
                angle = 180 * percentage
                angle = min(angle, 180)

                label_text = "Normal"
                if temp_input < 10:
                    label_text = "Low"
                elif temp_input > 40:
                    label_text = "High"

                self.canvas.create_arc(50, 50, 350, 350, start=180, extent=-angle, outline='#FFFD82',fill='#FFFD82', width=1)

                self.canvas.create_text(50, 220, anchor="sw", text=str(self.ymin), fill="black")
                self.canvas.create_text(350, 220, anchor="se", text=str(self.ymax), fill="black")
                self.canvas.create_text(200, 230, anchor="s", text=label_text, fill="black", font=("Helvetica", 12, "bold"))

        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number.")

if __name__ == "__main__":
    root = tk.Tk()
    app = DataGenerator(root)
    root.mainloop()
