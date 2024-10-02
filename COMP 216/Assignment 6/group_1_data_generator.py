# -*- coding: utf-8 -*-
"""group_1_data_generator.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1vP6OwqJFRFnPZR89OEGFdT7upqx7qFv5

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
Student number: <br>

1.	Create a <b>class</b> that does the following:
2.	Create a <b>private</b> method that will generate random values in the range 0-1. Look at the examples at the end of this document for ideas on approaching this. <br>
This method may take argument that can be passed by the property below.
3.	Create a <b>public property</b> that will use the above member to return a value in your preferred range. You may use a simple transformation of the form:<br>
y=mx + c<br>
where y is the intended output<br>
m is the range of your values i.e (Xmax - Xmin)<br>
x is the output of the method in step 2, and <br>
c is the smallest value of your output i.e. Xmin

4.	You will use the Matplotlib library to display your data values. The output must look professional. You will label your <b>output axes</b> and <b>title</b> appropriately.

5.	Code to drive (run your program)
"""

import math
import random

#1. Class
class DataGenerator:

  def __init__(self, ymin=18, ymax=25, daily_mean=19, daily_amps=[2, 1.5, 2, 1.8, 2.2], stddev=0.5):
    self.ymin = ymin
    self.ymax = ymax

    # Parameters for daily sine fluctuations
    self.daily_mean = daily_mean
    self.daily_amps = daily_amps
    self.daily_freqs = [2 * math.pi / 100, 0.5 * math.pi / 100, 1.8 * math.pi / 100, 0.8 * math.pi / 100, 1.1 * math.pi / 100]  # 100 temperature readings per day

    self.stddev = stddev

    self.t = 0

  #2. private method
  def __rand_values(self):
    return random.uniform(0,1)

  #3. public property
  def generate_data(self, num_points):
          data = []
          for _ in range(num_points):
              daily_variation = sum([amp * math.sin(self.t * freq) for amp, freq in zip(self.daily_amps, self.daily_freqs)])
              value = self.daily_mean + daily_variation + self.__rand_values()
              data.append(value)
              self.t += 1
          return data

  #4. You will use the Matplotlib library to display your data values. The output must look professional. You will label your output axes and title appropriately.
import matplotlib.pyplot as plt

def visualize_data(data):
    plt.figure(figsize=(10, 6))
    plt.plot(data, color='red')
    plt.title('Variation of Temperature')
    plt.xlabel('Time(hours)')
    plt.ylabel('Temperature (°C)')
    plt.grid(True)
    plt.show()

  #5. Code to drive (run your program)
if __name__ == "__main__":
    generator = DataGenerator()
    data_points = 500
    data = generator.generate_data(data_points)
    visualize_data(data)

"""See the appendix of this document for some code sample and possible directions to explore. You will need some combination of the last three examples.<br>
  •	Use generator_4() will give peaks and valleys. You may also use a sin function or some other function that will give you the base shape. <br>
  •	Use generator_3() to change the length (or frequency) of the peaks.<br>
  •	Use generator_2() and to get the squiggles.<br>
DO NOT USE THE CODE AS IS! Look at the intension behind the code.

"""
