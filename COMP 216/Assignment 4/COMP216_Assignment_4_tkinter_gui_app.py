# -*- coding: utf-8 -*-
"""
Created on Tue Feb  6 23:41:39 2024

@author: Jonathan Au - 300827701
"""
import tkinter as tk
from tkinter import ttk
#from tkinter import *
#from tkinter.ttk import *

window = tk.Tk()

window.title("Centennial College")
window.geometry('650x450')
window.configure(bg='light grey')
window.minsize(650, 450)

window.columnconfigure((0,1,2), weight=1, uniform = 'a')
window.rowconfigure(0, weight=2)
window.rowconfigure((1,2,3,4,5,6,7,8), weight=1, uniform = 'a')

#Lables
title_lbl = tk.Label(window, text = "ICET Student Survey", font=("Times New Roman", 25), bg='light grey')
full_name_lbl = tk.Label(window, text = "Full name: ", bg='light grey', font=("Times New Roman", 14))
residency_lbl = tk.Label(window, text = "Residency: ", bg='light grey', font=("Times New Roman", 14))
program_lbl = tk.Label(window, text = "Program: ", bg='light grey', font=("Times New Roman", 14))
courses_lbl = tk.Label(window, text = "Courses: ", bg='light grey', font=("Times New Roman", 14))

#Textboxes
full_name_txt = tk.Entry(window, width=25, relief='raised', font=("Times New Roman", 14))

#Radio Buttons
rad_set = tk.StringVar()
dom_rad = tk.Radiobutton(window, text='Domestic', value='Dom', variable=rad_set,
                         bg='light grey', font=("Times New Roman", 14))
intl_rad = tk.Radiobutton(window, text='International', value='Intl', variable=rad_set, 
                          bg='light grey', font=("Times New Roman", 14))
rad_set.set(None)

#Combobox
Program_combo = ttk.Combobox (window, font=("Times New Roman", 14))
Program_combo['values'] = ('AI', 'Gaming', 'Health', 'Software', 'Robotics')
#Program_combo.current(0)

#Checkbox
chk1 = tk.StringVar()
chk2 = tk.StringVar()
chk3 = tk.StringVar()
comp100_chk = tk.Checkbutton(window, text='Programming I', onvalue='Comp 100', offvalue='', 
                             variable=chk1, bg='light grey', font=("Times New Roman", 14))
comp213_chk = tk.Checkbutton(window, text='Web Page Design', onvalue='Comp 213', offvalue='', 
                             variable=chk2, bg='light grey', font=("Times New Roman", 14))
comp120_chk = tk.Checkbutton(window, text='Software Engineering', onvalue='Comp 120', offvalue='', 
                             variable=chk3, bg='light grey', font=("Times New Roman", 14))

#button events
def __init__():
    Reset_Event()
    
def Reset_Event():
    for i in window.winfo_children():
        if isinstance(i, tk.Entry):
            i.delete(0,'end')
        if isinstance(i, tk.Checkbutton):
            i.deselect()
        if isinstance(i, ttk.Combobox):
            i.delete(0,'end')
        if isinstance(i, tk.Radiobutton):
            rad_set.set(None)

def Okay_Event():
    #event here
    chk_group = [chk1, chk2, chk3]
    chk_out = ''
    rad_out = rad_set.get()
    if rad_set.get() == "None":
        rad_out = ''
    for i in chk_group:
        chk_out = chk_out + i.get() + '\n\t'
    tk.messagebox.showinfo('Information', 'Name: ' +full_name_txt.get() + '\n' 
                           + 'Program: ' + Program_combo.get() + '\n' 
                           + 'Residency: ' + rad_out + '\n' 
                           + 'Program: ' + chk_out )

#Buttons
reset_btn = tk.Button(window, text="Reset", command=Reset_Event, width=25, font=("Times New Roman", 15))
Okay_btn = tk.Button(window, text="OK", command=Okay_Event, width=25, font=("Times New Roman", 15))
Exit_btn = tk.Button(window, text="Exit", command=window.destroy, width=25, font=("Times New Roman", 15))

#Grid placements
title_lbl.grid(column=0, row=0, columnspan=3, rowspan=2, padx=10, pady=10, sticky='nsew')
full_name_lbl.grid(column=0, row=2, padx=10, pady=10, sticky='nsew')
full_name_txt.grid(column=1, row=2, padx=10, pady=10, sticky='nsew')
residency_lbl.grid(column=0, row=3, rowspan=2, padx=10, pady=10, sticky='new')
dom_rad.grid(column=1, row=3, padx=10, pady=10, sticky='nsw')
intl_rad.grid(column=1, row=4, padx=10, pady=10, sticky='nsw')
program_lbl.grid(column=0, row=5, padx=10, pady=10, sticky='nsew')
Program_combo.grid(column=1, row=5, padx=10, pady=10, sticky='nsew')
courses_lbl.grid(column=0, row=6, rowspan=3, padx=10, pady=10, sticky='new')
comp100_chk.grid(column=1, row=6, padx=10, pady=10, sticky='nsw')
comp213_chk.grid(column=1, row=7, padx=10, pady=10, sticky='nsw')
comp120_chk.grid(column=1, row=8, padx=10, pady=10, sticky='nsw')
reset_btn.grid(column=0, row=9, padx=10, pady=10, sticky='nsew')
Okay_btn.grid(column=1, row=9, padx=10, pady=10, sticky='nsew')
Exit_btn.grid(column=2, row=9, padx=10, pady=10, sticky='nsew')



window.mainloop()
