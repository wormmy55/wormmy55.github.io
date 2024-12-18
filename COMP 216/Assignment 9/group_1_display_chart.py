# -*- coding: utf-8 -*-
"""group_1_display_chart.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1HveH6TNAU45G-11KP1MEzo5GNXDnQRlT

#Group 1
Name: Salma Chaaban <br>
Student number: 301216551 <br>
Name: Hodan Ahmed Yusuf<br>
Student number: 301226634<br>
Name: Jonathan Au<br>
Student number: 300827701<br>
Name: Landon Essex<br>
Student number: 301349452<br>
Name: Michael Angelo Cabalinan <br>
Student number: 300924795 <br>
COMP 216 - assignment 9

#Lab 11 – Display chart.
We will build a GUI to display a set of values. You will display the values using both a line chart and a bar chart on the same app. Most of the coding will come from Week_09_lab_09_Display.docx. You will make the following modification to your solution of lab09 or lab10:
1.	In the constructor create a list of 20 values from your generator class in Lab 8. This will not change for the life of the application. (You must get these values explicitly form your previous code)
2.	In the initUI() method do the following:
o	Add the code that will create the three widgets at the top of the window as shown in the screenshot below.
o	Call the method below that will draw the rectangles and lines as shown in the screenshot.
o	Wire-up the button to read the input from the textbox and call the method in step 3 with the appropriate arguments.
3.	Define a method that takes the start values (the list of values is available as a class attribute) and will draw the six rectangles and the lines.

##Requirements:
1.	You will use the same quantity that you selected in the previous lab (from temperature, humidity, barometric pressure, customers at a mall, or just with an alternate descriptor).
2.	Design and build a GUI application class that will model a display for your sensor reasonably well.
3.	You must provide an Entry (Textbox) and a button to read the value and call the method to draw the rectangles and lines.
4.	There are marks for aesthetics.
See the appendix of the previous week lab for some code sample and possible directions to explore.

##Rubrics <br>
[Class] 4/4<br>
[unitUI Method] 3/3<br>
[Button Handler] 2/2<br>
[Draw rectangle] 6/6<br>
[Gui] 2/2<br>
[Aesthetics] 3/3<br>
Total 20/20<br>
"""

import tkinter as tk
from tkinter import ttk, messagebox
import random
import math

class DataGenerator:
    def __init__(self, root, ymin=0, ymax=60, daily_mean=19, daily_amps=[1.2, 2, 3, 2.5, 3.5], stddev=2.4):
        self.root = root
        self.ymin = ymin
        self.ymax = ymax
        self.daily_mean = daily_mean
        self.daily_amps = daily_amps
        self.daily_freqs = [2.5 * math.pi / 100, 1 * math.pi / 100, 2 * math.pi / 100, 1.2 * math.pi / 100, 1.8 * math.pi / 100]
        self.stddev = stddev
        self.t = 0

    def initUI(self):
        self.root.title("Temperature Display - Static Series Display")

        self.chart_label = ttk.Label(self.root, text="TEMPERATURE STATIC DISPLAY", font=("Helvetica", 16, "bold"))
        self.chart_label.pack(pady=(20, 0))

        self.canvas = tk.Canvas(self.root, width=500, height=250)
        self.canvas.pack()

        self.data_range_label = ttk.Label(self.root, text="", font=("Helvetica", 12))
        self.data_range_label.pack(pady=10)

        self.input_label = ttk.Label(self.root, text="Please enter data range value:", font=("Helvetica", 10))
        self.input_label.pack(pady=(0, 10))

        self.input_entry = ttk.Entry(self.root, width=10)
        self.input_entry.pack(pady=(0, 20))
        self.input_entry.insert(0, "0")

        self.update_btn = ttk.Button(self.root, text="ENTER", command=self.update_chart)
        self.update_btn.pack(pady=(10, 40))

        self.values = self.generate_values(20)

        self.draw_chart()

    def __rand_values(self):
        return random.uniform(0, 1)

    @property
    def transform(self):
        y = ((self.ymax - self.ymin) * self.__rand_values()) - self.ymin
        return y

    def generate_values(self, count):
        data = []
        num_points = 500
        for _ in range(num_points):
            daily_variation = sum([amp * math.sin(self.t * freq) for amp, freq in zip(self.daily_amps, self.daily_freqs)])
            value = self.daily_mean + daily_variation + random.gauss(0, self.stddev * 2)
            data.append(value)
            self.t += 1
        return data

    def draw_chart(self):
        self.canvas.delete("all")
        start_values = self.values[:6]

        bar_width = 300 / 6
        total_width = bar_width * len(start_values)
        x_start = (500 - total_width) / 2
        y_start = 250
        bar_height_factor = 6

        for i, value in enumerate(start_values):
            x = x_start + i * bar_width
            bar_height = value * bar_height_factor
            self.canvas.create_rectangle(x, y_start - bar_height, x + bar_width, y_start, fill="#A0CED9")

        for i in range(len(start_values) - 1):
            x1 = x_start + i * bar_width + bar_width / 2
            x2 = x_start + (i + 1) * bar_width + bar_width / 2
            y1 = y_start - start_values[i] * bar_height_factor
            y2 = y_start - start_values[i + 1] * bar_height_factor
            self.canvas.create_line(x1, y1, x2, y2, fill="#0D3B66", width=2)

    def update_chart(self):
        try:
            start_index = int(self.input_entry.get())
            if start_index < 0 or start_index > 15:
                messagebox.showerror("Error", "Please enter a valid starting value between 0 and 15.")
            else:
                data_range = f"{start_index}-{start_index + 6}"
                self.data_range_label.config(text=f"Data range: {data_range}")
                start_values = self.values[start_index:start_index + 6]
                if len(start_values) < 6:
                    messagebox.showerror("Error", "Not enough values to display.")
                else:
                    self.canvas.delete("all")
                    self.draw_chart_with_lines(start_values)
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number.")


    def draw_chart_with_lines(self, start_values):
        self.canvas.delete("all")
        bar_width = 300 / 6
        total_width = bar_width * len(start_values)
        x_start = (500 - total_width) / 2
        y_start = 250
        bar_height_factor = 6

        for i, value in enumerate(start_values):
            x = x_start + i * bar_width
            bar_height = value * bar_height_factor
            y = y_start - bar_height
            self.canvas.create_rectangle(x, y, x + bar_width, y_start, fill="#A0CED9")

        for i in range(len(start_values) - 1):
            x1 = x_start + i * bar_width + bar_width / 2
            x2 = x_start + (i + 1) * bar_width + bar_width / 2
            y1 = y_start - start_values[i] * bar_height_factor
            y2 = y_start - start_values[i + 1] * bar_height_factor
            self.canvas.create_line(x1, y1, x2, y2, fill="#0D3B66", width=2)

if __name__ == "__main__":
    root = tk.Tk()
    app = DataGenerator(root)
    app.initUI()
    root.mainloop()