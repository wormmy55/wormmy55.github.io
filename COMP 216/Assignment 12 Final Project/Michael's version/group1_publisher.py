import tkinter as tk
from tkinter import ttk, messagebox
import random
from time import sleep
import paho.mqtt.client as mqtt
from data_generator import DataGenerator

class PublisherGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Publisher GUI")

        self.min_label = ttk.Label(self.root, text="Min Value:")
        self.min_label.pack()
        self.min_entry = ttk.Entry(self.root)
        self.min_entry.pack()

        self.max_label = ttk.Label(self.root, text="Max Value:")
        self.max_label.pack()
        self.max_entry = ttk.Entry(self.root)
        self.max_entry.pack()

        self.mean_label = ttk.Label(self.root, text="Daily Mean:")
        self.mean_label.pack()
        self.mean_entry = ttk.Entry(self.root)
        self.mean_entry.pack()

        self.readings_label = ttk.Label(self.root, text="Desired Number of Readings:")
        self.readings_label.pack()
        self.readings_entry = ttk.Entry(self.root)
        self.readings_entry.pack()

        self.topic_label = ttk.Label(self.root, text="Topic:")
        self.topic_label.pack()
        self.topic_entry = ttk.Entry(self.root)
        self.topic_entry.pack()

        self.update_btn = ttk.Button(self.root, text="Update", command=self.update_data)
        self.update_btn.pack()

        self.start_btn = ttk.Button(self.root, text="Start Publishing", command=self.start_publishing)
        self.start_btn.pack()

        self.stop_btn = ttk.Button(self.root, text="Stop Publishing", command=self.stop_publishing)
        self.stop_btn.pack()

        self.publisher = None

    def update_data(self):
        try:
            min_value = float(self.min_entry.get())
            max_value = float(self.max_entry.get())
            daily_mean = float(self.mean_entry.get())
            readings = int(self.readings_entry.get())
            topic = self.topic_entry.get()
            self.publisher = Publisher(min_value, max_value, daily_mean, readings, topic)
            messagebox.showinfo("Success", "Publisher data updated.")
        except ValueError:
            messagebox.showerror("Error", "Please enter valid numerical values.")

    def start_publishing(self):
        if self.publisher:
            self.publisher.start_publishing()
            messagebox.showinfo("Info", "Publishing started.")

    def stop_publishing(self):
        if self.publisher:
            self.publisher.stop_publishing()
            messagebox.showinfo("Info", "Publishing stopped.")

class Publisher:
    def __init__(self, min_value, max_value, daily_mean, readings, topic):
        self.min_value = min_value
        self.max_value = max_value
        self.daily_mean = daily_mean
        self.readings = readings
        self.topic = topic
        self.client = mqtt.Client()
        self.running = False

    def start_publishing(self):
        if not self.running:
            self.running = True
            self.client.connect('localhost', 1883)
            self.client.loop_start()
            self.publish_data()

    def stop_publishing(self):
        if self.running:
            self.running = False
            self.client.loop_stop()
            self.client.disconnect()

    def publish_data(self):
        generator = DataGenerator(self.min_value, self.max_value, self.daily_mean)
        for _ in range(self.readings):
            value = generator.get_value()
            self.client.publish(self.topic, payload=str(value))
            sleep(1)

if __name__ == "__main__":
    root = tk.Tk()
    app = PublisherGUI(root)
    root.mainloop()
