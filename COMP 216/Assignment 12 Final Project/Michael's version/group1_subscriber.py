import tkinter as tk
from tkinter import ttk, messagebox
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class SubscriberGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Subscriber GUI")

        self.valid_min_label = ttk.Label(self.root, text="Valid Min:")
        self.valid_min_label.pack()
        self.valid_min_entry = ttk.Entry(self.root)
        self.valid_min_entry.pack()

        self.valid_max_label = ttk.Label(self.root, text="Valid Max:")
        self.valid_max_label.pack()
        self.valid_max_entry = ttk.Entry(self.root)
        self.valid_max_entry.pack()

        self.connect_btn = ttk.Button(self.root, text="Connect", command=self.connect_publisher)
        self.connect_btn.pack()

        self.disconnect_btn = ttk.Button(self.root, text="Disconnect", command=self.disconnect_publisher)
        self.disconnect_btn.pack()

        self.fig, self.ax = plt.subplots()
        self.ax.set_xlabel('Time')
        self.ax.set_ylabel('Value')
        self.line, = self.ax.plot([], [], label='Received Data')
        self.ax.legend()
        self.canvas = FigureCanvasTkAgg(self.fig, self.root)
        self.canvas.get_tk_widget().pack()

    def connect_publisher(self):
        pass

    def disconnect_publisher(self):
        pass

    def update_chart(self, x_data, y_data):
        self.line.set_data(x_data, y_data)
        self.ax.relim()
        self.ax.autoscale_view()
        self.canvas.draw()

if __name__ == "__main__":
    root = tk.Tk()
    app = SubscriberGUI(root)
    root.mainloop()
